import os
from typing import Optional, Dict

from fastapi import FastAPI, HTTPException
from pymongo.errors import DuplicateKeyError
from starlette.middleware.cors import CORSMiddleware

from app.graphs import stacked_bar_chart, df_grapes_by_side, grouped_by_chart
from app.data import MongoDB
from app.schema import GrapeBuyer, GrapeSeller, GrapeBuyerUpdate, GrapeSellerUpdate

API = FastAPI(
    title='Thru the Grapevine API',
    version="0.1.1",
    docs_url='/'
)

API.db = MongoDB()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@API.get("/version")
async def version():
    local = os.getenv("CONTEXT") == 'local'
    remote = "Run the API locally with the proper environment variables"
    password = API.db.first("Secret")["Password"] if local else remote
    return {"result": {"Version": API.version, "Password": password}}


@API.get("/collections")
async def collections():
    return {"result": API.db.get_database_info()}


@API.post("/read/grape-buyer")
async def read_grape_buyer(data: Optional[Dict] = None):
    return {"result": API.db.read("GrapeBuyers", data)}


@API.post("/read/grape-seller")
async def read_grape_seller(data: Optional[Dict] = None):
    return {"result": API.db.read("GrapeSellers", data)}


@API.post("/create/grape-buyer")
async def create_grape_buyer(data: GrapeBuyer):
    try:
        return {"result": API.db.create("GrapeBuyers", data.dict())}
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Profile ID must be unique.")


@API.post("/create/grape-seller")
async def create_grape_seller(data: GrapeSeller):
    try:
        return {"result": API.db.create("GrapeSellers", data.dict())}
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Profile ID must be unique.")


@API.post("/update/grape-buyer/{profile_id}")
async def update_grape_buyer(profile_id: str, update_data: GrapeBuyerUpdate):
    data = update_data.dict(exclude_none=True)
    return {"result": API.db.update("GrapeBuyers", {"profile_id": profile_id}, data)}


@API.post("/update/grape-seller/{profile_id}")
async def update_grape_seller(profile_id: str, update_data: GrapeSellerUpdate):
    data = update_data.dict(exclude_none=True)
    return {"result": API.db.update("GrapeSellers", {"profile_id": profile_id}, data)}


@API.get("/graph/df-grapes-by-side")
async def grapes_by_side():
    """ Tech Stack Count by Role - stacked bar chart
    Returns an Altair Chart in JSON format """
    return grouped_by_chart(
        df_grapes_by_side(API.db),
        "grapes",
        "side",
        "volume"
    ).to_dict()

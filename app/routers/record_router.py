from fastapi import APIRouter
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
from typing import Optional, Dict
from app.schema import GrapeBuyer, GrapeSeller, GrapeBuyerUpdate, GrapeSellerUpdate
from app.data import MongoDB


Router = APIRouter(
    prefix="/record",
    tags=["Record Operations"]
)


@Router.post("/read/grape-buyer")
async def read_grape_buyer(data: Optional[Dict]):
    return {"result": MongoDB().read("GrapeBuyers", data)}


@Router.post("/read/grape-seller")
async def read_grape_seller(data: Optional[Dict]):
    return {"result": MongoDB().read("GrapeSellers", data)}


@Router.post("/create/grape-buyer")
async def create_grape_buyer(data: GrapeBuyer):
    try:
        return {"result": MongoDB().create("GrapeBuyers", data.dict())}
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Profile ID must be unique.")


@Router.post("/create/grape-seller")
async def create_grape_seller(data: GrapeSeller):
    try:
        return {"result": MongoDB().create("GrapeSellers", data.dict())}
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Profile ID must be unique.")


@Router.post("/update/grape-buyer/{profile_id}")
async def update_grape_buyer(profile_id: str, update_data: GrapeBuyerUpdate):
    data = update_data.dict(exclude_none=True)
    return {"result": MongoDB().update("GrapeBuyers", {"profile_id": profile_id}, data)}


@Router.post("/update/grape-seller/{profile_id}")
async def update_grape_seller(profile_id: str, update_data: GrapeSellerUpdate):
    data = update_data.dict(exclude_none=True)
    return {"result": MongoDB().update("GrapeSellers", {"profile_id": profile_id}, data)}



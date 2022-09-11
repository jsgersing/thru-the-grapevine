from typing import Optional, Dict

from fastapi import FastAPI, HTTPException
from pymongo.errors import DuplicateKeyError
from starlette.middleware.cors import CORSMiddleware

from app.graphs import stacked_bar_chart, df_grapes_by_side, df_grapes_by_state_buyer, df_grapes_by_state_seller, \
    grouped_bar_chart, df_tons_by_state_combined, donut_chart, df_tons_by_variety_buyer, df_tons_by_variety_seller
from app.data import MongoDB
from app.model import BuyerSellerMatcher
from app.schema import GrapeBuyer, GrapeSeller, GrapeBuyerUpdate, GrapeSellerUpdate

API = FastAPI(
    title='Thru the Grapevine API',
    version="0.1.2",
    docs_url='/'
)

API.db = MongoDB()
API.matcher = BuyerSellerMatcher()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@API.get("/version")
async def version():
    # local = os.getenv("CONTEXT") == 'local'
    # remote = "Run the API locally with the proper environment variables"
    # password = API.db.first("Secret")["Password"] if local else remote
    return {"result": {"Version": API.version}}


@API.get("/collections")
async def collections():
    return {"result": API.db.get_database_info()}


@API.post("/read/grape-buyer")
async def read_grape_buyer(data: Optional[Dict]):
    return {"result": API.db.read("GrapeBuyers", data)}


@API.post("/read/grape-seller")
async def read_grape_seller(data: Optional[Dict]):
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


@API.post("/match/{profile_id}")
async def match(profile_id: str, n_matches: int):
    return {"result": API.matcher(n_matches, profile_id)}


@API.get("/graph/df-grapes-by-side")
async def grapes_by_side():
    """ Variety Volume by Side - stacked bar chart
    Returns an Altair Chart in JSON format """
    return stacked_bar_chart(
        df_grapes_by_side(API.db),
        "tons",
        "side",
        "variety"
    ).to_dict()


@API.get("/graph/df-grapes-by-state-buyer")
async def grapes_by_state_buyer():
    """ Variety Volume by State for Buyers - stacked bar chart
    Returns an Altair Chart in JSON format """
    return stacked_bar_chart(
        df_grapes_by_state_buyer(API.db),
        "tons",
        "state",
        "variety"
    ).to_dict()


@API.get("/graph/df-grapes-by-state-seller")
async def grapes_by_state_seller():
    """ Variety Volume by State for Sellers - stacked bar chart
    Returns an Altair Chart in JSON format """
    return stacked_bar_chart(
        df_grapes_by_state_seller(API.db),
        "tons",
        "state",
        "variety"
    ).to_dict()


@API.get("/graph/df-grapes-by-state-combined")
async def tons_by_state_combined():
    """ Variety Volume by Side by State - Grouped bar chart
    Returns an Altair Chart in JSON format """
    return grouped_bar_chart(
        df_tons_by_state_combined(API.db),
        "tons",
        "side",
        "variety",
        "state"
    ).to_dict()


@API.get("/graph/df-tons-by-variety-buyer")
async def tons_by_variety_buyer():
    """ Variety Volume for Buyer - Donut Chart
    Returns an Altair Chart in JSON format """
    return donut_chart(
        df_tons_by_variety_buyer(API.db),
        "variety",
        "tons"
    ).to_dict()


@API.get("/graph/df-tons-by-variety-seller")
async def tons_by_variety_seller():
    """ Variety Volume for Seller - Donut Chart
    Returns an Altair Chart in JSON format """
    return donut_chart(
        df_tons_by_variety_seller(API.db),
        "variety",
        "tons"
    ).to_dict()

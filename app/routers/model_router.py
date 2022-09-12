from fastapi import APIRouter
from app.model import BuyerSellerMatcher

Router = APIRouter(
    prefix="/model",
    tags=["Model Operations"]
)


@Router.post("/match/{profile_id}")
async def match(profile_id: str, n_matches: int):
    return {"result": BuyerSellerMatcher()(n_matches, profile_id)}

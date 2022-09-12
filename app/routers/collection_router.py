from fastapi import APIRouter
from app.data import MongoDB

Router = APIRouter(
    prefix="/collection",
    tags=["Collection Operations"]
)


@Router.get("/collections")
async def collections():
    return {"result": MongoDB().get_database_info()}

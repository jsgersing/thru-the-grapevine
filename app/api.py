from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.data import MongoDB
from app.routers import record_router, graph_router, model_router, collection_router

API = FastAPI(
    title='Thru the Grapevine API',
    version="0.1.3",
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


@API.get("/version", tags=["General Operations"])
async def version():
    # local = os.getenv("CONTEXT") == 'local'
    # remote = "Run the API locally with the proper environment variables"
    # password = API.db.first("Secret")["Password"] if local else remote
    return {"result": {"Version": API.version}}


for router in (record_router, collection_router, graph_router, model_router):
    API.include_router(router.Router)

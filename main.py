from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

from utils.api_router.register import register_routers

from utils.exceptions import ItemNotFoundError

# from .common.client.httpx_client import HTTPXClient
# from .config.env_manager import get_settings
# from .events.register import register_routers

# EnvManager = get_settings()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     app.requests_client = httpx.AsyncClient()
#     yield
#     await app.requests_client.aclose()
#
# app = FastAPI(lifespan=lifespan)
app = FastAPI(title="Clients App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000"],  # Allow specific origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

register_routers(app, "api.routers.v1", "api")

# if EnvManager.VM_CORS == "allow_all":
#     allow_origins = ["*"]
# else:
#     allow_origins = [EnvManager.FE_URL]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=allow_origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
#     expose_headers=["*"],
# )

@app.get("/")
async def get():
    return {"app": "bus booking", "version": "0.1"}

@app.exception_handler(ItemNotFoundError)
async def unicorn_exception_handler(request: Request, exc: ItemNotFoundError):
    print("===> exception_handler")
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! {exc.error_msg}, {request.method}"},
    )

handler = Mangum(app)

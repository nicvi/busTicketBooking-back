from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

from utils.api_router.register import register_routers

from utils.exceptions import ItemNotFoundError

app = FastAPI(title="Clients App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routers(app, "api.routers.v1", "api")

@app.get("/")
async def get():
    return {"app": "bus booking", "version": "0.1"}

@app.exception_handler(ItemNotFoundError)
async def unicorn_exception_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! {exc.error_msg}, {request.method}"},
    )

handler = Mangum(app)

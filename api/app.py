from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

import core
from . import register_routers

def create_app() -> FastAPI:
    app = FastAPI(title="Clients App")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3001", "http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_routers(app, "api.routers.v1", "api")

    @app.exception_handler(core.ItemNotFoundError)
    async def unicorn_exception_handler(request: Request, exc: core.ItemNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"message": f"Oops! {exc.error_msg}, {request.method}"},
        )

    @app.get("/")
    async def root():
        return {"app": "bus booking", "version": "0.1"}

    return app

from httpx import AsyncClient
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


class Proxy:
    def __init__(self, client: AsyncClient):
        self.app = Starlette(
            debug=True,
            routes=[
                Route("/{path:path}", self.handle),
            ],
        )
        self.client = client

    async def handle(self, request: Request):
        return JSONResponse(
            {
                "method": request.method,
                "url": str(request.url),
                "headers": dict(request.headers),
                "params": str(request.query_params),
            }
        )

import httpx


class HttpClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def send(self, request: httpx.Request) -> httpx.Response:
        res = await self.client.send(request)
        return res

    async def close(self):
        await self.client.aclose()

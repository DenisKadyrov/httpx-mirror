from app import App
from http_client import HttpClient
from proxy import Proxy
import uvicorn


client = HttpClient()
proxy = Proxy(client)
app = App(proxy)
proxy_app = app.proxy.app

if __name__ == "__main__":
    uvicorn.run("main:proxy_app", port=8000, reload=True)

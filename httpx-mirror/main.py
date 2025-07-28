from app import App
from config import Config
from dotenv import load_dotenv
from http_client import HttpClient
from proxy import Proxy
import uvicorn

load_dotenv()
config = Config()

client = HttpClient()
proxy = Proxy(client)
app = App(proxy)
proxy_app = app.proxy.app

if __name__ == "__main__":
    uvicorn.run("main:proxy_app", port=8000, reload=config.DEBUG)

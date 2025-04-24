from fastapi import FastAPI

from http_client import CMCHTTPClient

from config import settings

app = FastAPI(

)
cmc_client = CMCHTTPClient(
    "https://pro-api.coinmarketcap.com",
    settings.CMC_API_KEY 
)

@app.get("/cryptocurrencies")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()

@app.get("/cryptocurrencies/{currency_id}")
async def get_cryptocyrrecy(currency_id: int):
    return await cmc_client.get_currency(currency_id=currency_id)
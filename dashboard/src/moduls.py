from .http_client import CMCHTTPClient

from .config import settings

cmc_client = CMCHTTPClient(
    "https://pro-api.coinmarketcap.com",
    settings.CMC_API_KEY,
)
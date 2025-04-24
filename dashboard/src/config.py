from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    CMC_API_KEY: str

    model_config =  SettingsConfigDict(
        env_file="/Users/admin/itshka/CryptoDashboard/dashboard/.env"
    )

settings = Settings()
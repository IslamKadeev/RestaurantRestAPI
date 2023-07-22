from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: str = 8000
    database_url: str = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)

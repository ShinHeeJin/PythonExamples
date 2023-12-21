from pydantic import Field
from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    host: str = Field(default="127.0.0.1", env="host")
    port: int = Field(default=3306, env="port")

    class Config:
        env_file = ".env"


def test_base_settings():
    assert DBConfig().model_dump() == {"host": "123.123.123.123", "port": 3306123}

import ipaddress
import socket

import pytest
from pydantic import Field, validator
from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    host: str = Field(default="127.0.0.1", env="host")
    port: int = Field(default=3306, env="port")

    class Config:
        env_file = ".env"

    @validator("host", pre=True)  # default validator보다 먼저 실행
    def check_host(cls, host):
        try:
            ipaddress.ip_address(host)
            return host
        except ValueError:
            try:
                socket.gethostbyname(host)
                return host
            except socket.error:
                return ValueError("Invalid host")

    @validator("port")
    def check_port(cls, port):
        try:
            port = int(port)
        except ValueError:
            raise ValueError("Invalid port")

        if 1 <= port <= 65535:
            return port
        raise ValueError("Invalid port")


def test_base_settings():
    assert DBConfig().model_dump() == {"host": "123.123.123.123", "port": 65534}
    assert DBConfig(host="example.com", port="80").model_dump() == {"host": "example.com", "port": 80}

    with pytest.raises(ValueError):
        DBConfig(host="---", port="80")

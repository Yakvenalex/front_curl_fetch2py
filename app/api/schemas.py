from enum import Enum
from pydantic import BaseModel, Field


class StartEnum(str, Enum):
    fetch = "fetch"
    curl = "curl"


class TargetEnum(str, Enum):
    requests = "requests"
    httpx = "httpx"


class RequestData(BaseModel):
    request_type: StartEnum = Field(..., description="Вариант fetch или curl")
    target: TargetEnum = Field(..., description="Вариант requests или httpx")
    data_str: str = Field(..., description="Строка на вход")



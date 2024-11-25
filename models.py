from pydantic import BaseModel, HttpUrl
from datetime import datetime


class Lot(BaseModel):
    name: str
    picture: HttpUrl
    currentPrice: int
    lastPriceTime: datetime.time
    buyTimer: int
    winner: str = None
    owner: str
    sold: bool = False


class User(BaseModel):
    username: str
    password: str
    currentToken: str



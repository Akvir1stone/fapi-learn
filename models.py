from pydantic import BaseModel, HttpUrl
from datetime import datetime


class Lot(BaseModel):
    name: str
    picture: HttpUrl
    currentPrice: int
    lastPriceTime: datetime.time
    winner: str = None
    owner: str
    sold: bool = False



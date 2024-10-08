from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime as date


class Article(BaseModel):
    name: str
    price: float
    quantity: int
    warranty: Optional[str] = None


class TicketCreate(BaseModel):
    store_name: str
    items: List[Article]
    total: float


class TicketResponse(BaseModel):
    id: int
    store_name: str
    date: date
    items: List[Article]
    total: float

    class Config:
        orm_mode = True


class WarrantyResponse(BaseModel):
    id: int
    article_name: str
    warranty_duree: str

    class Config:
        orm_mode = True

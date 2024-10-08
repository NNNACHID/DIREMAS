from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String, index=True)
    date = Column(DateTime, default=datetime.now)
    items = Column(JSON, nullable=False)
    total = Column(Float, nullable=False)

    warranties = relationship("Warranty", back_populates="ticket")


class Warranty(Base):
    __tablename__ = "warranties"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    article_name = Column(String, nullable=False)
    garantie_duree = Column(String, nullable=False)

    ticket = relationship("Ticket", back_populates="warranties")

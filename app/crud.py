from sqlalchemy.orm import Session
from . import models, schemas


def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = models.Ticket(
        store_name=ticket.store_name,
        items=[item.model_dump() for item in ticket.items],
        total=ticket.total,
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_tickets(db: Session):
    return db.query(models.Ticket).all()



def create_warranty(
    db: Session, ticket_id: int, article_name: str, warranty_duree: str
):
    warranty = models.Warranty(
        ticket_id=ticket_id, article_name=article_name, warranty_duree=warranty_duree
    )
    db.add(warranty)
    db.commit()
    return warranty


def get_warranties(db: Session):
    return db.query(models.Warranty).all()

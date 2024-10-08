from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, database

router = APIRouter()


@router.post("/tickets", response_model=schemas.TicketResponse)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(database.get_db)):
    db_ticket = crud.create_ticket(db, ticket)
    for item in ticket.items:
        if item.warranty:
            crud.create_warranty(db, db_ticket.id, item.name, item.warranty)
    return db_ticket


@router.get("/tickets", response_model=list[schemas.TicketResponse])
def get_tickets(db: Session = Depends(database.get_db)):
    return crud.get_tickets(db)


@router.get("/warranties", response_model=list[schemas.WarrantyResponse])
def get_warranties(db: Session = Depends(database.get_db)):
    return crud.get_warranties(db)

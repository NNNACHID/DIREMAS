```
________ ______                 ______  _______ _____________________                
___  __ \__<  /________________ ___  /_ __  __ \___  /__<  /______  /____  __________
__  / / /__  / __  ___/___  __ \__  __ \_  / / /__  / __  / _  __  / _  / / /__  ___/
_  /_/ / _  /  _(__  ) __  /_/ /_  / / // /_/ / _  /  _  /  / /_/ /  / /_/ / _(__  ) 
/_____/  /_/   /____/  _  .___/ /_/ /_/ \____/  /_/   /_/   \__,_/   \__,_/  /____/  
                       /_/                                                           
```

# DIREMAS Project

DIREMAS Project: Digital.Receipts.Management.System

## Prerequisites

- Python 3.x
- FastAPI

## Installation

1. Clone the project:

`git clone https://github.com/your-username/DIREMAS.git`

2. Navigate to the project directory:

`cd DIREMAS/`

3. Create a virtual environment:

`python3 -m venv venv`

4. Activate the virtual environment:

`source venv/bin/activate`

5. Install the dependencies:

`pip install -r requirements.txt`

6. Run the server:

`uvicorn app.main:app --reload`

7. Access the application at:

`http://127.0.0.1:8000/`


8. Access the Swagger documentation:

`http://127.0.0.1:8000/docs`

## Project Structure
```
diremas/
│
├── app/
│   ├── __init__.py         # Initialise le module app
│   ├── main.py             # Entry point for the FastAPI application
│   ├── models.py           # Defines SQLAlchemy models (Ticket, Warranty)
│   ├── schemas.py          # Defines Pydantic schemas for validation
│   ├── database.py         # Database connection and table creation
│   ├── crud.py             # CRUD operations (Create, Read, Update, Delete)
│   └── routers.py          # Router file for managing routes
│
├── .gitignore
├── README.md               # Project documentation
└── requirements.txt        # List of Python dependencies (FastAPI, SQLAlchemy, etc.)
```

## Licence
This project is licensed under the MIT License. See the LICENSE file for more details.
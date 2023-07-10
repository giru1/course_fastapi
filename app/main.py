from fastapi import FastAPI, Query
from typing import Optional
from datetime import date

from app.contractors.router import router as router_contractors

app = FastAPI()

app.include_router(router_contractors)


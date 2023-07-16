from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
import sys
import os


from app.contractors.router import router as router_contractors

app = FastAPI()

app.include_router(router_contractors)


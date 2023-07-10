from sqlalchemy import select

from app.contractors.models import Contractors
from app.dao.base import BaseDAO
from app.database import async_session_maker


class ContractorsDAO(BaseDAO):
    model = Contractors



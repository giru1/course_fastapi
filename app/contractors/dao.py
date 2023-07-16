from app.contractors.models import Contractors
from app.dao.base import BaseDAO


class ContractorsDAO(BaseDAO):
    model = Contractors

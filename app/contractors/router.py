from fastapi import APIRouter

from app.contractors.dao import ContractorsDAO


router = APIRouter(
    prefix='/contractors',
    tags=['Контрагенты']
)


@router.get('')
async def get_contractors():
    return await ContractorsDAO.get_all()

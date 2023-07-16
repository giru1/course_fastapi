from typing import List

from fastapi import APIRouter

from app.contractors.dao import ContractorsDAO
from app.contractors.schemas import ContractorsSchemas

router = APIRouter(
    prefix='/contractors',
    tags=['Контрагенты']
)


@router.get('')
async def get_contractors() -> ContractorsSchemas:
    return await ContractorsDAO.get_all()


@router.get('')
async def get_contractors() -> List[ContractorsSchemas]:
    return await ContractorsDAO.get_one_or_none()


@router.post('')
async def add_contractors(contractor) -> ContractorsSchemas:
    return await ContractorsDAO.add(**contractor)


@router.put('')
async def add_contractors(contractor) -> ContractorsSchemas:
    return await ContractorsDAO.add(**contractor)


@router.delete('')
async def add_contractors(contractor) -> ContractorsSchemas:
    return await ContractorsDAO.add(**contractor)

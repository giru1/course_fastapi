from sqlalchemy import select, insert, delete, update

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars_one_or_none()

    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, **filter_by):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()

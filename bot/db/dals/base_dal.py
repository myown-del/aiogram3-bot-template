from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession


class BaseDAL:
    """Base data access layer"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def refresh_objects(self, iterable: Iterable) -> None:
        """Refreshes given objects with new database data"""
        for x in iterable:
            await self.db_session.refresh(x)

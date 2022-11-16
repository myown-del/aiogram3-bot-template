__all__ = (
    'get_dal_controller',
    'DALController',
)

from sqlalchemy.ext.asyncio import AsyncSession

from .dal_controller import DALController


def get_dal_controller(session: AsyncSession) -> DALController:
    return DALController(
    )

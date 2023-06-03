from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class DALController:
    ...


def get_dal_controller(session: AsyncSession) -> DALController:
    return DALController(

    )

from typing import Union

import sqlalchemy
import sqlalchemy.ext.asyncio
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker


def create_sync_engine(url: Union[URL, str]) -> sqlalchemy.engine.Engine:
    """
    :param url:
    :return:
    """
    return sqlalchemy.create_engine(url=url, encoding='utf-8', pool_pre_ping=True)


def create_async_engine(url: Union[URL, str]) -> sqlalchemy.ext.asyncio.AsyncEngine:
    """
    :param url:
    :return:
    """
    return _create_async_engine(url=url, encoding='utf-8', pool_pre_ping=True)


def get_session_maker(engine: sqlalchemy.ext.asyncio.AsyncEngine) -> sessionmaker:
    """
    :param engine:
    :return:
    """
    return sessionmaker(engine, class_=sqlalchemy.ext.asyncio.AsyncSession, expire_on_commit=False)
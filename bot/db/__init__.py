__all__ = (
    'async_engine',
    'db_pool',
)

from bot.config import Config
from .connection import create_sync_engine, create_async_engine, get_session_maker

config = Config.from_env()

async_engine = create_async_engine(config.db.URL)
db_pool = get_session_maker(async_engine)

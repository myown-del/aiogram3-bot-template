from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.engine import URL


@dataclass
class DB:
    host: str
    port: int
    user: str
    password: str
    database: str

    @property
    def url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            database=self.database,
        )


@dataclass
class Config:
    bot_token: str
    db: DB

    @staticmethod
    def from_env() -> Config:
        env = Env()
        env.read_env()
        return Config(
            bot_token=env.str("BOT_TOKEN"),
            db=DB(
                host=env.str("DB_HOST"),
                port=env.int("DB_PORT"),
                user=env.str("DB_USER"),
                password=env.str("DB_PASSWORD"),
                database=env.str("DB_NAME"),
            )
        )

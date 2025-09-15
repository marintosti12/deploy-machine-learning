from __future__ import annotations
from logging.config import fileConfig
import os

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import pool

from src.config.db import Base

# Alembic Config
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def get_url() -> str:
    url = os.getenv("DATABASE_URL")
    return url

def run_migrations_offline() -> None:
    """Mode offline : pas d'engine, juste l'URL."""
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection) -> None:
    """Configuration commune (online) une fois connecté."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  
    )
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    """Mode online : engine async."""
    connectable: AsyncEngine = create_async_engine(
        get_url(),
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())

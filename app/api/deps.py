from sqlalchemy.ext.asyncio import AsyncSession

from app.configs.logging_settings import get_logger
from app.db.postgres import session_maker

logger = get_logger(__name__)


async def get_db() -> AsyncSession:
    try:
        async with session_maker() as session:
            yield session

    finally:
        await session.commit()
        await session.close()


async def get_db_transaction() -> AsyncSession:
        try:
            async with session_maker.begin() as session:
                yield session

        finally:
            await session.commit()
            await session.close()

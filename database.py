from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


engine = create_async_engine('sqlite+aiosqlite:///auction.db')
session = async_sessionmaker(engine, expire_on_commit=False)

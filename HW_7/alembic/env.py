from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from models import Base


target_metadata = Base.metadata

fileConfig(context.config.config_file_name)

config = context.config
config.set_main_option('sqlalchemy.url', 'sqlite:///school.db')
engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool)


with engine.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )


with context.begin_transaction():
    context.run_migrations()

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Ensure the app directory is on sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your Base and all models to register them with SQLAlchemy's metadata
from app.db.models import exam, grading, result
from app.db.base import Base

target_metadata = Base.metadata
from app.db.base import Base  # Base = declarative_base()

print(Base.metadata.tables.keys())


# Alembic Config object
config = context.config

# Load database URL from environment variable
db_url = os.getenv("DATABASE_URL")
if db_url:
    config.set_main_option("sqlalchemy.url", db_url)

# Interpret config file for logging
fileConfig(config.config_file_name)

# Set target metadata for 'autogenerate' support
target_metadata = Base.metadata

# Run migration in offline mode (generates SQL script)
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# Run migration in online mode (direct DB changes)
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

# Main execution entrypoint
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


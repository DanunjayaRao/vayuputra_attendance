"""Add device_pins column to users table

Revision ID: add_device_pins
Revises: 202602161200
Create Date: 2026-03-03

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON


# revision identifiers, used by Alembic.
revision: str = "add_device_pins"
down_revision: Union[str, None] = "202602161200"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _column_exists(table_name: str, column_name: str) -> bool:
    """Return True when the given column already exists."""
    inspector = sa.inspect(op.get_bind())
    return any(col["name"] == column_name for col in inspector.get_columns(table_name))


def upgrade():
    """Add device_pins JSON column to users table"""
    if not _column_exists('users', 'device_pins'):
        op.add_column('users', sa.Column('device_pins', JSON, nullable=True))


def downgrade():
    """Remove device_pins column from users table"""
    if _column_exists('users', 'device_pins'):
        op.drop_column('users', 'device_pins')

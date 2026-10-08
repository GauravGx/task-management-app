"""create tasks table

Revision ID: c59a083b891f
Revises:
Create Date: 2026-09-18 23:48:06.984386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c59a083b891f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create tasks table."""

    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("is_completed", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_index(
        op.f("ix_tasks_id"),
        "tasks",
        ["id"],
        unique=False
    )


def downgrade() -> None:
    """Drop tasks table."""

    op.drop_index(
        op.f("ix_tasks_id"),
        table_name="tasks"
    )

    op.drop_table("tasks")
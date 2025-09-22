"""ml outputs

Revision ID: 24251a13df00
Revises: ecd589af543e
Create Date: 2025-09-15 16:34:46.842373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '24251a13df00'
down_revision: Union[str, Sequence[str], None] = 'ecd589af543e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ml_outputs",
        sa.Column("id",  postgresql.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()")),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("TIMEZONE('utc', now())")),
        sa.Column("input_id",  postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("prediction", sa.String(length=100), nullable=False),
        sa.Column("prob", sa.Float(), nullable=True),
        sa.Column("error", sa.String(length=500), nullable=True),
        sa.ForeignKeyConstraint(["input_id"], ["ml_inputs.id"], ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table("ml_outputs")


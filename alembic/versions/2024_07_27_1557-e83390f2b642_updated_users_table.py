"""updated users table

Revision ID: e83390f2b642
Revises: 2e0797256e03
Create Date: 2024-07-27 15:57:19.874588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e83390f2b642'
down_revision: Union[str, None] = '2e0797256e03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=320),
               existing_nullable=False)
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'email',
               existing_type=sa.String(length=320),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=32),
               existing_nullable=False)
    # ### end Alembic commands ###

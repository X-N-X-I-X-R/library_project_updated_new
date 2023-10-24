"""Add additional_fields to Loan model

Revision ID: 08d47881085f
Revises: 
Create Date: 2023-10-24 11:13:06.766355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08d47881085f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('additional_fields', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loan', schema=None) as batch_op:
        batch_op.drop_column('additional_fields')

    # ### end Alembic commands ###

"""Add amenity and bus_amenity tables

Revision ID: 6d6ac24c7093
Revises: c19e603e923c
Create Date: 2024-09-10 01:12:23.885224

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6d6ac24c7093'
down_revision = 'c19e603e923c'
branch_labels = None
depends_on = None


def upgrade():
    # Create amenity table
    op.create_table('amenity',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), nullable=False)
    )

    # Create bus_amenity table (join table)
    op.create_table('bus_amenity',
        sa.Column('bus_id', sa.Integer, sa.ForeignKey('bus.id'), primary_key=True),
        sa.Column('amenity_id', sa.Integer, sa.ForeignKey('amenity.id'), primary_key=True)
    )

def downgrade():
    # Drop the bus_amenity table
    op.drop_table('bus_amenity')

    # Drop the amenity table
    op.drop_table('amenity')

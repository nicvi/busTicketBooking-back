"""rename columns from trip table

Revision ID: dd6dd1f373cc
Revises: 48b29b9ce3af
Create Date: 2024-09-11 00:19:16.782325

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = 'dd6dd1f373cc'
down_revision = '48b29b9ce3af'
branch_labels = None
depends_on = None


def upgrade():
    # Rename column 'departure_time' to 'start_time' in 'trip' table
    op.alter_column('trip', 'rout_id', new_column_name='route_id')
    op.alter_column('trip', 'SeatsOccupied', new_column_name='seats_occupied')

def downgrade():
    # Revert column name back to 'departure_time' in 'trip' table
    op.alter_column('trip', 'route_id', new_column_name='rout_id')
    op.alter_column('trip', 'seats_occupied', new_column_name='SeatsOccupied')

"""create initial tables

Revision ID: c19e603e923c
Revises: 
Create Date: 2024-08-29 10:30:02.088423

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'c19e603e923c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False)
    )

    op.create_table('bus',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('bus_number', sa.String(length=50), nullable=False),
    sa.Column('number_ofSeats', sa.Integer, nullable=False),
    sa.Column('amenities', sa.String, nullable=True)
    )

    op.create_table('route',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('origin_city', sa.String(length=100), nullable=False),
    sa.Column('destination_city', sa.String(length=100), nullable=False),
    sa.Column('departure_date', sa.DateTime, nullable=False)
    )

    op.create_table('trip',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('bus_id', sa.Integer, sa.ForeignKey('bus.id'), nullable=False),
    sa.Column('rout_id', sa.Integer, sa.ForeignKey('route.id'), nullable=False),
    sa.Column('SeatsOccupied', sa.Integer, nullable=False)
    )

    op.create_table('booking',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
    sa.Column('booking_date', sa.DateTime, nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('trip_id', sa.Integer, sa.ForeignKey('trip.id'), nullable=False)
    )

    op.create_table('ticket',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('booking_id', sa.Integer, sa.ForeignKey('booking.id'), nullable=False),
    sa.Column('seat_number', sa.Integer, nullable=False)
    )

    op.create_table('payment',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('booking_id', sa.Integer, sa.ForeignKey('booking.id'), nullable=False),
    sa.Column('payment_method', sa.String(length=50), nullable=False),
    sa.Column('payment_status', sa.String(length=50), nullable=False),
    sa.Column('payment_date', sa.DateTime, nullable=False)
    )

def downgrade():
    op.drop_table('payment')
    op.drop_table('ticket')
    op.drop_table('booking')
    op.drop_table('trip')
    op.drop_table('route')
    op.drop_table('bus')
    op.drop_table('user')
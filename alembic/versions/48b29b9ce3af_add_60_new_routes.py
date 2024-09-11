"""Add 60 new routes

Revision ID: 48b29b9ce3af
Revises: 47606e6f58df
Create Date: 2024-09-10 01:32:40.001394

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime, timedelta
import random


# revision identifiers, used by Alembic.
revision = '48b29b9ce3af'
down_revision = '47606e6f58df'
branch_labels = None
depends_on = None


def upgrade():
    # Define cities and dates
    cities = ['Machala', 'Guayaquil', 'Cuenca', 'Duran', 'Huaquillas', 'Arenillas',
              'Santa Rosa', 'El Guabo', 'Naranjal', 'Lima', 'Camilo Ponce Enriquez',
              'Giron', 'Yunguilla']
    departure_dates = [datetime(2024, 9, 10) + timedelta(hours=i) for i in range(12)] + \
                      [datetime(2024, 9, 11) + timedelta(hours=i) for i in range(12)]

    # Prepare 60 random routes with different origins and destinations
    routes = []
    for i in range(60):
        origin = random.choice(cities)
        destination = random.choice([city for city in cities if city != origin])
        departure_date = random.choice(departure_dates)
        routes.append({
            'origin_city': origin,
            'destination_city': destination,
            'departure_date': departure_date
        })

    # Insert into the route table
    op.bulk_insert(
        sa.table('route',
                 sa.column('origin_city', sa.String),
                 sa.column('destination_city', sa.String),
                 sa.column('departure_date', sa.DateTime),
                 ),
        routes
    )


def downgrade():
    # The downgrade would remove the 60 new routes by their departure date range
    op.execute("""
        DELETE FROM route 
        WHERE departure_date BETWEEN '2024-09-10' AND '2024-09-11'
    """)
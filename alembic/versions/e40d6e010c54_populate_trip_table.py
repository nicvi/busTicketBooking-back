"""populate trip table

Revision ID: e40d6e010c54
Revises: dd6dd1f373cc
Create Date: 2024-09-11 00:27:39.521289

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
import random

# revision identifiers, used by Alembic.
revision = 'e40d6e010c54'
down_revision = 'dd6dd1f373cc'
branch_labels = None
depends_on = None


def upgrade():
    # Populate trip table
    connection = op.get_bind()

    # Fetch all available buses
    buses = connection.execute(sa.text("SELECT id FROM bus")).fetchall()
    # Fetch all available routes
    routes = connection.execute(sa.text("SELECT id, departure_date FROM route")).fetchall()

    # Ensure routes are ordered by departure date
    routes = sorted(routes, key=lambda x: x[1])

    trip_table = table('trip',
                       column('bus_id', sa.Integer),
                       column('route_id', sa.Integer),
                       column('seats_occupied', sa.Integer)
                       )

    trip_entries = []
    bus_routes = {}

    for route in routes:
        route_id, departure_date = route

        available_buses = buses[:]
        # For each day (date), assign buses to different routes
        for i in range(min(len(available_buses), 10)):
            bus_id = available_buses.pop(0)

            # Ensure that a bus does not have the same route multiple times a day
            if bus_id in bus_routes and departure_date.date() in bus_routes[bus_id]:
                continue

            if bus_id not in bus_routes:
                bus_routes[bus_id] = []
            bus_routes[bus_id].append(departure_date.date())

            seats_occupied = random.randint(0, 50)  # Randomly assign seats occupied

            # Add trip entry
            trip_entries.append({
                'bus_id': bus_id[0],
                'route_id': route_id,
                'seats_occupied': seats_occupied
            })

    # Ensure at least 20 rows are inserted
    for i in range(10, 20):
        if len(trip_entries) < 20:
            bus_id = random.choice(buses)[0]
            route_id = random.choice(routes)[0]
            seats_occupied = random.randint(0, 50)

            trip_entries.append({
                'bus_id': bus_id,
                'route_id': route_id,
                'seats_occupied': seats_occupied
            })

    # Bulk insert into the trip table
    op.bulk_insert(trip_table, trip_entries)


def downgrade():
    # Remove populated trip entries
    op.execute("""
        DELETE FROM trip
        WHERE bus_id IS NOT NULL AND route_id IS NOT NULL
    """)

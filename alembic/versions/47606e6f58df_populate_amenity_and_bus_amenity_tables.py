"""populate amenity and bus_amenity tables

Revision ID: 47606e6f58df
Revises: 6d6ac24c7093
Create Date: 2024-09-10 01:18:11.252835

"""
import random

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import column, table

from alembic import op

# revision identifiers, used by Alembic.
revision = '47606e6f58df'
down_revision = '6d6ac24c7093'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()

    # Define amenity table for bulk insertion
    amenities_table = table('amenity',
                            column('id', sa.Integer),
                            column('name', sa.String)
                            )

    # Insert predefined amenities if they don't already exist
    existing_amenities = connection.execute(sa.text("SELECT id FROM amenity")).fetchall()
    if not existing_amenities:
        op.bulk_insert(amenities_table, [
            {'name': 'WiFi'},
            {'name': 'Media Play'},
            {'name': 'USB Charger Hubs'},
            {'name': 'Toilet'}
        ])

    # Insert 10 new buses
    buses_table = table('bus',
                        column('id', sa.Integer),
                        column('bus_number', sa.String),
                        column('number_ofSeats', sa.Integer)
                        )

    op.bulk_insert(buses_table, [
        {'bus_number': f'Bus-{i}', 'number_ofSeats': random.randint(30, 60)} for i in range(1, 11)
    ])

    # Fetch the IDs of the buses and amenities to establish relationships
    bus_ids = connection.execute(sa.text("SELECT id FROM bus ORDER BY id DESC LIMIT 10")).fetchall()
    amenity_ids = connection.execute(sa.text("SELECT id FROM amenity")).fetchall()

    # Ensure each bus has a toilet, and randomly assign other amenities
    toilet_amenity_id = connection.execute(sa.text("SELECT id FROM amenity WHERE name = 'Toilet'")).scalar()
    bus_amenity_table = table('bus_amenity',
                              column('bus_id', sa.Integer),
                              column('amenity_id', sa.Integer)
                              )

    for bus_id in bus_ids:
        # Assign the toilet amenity and other random amenities
        assigned_amenities = [toilet_amenity_id]
        other_amenities = [amenity_id[0] for amenity_id in amenity_ids if amenity_id[0] != toilet_amenity_id]
        random_amenities = random.sample(other_amenities, random.randint(1, 2))
        assigned_amenities.extend(random_amenities)

        # Insert the bus-amenity relationships into the bus_amenity table
        for amenity_id in assigned_amenities:
            connection.execute(sa.text(
                "INSERT INTO bus_amenity (bus_id, amenity_id) VALUES (:bus_id, :amenity_id)"),
                {'bus_id': bus_id[0], 'amenity_id': amenity_id}
            )


def downgrade():
    connection = op.get_bind()

    # Remove the buses and corresponding bus_amenity records
    bus_ids = connection.execute(sa.text("SELECT id FROM bus ORDER BY id DESC LIMIT 10")).fetchall()
    bus_ids_to_delete = [bus_id[0] for bus_id in bus_ids]

    op.execute(sa.text("DELETE FROM bus_amenity WHERE bus_id = ANY(:bus_ids)").bindparams(bus_ids=bus_ids_to_delete))
    op.execute(sa.text("DELETE FROM bus WHERE id = ANY(:bus_ids)").bindparams(bus_ids=bus_ids_to_delete))
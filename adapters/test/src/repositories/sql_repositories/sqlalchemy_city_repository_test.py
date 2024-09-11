import unittest
from unittest.mock import MagicMock
from adapters.src.repositories.sql_repositories import SQLAlchemyCityRepository
from factories.config.db_connection import SessionLocal


class TestSQLAlchemyCityRepository(unittest.TestCase):
    def setUp(self):
        db = SessionLocal()
        self.session = MagicMock(db)
        self.repo = SQLAlchemyCityRepository(self.session)

    def test_get_available_cities(self):
        origin_cities = [('Guayaquil',), ('Cuenca',)]
        destination_cities = [('Machala',), ('Cuenca',)]
        expected_cities = ['Guayaquil', 'Cuenca', 'Machala']

        self.session.query.return_value.all.side_effect = [origin_cities, destination_cities]
        cities = self.repo.get_available_cities()

        self.assertCountEqual(cities, expected_cities)

from unittest import TestCase, mock

from factories import config

from ..... import SQLAlchemyCityRepository


class TestSQLAlchemyCityRepository(TestCase):
    def setUp(self):
        db = config.SessionLocal()
        self.session = mock.MagicMock(db)
        self.repo = SQLAlchemyCityRepository(self.session)

    def test_get_available_cities(self):
        origin_cities = [('Guayaquil',), ('Cuenca',)]
        destination_cities = [('Machala',), ('Cuenca',)]
        expected_cities = ['Guayaquil', 'Cuenca', 'Machala']

        self.session.query.return_value.all.side_effect = [origin_cities, destination_cities]
        cities = self.repo.get_available_cities()

        self.assertCountEqual(cities, expected_cities)

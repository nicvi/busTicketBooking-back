from unittest.mock import MagicMock, patch
import core
from ... import dependencies

@patch("factories.config.get_db", return_value=MagicMock())
@patch("api.dependencies.city.repositories.SQLAlchemyCityRepository")
def test_get_cities_use_case(mock_city_repo_class, mock_get_db):
    mock_db_session = next(mock_get_db())
    mock_city_repo = mock_city_repo_class.return_value

    use_case = dependencies.get_cities_use_case()

    assert mock_get_db.call_count == 2
    mock_city_repo_class.assert_called_with(session=mock_db_session)
    assert isinstance(use_case, core.GetCities)
    assert use_case.city_repository == mock_city_repo

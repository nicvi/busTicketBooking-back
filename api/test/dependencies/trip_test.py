from unittest.mock import MagicMock, patch

import core

from ... import dependencies


@patch("factories.config.get_db", return_value=MagicMock())
@patch("api.dependencies.trip.repositories.SQLAlchemyTripRepository")
def test_get_view_available_trips_use_case(mock_trip_repo_class, mock_get_db):
    mock_db_session = next(mock_get_db())
    mock_trip_repo = mock_trip_repo_class.return_value

    use_case = dependencies.get_view_available_trips_use_case()

    assert mock_get_db.call_count == 2
    mock_trip_repo_class.assert_called_with(session=mock_db_session)
    assert isinstance(use_case, core.GetAvailableTrips)
    assert use_case.trip_repository == mock_trip_repo

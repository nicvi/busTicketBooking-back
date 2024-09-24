from unittest.mock import MagicMock, patch
import core
from ... import dependencies


@patch("factories.config.get_db", return_value=MagicMock())
@patch("api.dependencies.booking.repositories.SQLAlchemyBookingRepository")
def test_get_booking_by_id_use_case(mock_booking_repo_class, mock_get_db):
    mock_db_session = next(mock_get_db())
    mock_booking_repo = mock_booking_repo_class.return_value

    use_case = dependencies.get_booking_by_id_use_case()

    assert mock_get_db.call_count == 2
    mock_booking_repo_class.assert_called_with(session=mock_db_session)
    assert isinstance(use_case, core.GetBookingById)
    assert use_case.booking_repository == mock_booking_repo

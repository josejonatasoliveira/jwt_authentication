from app.config.database import get_db


def test_database_connection(mocker):
    # GIVEN
    mock_session = mocker.patch('app.config.database.SessionLocal')

    # WHEN
    db = next(get_db())

    # THEN
    assert db == mock_session()

import pytest

from app import utils
from app.db import SessionLocal, Base, engine


@pytest.fixture(scope='function')
def test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def create_db_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def test_calculate_md5_succeeds():
    string = 'test'
    md5_string = '098f6bcd4621d373cade4e832627b4f6'
    assert utils.calculate_md5_hash(string) == md5_string

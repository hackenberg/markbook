import pytest

import markbook
import markbook.config


@pytest.fixture
def session(request, scope="module"):
    markbook.app.config.from_object("markbook.config.TestingConfig")
    session = markbook.app.test_client()
    db = markbook.db
    db.create_all()

    def finalizer():
        db.session.remove()
        db.drop_all()

    request.addfinalizer(finalizer)
    return session


@pytest.fixture
def app(scope="module"):
    return markbook.app


@pytest.fixture
def db(scope="module"):
    return markbook.db

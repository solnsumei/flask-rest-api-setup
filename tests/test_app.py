import os
import tempfile

import pytest
from main import create_app


@pytest.fixture
def client():
    test_app = create_app()
    db_fd, test_app.config['DATABASE'] = tempfile.mkstemp()

    test_app.config['TESTING'] = True

    client = test_app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(test_app.config['DATABASE'])

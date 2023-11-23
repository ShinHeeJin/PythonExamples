import os
import tempfile

import pytest


@pytest.fixture
def cleandir():
    with tempfile.TemporaryDirectory() as new_path:
        old_cwd = os.getcwd()
        os.chdir(new_path)
        yield
        os.chdir(old_cwd)

import os

import pytest

# https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#use-fixtures-in-classes-and-modules-with-usefixtures


@pytest.mark.usefixtures("cleandir")
def test_directory_init():
    assert os.listdir(os.getcwd()) == []
    with open("myfile", "w") as f:
        f.write("test")


@pytest.mark.usefixtures("cleandir")
def test_directory_init2():
    assert os.listdir(os.getcwd()) == []

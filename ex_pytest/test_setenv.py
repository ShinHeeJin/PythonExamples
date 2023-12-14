import os

import pytest

# https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#use-fixtures-in-classes-and-modules-with-usefixtures


@pytest.mark.usefixtures("cleandir")
def test_directory_init():
    """
    cleandir fixture 내부 임시 디렉토리에서 myfile가 생성되고 삭제됨
    """
    assert os.listdir(os.getcwd()) == []
    with open("myfile", "w") as f:
        f.write("test")


@pytest.mark.usefixtures("cleandir")
def test_directory_init2():
    """
    여전히 프로젝트 디렉토리에는 아무 파일도 존재하지 않음
    """
    assert os.listdir(os.getcwd()) == []

import os
from pathlib import Path

print(Path(__file__).parent / "test.txt")  # /Users/heej/envs/python-ex/ex_filesystem/test.txt
print(Path(__file__).parent)  # /Users/heej/envs/python-ex/ex_filesystem
print(Path(__file__))  # /Users/heej/envs/python-ex/ex_filesystem/pathlib_basic.py
print(Path.cwd())  # /Users/heej/envs/python-ex/ex_filesystem
print(Path.home())  # /Users/heej

# 파일 생성
path = Path("test.txt")
path.touch()
if os.path.isfile(path):
    os.remove(path)

# 이름 변경
path = Path("test.txt")
path.touch()
path.rename("test2.txt")
os.remove("test2.txt")

# 속성
path = Path("/Users/heej/Projects/python-ex/.pytest.ini")
print(f"stem : {path.stem}")  # .pytest
print(f"name : {path.name}")  # .pytest.ini
print(f"suffix : {path.suffix}")  # .ini
print(f"anchor : {path.anchor}")  # /
print(f"suffixes : {path.suffixes}")  # ['.ini']

# glob
basedir = os.path.abspath(os.path.dirname(__file__))  # /Users/heej/Projects/python-ex
path = Path(basedir)
assert list(path.glob("**/*.py")) == list(path.rglob("*.py"))

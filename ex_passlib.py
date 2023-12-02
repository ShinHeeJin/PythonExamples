from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "test1234!"
a = pwd_context.hash(password)
b = pwd_context.hash(password)
assert a != b

hashed_pwd = pwd_context.hash(password)
assert pwd_context.verify("test1234!", hashed_pwd)

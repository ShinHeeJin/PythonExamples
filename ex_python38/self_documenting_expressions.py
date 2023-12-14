# f-string에서 평가식(self-documenting-expressions)을 위한 =기호 추가

name = "test"
print(f"name = {name}")  # name = test
print(f"{name = }")  # name = 'test'

pi = 3.141592
print(f"{pi = :.3f}")  # pi = 3.142

number = 30000
print(f"{number = :,d}")  # pi = 30,000

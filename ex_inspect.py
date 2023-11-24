from inspect import signature

# 1. signature


def myfunc(a: int = 1, b: float = 2) -> int:
    return a + int(b)


signature = signature(myfunc)
print(signature.parameters)  # OrderedDict([('a', <Parameter "a: int = 1">), ('b', <Parameter "b: float = 2">)])

assert "a" in signature.parameters
assert "b" in signature.parameters
assert "c" not in signature.parameters

assert signature.return_annotation == int
assert signature.parameters.get("a").default == 1
signature.parameters.get("a").annotation == int
signature.parameters.get("b").annotation == float

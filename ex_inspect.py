from inspect import signature

# 1. signature


def myfunc(a: int = 1, b: float = 2) -> int:
    return a + int(b)


sig = signature(myfunc)
print(sig.parameters)  # OrderedDict([('a', <Parameter "a: int = 1">), ('b', <Parameter "b: float = 2">)])

assert "a" in sig.parameters
assert "b" in sig.parameters
assert "c" not in sig.parameters

assert sig.return_annotation == int
assert sig.parameters.get("a").default == 1
sig.parameters.get("a").annotation == int
sig.parameters.get("b").annotation == float

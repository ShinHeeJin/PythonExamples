from itertools import pairwise

for a, b in pairwise([1, 2, 3, 4, 5]):
    print(a, b)

# 1 2
# 2 3
# 3 4
# 4 5

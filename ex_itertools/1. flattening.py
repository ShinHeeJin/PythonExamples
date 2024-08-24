from itertools import chain

# fmt: off
# 3차원 배열 flattening

three_d_array = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

flattened = list(
    chain(
        *chain(*three_d_array)
    )
)

print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8]

two_d_array = [
    [1, 2, 3],
    [4, 5, 6]
]

flattened = list(
    chain(*two_d_array)
)
print(flattened) # [1, 2, 3, 4, 5, 6]

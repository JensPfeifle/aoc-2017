from math import modf
from typing import List

# part 1
def checksum(rows):
    checksum = 0
    for row in rows:
        numbers = list(map(int, row.split()))
        delta = max(numbers) - min(numbers)
        checksum += delta
    return checksum


# part 2
def find_evens(rows: List[str]) -> int:
    total = 0
    for row in rows:
        numbers = list(map(int, row.split()))
        # no need to check if smaller/larger is integer..
        numbers = sorted(numbers)
        result = 0
        for idx, i in enumerate(numbers):
            for j in numbers[idx + 1 :]:
                frac, int_ = modf(j / i)
                if frac == 0.0:
                    result = int(int_)
                    break
            if result:
                total += result
                result = 0
                continue
    return total


example = """
5 1 9 5
7 5 3
2 4 6 8
"""
print(checksum(example.strip().splitlines()))

with open("2.in") as f:
    print(checksum(f.read().strip().splitlines()))

example = """
5 9 2 8
9 4 7 3
3 8 6 5
"""
print(find_evens(example.strip().splitlines()))
with open("2.in") as f:
    print(find_evens(f.read().strip().splitlines()))

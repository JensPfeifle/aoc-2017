import itertools


def part1(inpt: str) -> int:
    total = 0
    prev = -1
    for d in inpt + inpt[0]:
        if int(d) == prev:
            total += prev
        prev = int(d)
    return total


def part2(inpt: str) -> int:
    total = 0
    num_items = len(inpt)
    for idx, d in enumerate(inpt):
        halfway_idx = idx + num_items // 2
        if halfway_idx >= num_items:
            halfway_idx -= num_items
        if d == inpt[halfway_idx]:
            total += int(d)
    return total


examples = ["1122", "1111", "1234", "91212129"]
for inpt in examples:
    total = part1(inpt)
    print(f"{inpt} -> {total}")

with open("1.in") as f:
    total = part1(f.read().strip())
    print("part1: ", total)

examples = ["1212", "1221", "123425", "123123", "12131415"]
for inpt in examples:
    total = part2(inpt)
    print(f"{inpt} -> {total}")

with open("1.in") as f:
    total = part2(f.read().strip())
    print("part2: ", total)

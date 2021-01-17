import itertools


def part1(passphrase: str):
    return len(passphrase.split()) == len(set(passphrase.split()))


def part2(passphrase: str):
    return all(
        set(a) != set(b) for a, b in itertools.combinations(passphrase.split(), 2)
    )


with open("4.in") as f:
    passphrases = f.read().strip().splitlines()

print("part1:", sum(map(part1, passphrases)))
print("part2:", sum(map(part2, passphrases)))

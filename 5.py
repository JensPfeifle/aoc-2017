with open("5.in") as f:
    offsets = [int(o) for o in f.read().strip().splitlines()]

pc = 0
steps = 0
while 0 <= pc < len(offsets):
    offset = offsets[pc]
    if offset >= 3:
        offsets[pc] -= 1
    else:
        offsets[pc] += 1
    pc = pc + offset
    steps +=1

print(steps)


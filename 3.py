import math
from typing import Dict, Tuple

Coords = Tuple[int, int]  # center = (0,0)

inpt = int(open("3.in").read().strip())


def above(square: Coords) -> Coords:
    x, y = square
    return (x, y - 1)


def below(square: Coords) -> Coords:
    x, y = square
    return (x, y + 1)


def right_of(square: Coords) -> Coords:
    x, y = square
    return (x + 1, y)


def left_of(square: Coords) -> Coords:
    x, y = square
    return (x - 1, y)


def prev_square(position: Coords, grid_size: int) -> Coords:
    assert grid_size % 2 == 1
    max_r = (grid_size - 1) // 2

    if position == (0, 0):
        # no prev for 0,0
        raise ValueError

    # check corners first...
    if position == (max_r, max_r):
        # bottom right
        return left_of(position)
    elif position == (-max_r, max_r):
        # bottom left
        return above(position)
    elif position == (-max_r, -max_r):
        # top left corner
        return right_of(position)
    elif position == (max_r, -max_r):
        # top right
        return below(position)

    # now try sides...
    if position[1] == max_r:
        # bottom row
        return left_of(position)
    elif position[0] == -max_r:
        # left side
        return above(position)
    elif position[1] == -max_r:
        # top row
        return right_of(position)
    elif position[0] == max_r:
        # right side
        return below(position)

    raise Exception


def next_square(position: Coords, grid_size: int) -> Coords:
    assert grid_size % 2 == 1
    max_r = (grid_size - 1) // 2

    if position == (0, 0):
        return (1, 0)

    # check corners first...
    if position == (max_r, max_r):
        # bottom right
        return above(position)
    elif position == (-max_r, max_r):
        # bottom left
        return right_of(position)
    elif position == (-max_r, -max_r):
        # top left corner
        return below(position)
    elif position == (max_r, -max_r):
        # top right
        return left_of(position)

    # now try sides...
    if position[1] == max_r:
        # bottom row
        return right_of(position)
    elif position[0] == -max_r:
        # left side
        return below(position)
    elif position[1] == -max_r:
        # top row
        return left_of(position)
    elif position[0] == max_r:
        # right side
        return above(position)

    raise Exception


def part1(inpt):
    print("part1:")
    grid_size = int(math.ceil(math.sqrt(inpt)))
    if grid_size % 2 == 0:
        grid_size += 1
    print(f"  grid containing {inpt} is {grid_size} x {grid_size}")
    layer_start = ((grid_size - 2) ** 2) + 1
    print(f"  outer layer contains {layer_start} to {grid_size **2}")

    number = grid_size ** 2
    # start at bottom right in outer layer, walk backwards to the number to find position
    position = [(grid_size - 1) // 2, (grid_size - 1) // 2]
    while number > inpt:
        position = prev_square(position, grid_size)
        number -= 1
    print(f"  {number} is at {position}")
    print(f"  manhattan distance to '1' is {abs(position[0]) + abs(position[1])}")


def sum_neighbors(grid: Dict[Coords, int], point: Coords) -> int:
    total = 0
    for x in (point[0] - 1, point[0], point[0] + 1):
        for y in (point[1] - 1, point[1], point[1] + 1):
            if (x, y) in grid:
                total += grid[(x, y)]
    return total


def part2(inpt):
    grid = {(0, 0): 1}
    grid_size = 3
    bottom_right = (1, 1)
    x, y = (0, 0)
    while grid[(x, y)] <= inpt:
        x, y = next_square((x, y), grid_size)
        grid[(x, y)] = sum_neighbors(grid, (x, y))
        if (x, y) == bottom_right:
            x, y = right_of(bottom_right)
            grid[(x, y)] = sum_neighbors(grid, (x, y))
            grid_size += 2
            bottom_right = ((grid_size - 1) // 2, (grid_size - 1) // 2)
    print(f"part2: {grid[(x,y)]}")


if __name__ == "__main__":
    part1(inpt)
    part2(inpt)

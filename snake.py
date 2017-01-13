import numpy as np


def kernel(l):
    mod = l[0] % 4
    mod_array = [(a - mod + 4) % 4 for a in l]
    rotated = [rotate_list(mod_array, n) for n in range(0, len(l))]
    rotated.sort()
    return rotated[0]


def rotate_list(l, n):
    return l[-n:] + l[:-n]


rotation_matrix = np.matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
reflection_matrix = np.matrix([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
sequence = [rotation_matrix, reflection_matrix] * 2


def add(o, l, d):
    o.add((tuple(l.tolist()), tuple(d.tolist())),)
    return o


def step_path(occupied, location, direction, turn):
    transform = reduce(lambda x, y: x * y, sequence[0:turn])
    new_direction = (direction * transform).A1
    side_direction1 = np.cross(new_direction, direction)
    side_direction2 = (side_direction1 * reflection_matrix).A1

    next_location = location + new_direction
    next_direction = (new_direction * reflection_matrix).A1

    new_occupied = add(occupied, location, direction)
    new_occupied = add(new_occupied, location, new_direction)
    new_occupied = add(new_occupied, location, side_direction1)
    new_occupied = add(new_occupied, location, side_direction2)

    return new_occupied, next_location, next_direction
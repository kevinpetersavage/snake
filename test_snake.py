from nose.tools import assert_equal
from snake import kernel, step_path
import numpy as np


def test_kernel_reduces_so_first_is_0():
    assert_equal(kernel([2,2,3,3]), [0,0,1,1])


def test_kernel_reduces_by_rotation():
    assert_equal(kernel([0,3,0,2]), [0,2,0,3])


def test_step_path():
    location = np.array([0,0,0])
    direction = np.array([0,0,1])
    occupied = set()

    new_occupied, new_location, new_direction = step_path(occupied, location, direction, 3)

    expected_occupied = {
        ((0, 0, 0), (0, 0, 1)),
        ((0, 0, 0), (0, 1, 0)),
        ((0, 0, 0), (-1, 0, 0)),
        ((0, 0, 0), (0, -1, 0))
    }
    assert_equal(new_occupied, expected_occupied)
    assert_equal(new_location.tolist(), [-1, 0, 0])
    assert_equal(new_direction.tolist(), [1, 0, 0])

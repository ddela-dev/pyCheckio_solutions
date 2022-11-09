from typing import Tuple
import math


def dis(p1, p2):
    return math.sqrt(math.pow((p1[0] - p2[0]), 2) + math.pow((p1[1] - p2[1]), 2))  # (ax || ay) && (bx || by)


def sec(p0, p1, p2):
    return ((p1[1] > p0[1]) != (p2[1] > p0[1])) and (
                p0[0] < (p2[0] - p1[0]) * (p0[1] - p1[1]) / (p2[1] - p1[1]) + p1[0])


def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    # if touches a corner
    for p in polygon:
        if p == point:
            return True

    # if touches a border
    if dis(polygon[0], point) + dis(point, polygon[len(polygon) - 1]) == dis(polygon[0], polygon[len(polygon) - 1]):
        return True
    for i in range(len(polygon) - 1):
        if dis(polygon[i], point) + dis(point, polygon[i + 1]) == dis(polygon[i], polygon[i + 1]):
            return True

    # if is inside
    inside = sec(point, polygon[0], polygon[len(polygon) - 1])
    for i in range(len(polygon) - 1):
        if sec(point, polygon[i], polygon[i + 1]):
            inside = not inside

    return inside


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) is False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) is True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) is False, "Eighth"
    print("All done! Let's check now")

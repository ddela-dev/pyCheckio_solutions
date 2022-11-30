import math


def get_dis(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def get_corners(p):
    return [(p[0], p[1]), (p[0] + 1, p[1]), (p[0], p[1] + 1), (p[0] + 1, p[1] + 1)]


def corners_inside(radius, corners):
    inside = 0
    for c in corners:
        if get_dis([0, 0], c) <= radius:
            inside += 1
    return inside


def checkio(radius):
    box_radius = math.ceil(radius)
    tiles = []
    for x in range(box_radius):
        for y in range(box_radius):
            tiles.append(get_corners([x, y]))

    solid = 0
    partial = 0
    for t in tiles:
        if corners_inside(radius, t) == 4:
            solid += 1
            continue
        if corners_inside(radius, t) != 0:
            partial += 1
            continue

    return [solid * 4, partial * 4]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"

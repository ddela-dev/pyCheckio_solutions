import math


def get_dis(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def get_corners(p):
    return sorted([[p[0], p[1]], [p[0] + 1, p[1]], [p[0], p[1] + 1], [p[0] + 1, p[1] + 1]])


def corners_inside(circle, corners):
    inside = 0
    for c in corners: inside += 1 if get_dis(circle, c) <= circle[2] else 0
    return inside


def get_tiles(circles):
    tiles = []
    for c in circles:
        box_radius = math.ceil(c[2])
        for x in range(c[0] - box_radius, c[0] + box_radius):
            for y in range(c[1] - box_radius, c[1] + box_radius):
                if get_corners([x, y]) not in tiles:
                    tiles.append(get_corners([x, y]))
    return tiles


def checkio(circles):
    solid = 0
    partial = 0
    tiles = get_tiles(circles)

    checked_tiles = []
    for t in tiles:
        if t not in checked_tiles:
            real = 0
            for c in circles:
                real = max(real, corners_inside(c, t))
            if real == 4:
                solid += 1
                checked_tiles.append(t)
            elif real != 0:
                partial += 1
                checked_tiles.append(t)

    ret = [solid, partial]
    print(ret)
    return ret


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 2], [0, 4, 2]]) == [8, 24], "N=2, N=2"
    assert checkio([[0, 0, 3], [2, -2, 2]]) == [19, 24], "N=3, N=2"
    assert checkio([[0, 0, 2.5]]) == [12, 20], "N=2.5"
    assert checkio([[0, 0, 2], [3, 0, 2]]) == [10, 18], "N=2, N=2 (2)"

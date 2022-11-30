import math


def get_dis(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)


def get_corners(p,s=1):
    corners=[]
    corners.append((p[0], p[1], p[2]))              #000
    corners.append((p[0], p[1], p[2] + s))          #001
    corners.append((p[0], p[1] + s, p[2]))          #010
    corners.append((p[0], p[1] + s, p[2] + s))      #011
    corners.append((p[0] + s, p[1], p[2]))          #100
    corners.append((p[0] + s, p[1], p[2] + s))      #101
    corners.append((p[0] + s, p[1] + s, p[2]))      #110
    corners.append((p[0] + s, p[1] + s, p[2] + s))  #111
    return corners


def corners_inside(radius, corners):
    inside = 0
    for c in corners:
        if get_dis([0, 0, 0], c) <= radius:
            inside += 1
    return inside


def checkio(radius):
    box_radius = math.ceil(radius)
    tiles = []
    for x in range(box_radius):
        for y in range(box_radius):
            for z in range(box_radius):
                tiles.append(get_corners([x, y, z]))

    solid = 0
    partial = 0
    for t in tiles:
        if corners_inside(radius, t) == 8:
            solid += 1
            continue
        if corners_inside(radius, t) != 0:
            partial += 1
            continue

    ret = [solid * 8, partial * 8]
    print(ret)
    return ret


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [8, 56], "N=2"
    assert checkio(3) == [56, 152], "N=3"
    assert checkio(2.1) == [8, 80], "N=2.1"
    assert checkio(2.5) == [32, 128], "N=2.5"

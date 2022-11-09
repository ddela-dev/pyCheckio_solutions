from typing import List, Tuple
import math
Coords = List[Tuple[int, int]]
Point = Tuple[int, int]

def dis(p1: Point, p2: Point) -> float:
    # d=√ ((x 2 – x 1)² + (y 2 – y 1)²)
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def similar_triangles(c1: Coords, c2: Coords) -> bool:
    # (AB)2/(DE)2 = (BC)2/(EF)2 = (AC)2/(DF)2
    return (dis(c1[0],c1[1])/dis(c2[0],c2[1]) == dis(c1[1],c1[2])/dis(c2[1],c2[2]) == dis(c1[0],c1[2])/dis(c2[0],c2[2])) or (dis(c1[0],c1[1])/dis(c2[0],c2[2]) == dis(c1[1],c1[2])/dis(c2[2],c2[1]) == dis(c1[0],c1[2])/dis(c2[0],c2[1])) or (dis(c1[0],c1[1])/dis(c2[1],c2[0]) == dis(c1[1],c1[2])/dis(c2[0],c2[2]) == dis(c1[0],c1[2])/dis(c2[1],c2[2])) or (dis(c1[0],c1[1])/dis(c2[1],c2[2]) == dis(c1[1],c1[2])/dis(c2[2],c2[0]) == dis(c1[0],c1[2])/dis(c2[1],c2[0])) or (dis(c1[0],c1[1])/dis(c2[2],c2[0]) == dis(c1[1],c1[2])/dis(c2[0],c2[1]) == dis(c1[0],c1[2])/dis(c2[2],c2[1])) or (dis(c1[0],c1[1])/dis(c2[2],c2[1]) == dis(c1[1],c1[2])/dis(c2[1],c2[0]) == dis(c1[0],c1[2])/dis(c2[2],c2[0]))


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(1, 3), (4, 2), (2, 1)], [(2, -2), (0, -3), (-1, -1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")

def get_corners(sqr):
    bl=[sqr[0],sqr[1]]
    tr=[sqr[0]+sqr[2],sqr[1]+sqr[2]]
    return [bl,tr]

def is_inside(corners,point):
    return (corners[0][0] <= point[0] <= corners[1][0]) and (corners[0][1] <= point[1] <= corners[1][1])

def squares_intersect(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    s1corners=get_corners(s1)
    s2corners=get_corners(s2)
    for c in s1corners:
        if is_inside(s2corners,c):
            return True
    for c in s2corners:
        if is_inside(s1corners,c):
            return True
    return False


print("Example:")
print(squares_intersect((2, 2, 3), (5, 5, 2)))

assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

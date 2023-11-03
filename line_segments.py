def is_degenerated(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2 and y1 == y2:
        return True
    else:
        return False


def is_vertical(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2 and y1 != y2:
        return True
    else:
        return False


def is_horizontal(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    if x1 != x2 and y1 == y2:
        return True
    else:
        return False


def is_inclined(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    if x1 != x2 and y1 != y2:
        return True
    else:
        return False


print(is_degenerated((3, 5), (3, 6)))
print(is_vertical((3, 5), (3, 6)))
print(is_horizontal((3, 5), (3, 6)))
print(is_inclined((3, 5), (3, 6)))


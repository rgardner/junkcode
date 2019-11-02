import collections
import random

Point = collections.namedtuple('Point', ['x', 'y'])


def main():
    circle = [Point(*p) for p in ((2, 0), (0, 2), (-2, 0), (0, -2))]
    assert(poly_contains(circle, Point(0, 0)))
    assert(poly_contains(circle, Point(1, 0)))
    assert(not poly_contains(circle, Point(2, 2)))
    assert(not poly_contains(circle, Point(2, 1)))

    square = [Point(*p) for p in ((2, 2), (-2, 2), (-2, -2), (2, -2))]
    assert(poly_contains(square, Point(1, 1)))
    assert(poly_contains(square, Point(2, 2)))
    assert(not poly_contains(square, Point(3, 0)))
    assert(not poly_contains(square, Point(2, 1)))


def poly_contains(polygon, point):
    return True


if __name__ == '__main__':
    main()

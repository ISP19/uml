#
# Draw a UML class diagram based on this code.
# Show classes, attributes, and methods and
# relationships between classes such as inheritance,
# association, and dependency.
# Use correct UML notation, show multiplicity where it makes sense.


class Point:
    """Class represents a point in cartesian coordinates"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class polygon:
    def __init__(self, vertices):
        """Initialize a polygon with ordered list of vertices."""
        self.points = vertices

    def area(self) -> float:
        """compute the area of polygon"""
        # code omitted
        return 0

    def contains(self, point: Point) -> bool:
        """test if Polygon contains a given point"""
        # code omitted
        # Count how many times a horizontal ray from point
        # intersects an edge of the polygon.
        # If its odd then point is inside the polygon
        # If its even then point is outside the polygon
        return False

    @staticmethod
    def _intersects(pt: Point, e1: Point, e2: Point):
        """Return the x-coordinate of place where a horizontal ray
           drawn from Point pt interests the line defined by [e1,e2].

           If no intersection then return None.
        """
        pt_x = pt.x

        # special case: [e1,e2] define a horizontal line
        if e1.y == e2.y:
            if pt.y != e1.y:
                return None
            # they all lie on same line
            if pt_x == e1.x:
                return pt
            if pt_x > e1.x:
                if pt_x < e1.x:
                    return pt
                else:
                    return None
            # must be pt_x < e1.x
            if pt_x > e2.x:
                return pt
            return None
        # e1 and e2 are not on a horizontal line,
        # so a horizontal ray from pt must intersect somewhere
        # TODO complete this
        return None


class Rectangle(polygon):
    def __init__(self, x, y, width, height):
        self.width, self.height = width, height
        p_1 = Point(x, y)
        p_2 = Point(x+width, y)
        p_3 = Point(x+width, y+height)
        p_4 = Point(x, y+height)
        super().__init__([p_1, p_2, p_3, p_4])

    # more efficient computation of area than done in Polygon
    def area(self) -> float:
        """Return the area of this rectangle"""
        return abs(self.width * self.height)

#
# Draw a UML class diagram based on this code.
# Show classes, attributes, and methods and
# relationships between classes such as inheritance,
# association, and dependency.
# Use correct UML notation, show multiplicity where it makes sense.
#
class Point:
    """Class represents a point in cartesian coordinates"""
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self, verticies): 
        """Initialize a polygon with ordered list of verticies."""
        self.points = verticies   

    def area(self) -> float:
        """compute the area of polygon"""
        # code omitted
        return 0

    def contains(self, point: Point) -> bool:
        """test if Polygon contains a given point"""
        # code omitted
        return False

class Rectangle(Polygon):
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
    

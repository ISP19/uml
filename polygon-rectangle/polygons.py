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
	def __init__(self, verticies): # verticies is a list of Points
		self.points = verticies   

	def area(self) -> float:
		"""compute area of polygon"""
		# code omitted
		return 0

	def contains(self, point: Point) -> bool:
		"""test if Polygon contains a given point"""
		# code omitted
		return False

class Rectangle(Polygon):
	def __init__(self, x, y, width, height):
		self.width, self.height = width, height
		p1 = Point(x,y)
		p2 = Point(x+width,y)
		p3 = Point(x+width,y+height)
		p4 = Point(x,y+height)
		super().__init__([p1, p2, p3, p4])

	# more efficient computation of area than done in Polygon
	def area(self) -> float:
		return abs( self.width * self.height )
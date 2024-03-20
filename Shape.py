import math
class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."

    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def set_x(self, x: float):
        self._x = x
    def set_y(self, y: float):
        self._y = y
    
    def compute_distance(self, point) -> float:
        distance = ((self._x - point._x)**2 +(self._y - point._y)**2 )**0.5
        return distance

    
class Line:
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._length = start.compute_distance(end)

    def get_start(self):
        return self._start
    def get_end(self):
        return self._end
    def get_length(self):
        return self._length
    
    def set_start(self, start: Point):
        self._start = start
    def set_end(self, end: Point):
        self._end = end

    


    def compute_length(self):
        return self._start.compute_distance(self._end)

        
class Shape:
    def __init__(self) -> None:
        self.__is_regular = False
        self.__vertices = [Point]
        self.__edges = [Line]
        self.__inner_angles = [float]
    

    def get_vertices(self):
        return self.__vertices
    def get_edges(self):
        return self.__edges
    def get_inner_angles(self):
        return self.__inner_angles
    def get_is_regular(self):
        return self.__is_regular
    
    def set_vertices(self, vertices: list):
        self.__vertices = vertices
    def set_edges(self, edges):
        self.__edges = edges
    def set_inner_angles(self, inner_angles):
        self.__inner_angles = inner_angles
    def set_is_regular(self, is_regular: bool):
        self.__is_regular = is_regular


    def compute_area(self):
        raise NotImplementedError("Subclass should implement compute_area()")
    
    def compute_perimeter(self):
        raise NotImplementedError("Subclass should implemen compute_perimeter()")
    
    def compute_inner_angles(self):
        raise NotImplementedError("Subclass should implemen compute_inner+angles()")
    
class Triangle(Shape):
    def compute_area(self):
        #Heron's formula is used
        edge_a = self.get_edges()[0].get_length()
        edge_b = self.get_edges()[1].get_length()
        edge_c = self.get_edges()[2].get_length()

        
        semiperimeter = (edge_a + edge_b + edge_c)/2 #semiperimeter
        return math.sqrt(semiperimeter * (semiperimeter - edge_a) * (semiperimeter - edge_b)* (semiperimeter -edge_c))
    
    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self.get_edges())
    
    def compute_inner_angles(self):
        edge_a = self.get_edges()[0].get_length()
        edge_b = self.get_edges()[1].get_length()
        edge_c = self.get_edges()[2].get_length()

        angle_A = math.degrees(math.acos((edge_b**2 + edge_c**2 - edge_a**2)/(2 * edge_b * edge_c)))     
        angle_B = math.degrees(math.acos((edge_c**2 + edge_a**2 - edge_b **2)/(2 * edge_c * edge_a)))
        angle_C = 180 - angle_A - angle_B
        
        self.set_inner_angles([angle_A, angle_B, angle_C])
    
class Isosceles(Triangle):
    pass

class Equilateral(Triangle):
    pass

class Scalene(Triangle):
    pass

class TriRectangle(Triangle):
    pass

class Rectangle(Shape):
    def compute_area(self):
        return self.get_edges[0].get_length * self.get_edges[1].get_length
    def compute_perimeter(self):
        return 2*(self.get_edges[0].get_length + self.get_edges[1].get_length)
    
class Square(Rectangle):
    pass



def main():
    point_1 = Point(0,0)
    point_2 = Point(3,0)
    point_3 = Point(0,4)

    line_1 = Line(point_1, point_2)
    line_2 = Line(point_2, point_3)
    line_3 = Line(point_3, point_1)

    triangle = Scalene()
    triangle.set_vertices([point_1, point_2, point_3])
    triangle.set_edges([line_1, line_2, line_3])

    triangle.compute_inner_angles()

    print("Triangle vertices:")
    for vertex in triangle.get_vertices():
        print("({}, {})".format(vertex.get_x , vertex.get_y))

    print("Triangle Edge lengths:")
    for edge in triangle.get_edges():
        print(edge.get_length())

    print("Triangle inner angles:")
    for angle in triangle.get_inner_angles():
        print(angle)

    print("Triangle Area:", triangle.compute_area())
    print("Triangle Perimeter:", triangle.compute_perimeter())


if __name__ == "__main__":
    main()
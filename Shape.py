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
        return round(math.sqrt(semiperimeter * (semiperimeter - edge_a) * (semiperimeter - edge_b)* (semiperimeter -edge_c)),2)
    
    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self.get_edges())
    
    def compute_inner_angles(self):
        edge_a = self.get_edges()[0].get_length()
        edge_b = self.get_edges()[1].get_length()
        edge_c = self.get_edges()[2].get_length()

        angle_A = math.degrees(math.acos((edge_b**2 + edge_c**2 - edge_a**2)/(2 * edge_b * edge_c)))     
        angle_B = math.degrees(math.acos((edge_c**2 + edge_a**2 - edge_b **2)/(2 * edge_c * edge_a)))
        angle_C = 180 - angle_A - angle_B
        
        self.set_inner_angles([(angle_A), (angle_B), (angle_C)])
    
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
        return self.get_edges()[0].get_length() * self.get_edges()[1].get_length()
    def compute_perimeter(self):
        return 2*(self.get_edges()[0].get_length() + self.get_edges()[1].get_length())
    def compute_inner_angles(self):
        self.set_inner_angles([90,90,90,90])
    
class Square(Rectangle):

    pass



def main():
    
    point_1 = Point(0, 0)
    point_2 = Point(3, 0)
    point_3 = Point(0, 4)

    
    line_1 = Line(point_1, point_2)
    line_2 = Line(point_2, point_3)
    line_3 = Line(point_3, point_1)

    # Crear un triángulo escaleno
    triangle_scalene = Scalene()
    triangle_scalene.set_vertices([point_1, point_2, point_3])
    triangle_scalene.set_edges([line_1, line_2, line_3])
    triangle_scalene.compute_inner_angles()

    # Crear un triángulo isósceles
    point_4 = Point(3, 4) 
    line_4 = Line(point_2, point_4) 
    triangle_isosceles = Isosceles()
    triangle_isosceles.set_vertices([point_1, point_2, point_4])  
    triangle_isosceles.set_edges([line_1, line_4, line_3])  
    triangle_isosceles.compute_inner_angles()

    # Crear triangulo equilatero
    point_1_equilateral = Point(-1, 0)
    point_2_equilateral = Point(1, 0)
    point_3_equilateral = Point(0, math.sqrt(3))  # Altura calculada

    
    line_1_equilateral = Line(point_1_equilateral, point_2_equilateral)
    line_2_equilateral = Line(point_2_equilateral, point_3_equilateral)
    line_3_equlateral = Line(point_3_equilateral, point_1_equilateral)

    
    equilateral_triangle = Equilateral()
    equilateral_triangle.set_vertices([point_1_equilateral, point_2_equilateral, point_3_equilateral])
    equilateral_triangle.set_edges([line_1_equilateral, line_2_equilateral, line_3_equlateral])
    equilateral_triangle.compute_inner_angles()

    # Crear un triángulo rectángulo
    point_6 = Point(3, 4)  
    line_7 = Line(point_1, point_2)
    line_8 = Line(point_2, point_6)
    line_9 = Line(point_6, point_1)
    triangle_rect = TriRectangle()
    triangle_rect.set_vertices([point_1, point_2, point_6])  
    triangle_rect.set_edges([line_7, line_8, line_9])
    triangle_rect.compute_inner_angles()

    # Crear un rectángulo
    point_1_rectangle = Point(0, 0)  
    point_2_rectangle = Point(4, 0)
    point_3_rectangle = Point(4,3)
    point_4_rectangle = Point(0,3)


    line_1_rectangle = Line(point_1_rectangle, point_2_rectangle)
    line_2_rectangle = Line(point_2_rectangle,point_3_rectangle )
    line_3_rectangle = Line(point_3_rectangle,point_4_rectangle )
    line_4_rectangle = Line(point_4_rectangle, point_1_rectangle)

    rectangle = Rectangle()
    rectangle.set_vertices([point_1_rectangle, point_2_rectangle, point_3_rectangle, point_4_rectangle]) 
    rectangle.set_edges([line_1_rectangle, line_2_rectangle, line_3_rectangle, line_4_rectangle])
    rectangle.compute_inner_angles()

    # Crear un cuadrado
    
    point_1_square = Point(0, 0)  
    point_2_square = Point(4, 0)
    point_3_square = Point(4,4)
    point_4_square = Point(0,4)
    line_1_square = Line(point_1_square, point_2_square)
    line_2_square = Line(point_2_square,point_3_square )
    line_3_square = Line(point_3_square,point_4_square )
    line_4_square = Line(point_4_square, point_1_square)

    square = Square()
    square.set_vertices([point_1_square, point_2_square, point_3_square, point_4_square])  
    square.set_edges([line_1_square, line_2_square, line_3_square, line_4_square])
    square.compute_inner_angles()
    
    # Calcular y mostrar información para cada forma
    for shape in [triangle_scalene, triangle_isosceles, equilateral_triangle, triangle_rect, rectangle,square]:
        print("\nShape:", shape.__class__.__name__)
        print("Vertices:")
        for vertex in shape.get_vertices():
            print("({}, {})".format(vertex.get_x(), vertex.get_y()))

        print("Edge lengths:")
        for edge in shape.get_edges():
            print(edge.get_length())

        print("Inner angles:")
        for angle in shape.get_inner_angles():
            print(angle)

        print("Area:", shape.compute_area())
        print("Perimeter:", shape.compute_perimeter())

if __name__ == "__main__":
    main()

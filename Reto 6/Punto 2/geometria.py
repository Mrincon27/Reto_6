from math import sqrt, isclose
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start = start_point
        self.end = end_point
        self.length = self.compute_length()

    def compute_length(self) -> float:
        """Calcula la longitud de la línea."""
        return sqrt((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)

class Shape:
    def __init__(self, is_regular: bool, vertices: "list[Point]"):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = self.calculate_edges()
        self.inner_angles = self.compute_inner_angles()
    

    def calculate_edges(self) -> "list[Line]":
        edges = []
        for i in range(len(self.vertices)):
            start_point = self.vertices[i]
            end_point = self.vertices[(i + 1) % len(self.vertices)]  # Ciclo cerrado
            edges.append(Line(start_point, end_point))
        return edges

    def compute_perimeter(self) -> float:
        return sum(edge.length for edge in self.edges)

    def compute_area(self) -> float:
        raise NotImplementedError("El cálculo de área debe ser implementado por las subclases.")

    def compute_inner_angles(self) -> "list[float]":
        raise NotImplementedError("El cálculo de los ángulos debe ser implementado por las subclases.")

    def __str__(self):
        return f"Forma con {len(self.vertices)} vértices."


class Rectangle(Shape):
    """Clase para representar rectángulos."""

    def __init__(self, is_regular: bool, vertices: "list[Point]"):
        if len(vertices) != 4:
            raise ValueError("Un rectángulo debe tener exactamente 4 vértices.")
        super().__init__(is_regular, vertices)

    def compute_area(self) -> float:
        """Calcula el área como ancho x altura."""
        width = self.edges[0].length
        height = self.edges[1].length
        return width * height

    def compute_inner_angles(self) -> "list[float]":
        """Devuelve los ángulos internos de un rectángulo."""
        return [90, 90, 90, 90]

    def __str__(self):
        return "Rectángulo."


class Square(Rectangle):
    """Clase para representar cuadrados."""

    def __init__(self, is_regular: bool, vertices: "list[Point]"):
        super().__init__(is_regular, vertices)
        if not self.is_regular:
            raise ValueError("Un cuadrado debe ser regular.")
        lengths = [edge.length for edge in self.edges]
        if not all(isclose(length, lengths[0], rel_tol=1e-9) for length in lengths):
            raise ValueError("Todos los lados de un cuadrado deben tener la misma longitud.")

    def __str__(self):
        return "Cuadrado."

class ShapeWithComposition:
    """Clase base que utiliza composición para definir formas con bordes."""

    def __init__(self, is_regular: bool, vertices: "list[Point]"):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = self.calculate_edges()

    def calculate_edges(self) -> "list[Line]":
        """Calcula las líneas que forman los bordes de la forma."""
        edges = []
        for i in range(len(self.vertices)):
            start_point = self.vertices[i]
            end_point = self.vertices[(i + 1) % len(self.vertices)]
            edges.append(Line(start_point, end_point))
        return edges

    def compute_perimeter(self) -> float:
        """Calcula el perímetro sumando las longitudes de los bordes."""
        return sum(edge.length for edge in self.edges)

    def __str__(self):
        return f"Forma compuesta por {len(self.edges)} bordes."


class TriangleComposition(ShapeWithComposition):
    """Clase para representar triángulos usando composición."""

    def __init__(self, is_regular: bool, vertices: "list[Point]"):
        if len(vertices) != 3:
            raise ValueError("Un triángulo debe tener exactamente 3 vértices.")
        super().__init__(is_regular, vertices)

    def compute_area(self) -> float:
        """Calcula el área usando la fórmula de Herón."""
        a, b, c = (edge.length for edge in self.edges)
        s = (a + b + c) / 2  # Semiperímetro
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def __str__(self):
        return "Triángulo."

try:
    vertices = [Point(0, 0), Point(1, 0), Point(1, 1)]  
    rectangle = Rectangle(is_regular=True, vertices=vertices)
except ValueError as e:
    print(e) 

try:
    vertices = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
    square = Square(is_regular=False, vertices=vertices) 
except ValueError as e:
    print(e) 

try:
    vertices = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]  
    triangle = TriangleComposition(is_regular=True, vertices=vertices)
except ValueError as e:
    print(e)
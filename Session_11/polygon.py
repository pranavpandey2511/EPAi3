import math

class Polygon:
    """
    Polygon class to create polygons which are regular strictly convex.\n\
    Regular strict polygons have two properties: \n 1- All interior angles are less than 180. \
    \n 2- All sides have equal length
    """

    def __init__(self, n_edges: int, circumradius: float):
        assert isinstance(n_edges, int) and n_edges >= 3, "Number of Edges must be an integer greater than or equal to 3."
        assert isinstance(circumradius, (int, float)) and circumradius > 0, "Circumradius should be float or int and not less than or eual to 0."
        self._n_edges = n_edges
        self._circumradius = circumradius

    @property
    def n_edges(self):
        """Number of edges in the polygon"""
        return self._n_edges

    @n_edges.setter
    def n_edges(self, value):
        """Number of edges setter"""
        self._n_edges = value

    @property
    def circumradius(self):
        """Circumradius of the polygon"""
        return self._circumradius

    @circumradius.setter
    def circumradius(self, value):
        self._circumradius = value

    @property
    def edge_length(self):
        """Edge length of individual edge in the polygon"""
        return (2 * self._circumradius * math.sin(math.pi/self._n_edges))

    @property
    def interior_angle(self):
        """Interior angle value of each angle in the polygon"""
        return (self._n_edges - 2) * (180/self._n_edges)

    @property
    def apothem(self):
        """Apothem length for the polygon"""
        return (self._circumradius * math.cos(math.pi/self._n_edges))

    @property
    def area(self):
        """Area of the polygon"""
        return (self._n_edges * self.edge_length * self.apothem * 0.5)

    @property
    def perimeter(self):
        """Perimeter of the polygon"""
        return (self._n_edges * self.edge_length)

    def __repr__(self):
        return f"Polygon(n_edges: {self.n_edges}, circumradius: {self.circumradius})"

    def __gt__(self, poly):
        """Provide ability to compare two objects for greater than '>' test."""
        if (self.n_edges > poly.n_edges): # If number of edges is greater then return True
            return True
        else:
            return False


    def __eq__(self, poly):
        """Provides ability to compare two objects for euality (==)."""
        if (self.n_edges == poly.n_edges) and (self.circumradius == poly.circumradius): # if both number of edges and circumradius is equal then return True
            return True
        else:
            return False
import math
import operator
from functools import reduce, lru_cache
from polygon import Polygon

class PolygonsIterator:
    '''
    This class is to make the Polygon sequence class (PolyList) of type Iterator.
    '''
    def __init__(self, n_edges_max, circumradius):
        if n_edges_max < 3:
            raise ValueError('number of maximum edges must be greater than 3')
        self._n_edges_max = n_edges_max
        self._circumradius = circumradius
        self._index = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self._index > self._n_edges_max:
            raise StopIteration
        else:
            result = Polygon(self._index, self._circumradius)
            self._index += 1
            return result
class PolyList:
    """Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
    by n_edges_max  and circumradius for all polygons is is given by circumradius and is same for all polygons"
    """
    def __init__(self, n_edges_max: int, circumradius: float):
        assert isinstance(n_edges_max, int) and n_edges_max > 2, "Number of edges should atleast be 3 (int)."
        self._n_edges_max = n_edges_max
        self._circumradius = circumradius
        self._max_efficient = None
    
    def __len__(self):
        return self._n_edges_max - 2


    def __repr__(self):
        return (str(self[:]))


    def __iter__(self):
        return PolygonsIterator(self._n_edges_max, self._circumradius)

    @property
    def most_efficient(self):
        """Most efficient polygon in terms of area:perimeter ratio.
        """
        if self._max_efficient is None:
            self._max_efficient = sorted(PolygonsIterator(self._n_edges_max, self._circumradius), key = lambda poly: poly.area/poly.perimeter, reverse=True)[0] #get the first element from the sorted list
        return self._max_efficient
import math
import operator
from functools import reduce, lru_cache
from polygon import Polygon

class PolyList:
    """Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
    by n_edges_max  and circumradius for all polygons is is given by circumradius and is same for all polygons"
    """
    def __init__(self, n_edges_max: int, circumradius: float):
        assert isinstance(n_edges_max, int) and n_edges_max > 2, "Number of edges should atleast be 3 (int)."
        self._n_edges_max = n_edges_max
        self._circumradius = circumradius

    def __getitem__(self, index):
        if isinstance(index, int):
            # single item requested
            if index < 0:
                index = self._n_edges_max + index -2
            if index < 0 or index > self._n_edges_max - 3:
                raise IndexError(":: Index out of bounds ::")
            return self._polygon(self,index)
        else:
            # slice is requested
            idx = index.indices(self._n_edges_max)
            rng = range(*idx)
            return [self._polygon(self,n) for n in rng]

    @property
    def most_efficient(self):
        """Most efficient polygon in terms of area:perimeter ratio.
        """
        all_polys = {}
        for n in range(self._n_edges_max-2):
            all_polys[n] = self._polygon(self,n)
        all_polys = sorted(all_polys.values(), key= lambda poly: (poly.area/poly.perimeter))
        return all_polys[-1]

    @staticmethod
    @lru_cache(2**10)
    def _polygon(self, n_edges):
        n_edges += 3 # First is element with 3 sides, second is with 4 sides etc.
        return Polygon(n_edges=n_edges, circumradius = self._circumradius)

    def __len__(self):
        return self._n_edges_max - 2
    def __repr__(self):
        return (str(self[:]))
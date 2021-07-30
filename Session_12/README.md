# Session 12

## Assignment

The starting point for this assignment is the `Polygon` class and the `Polygons` sequence type you created in the previous assignment.

The code for these classes along with the unit tests for the `Polygon` class are below if you want to use those as your starting point. But use whatever you came up with in the last project.
You have two goals:
Goal 1:

Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").

Goal 2:

Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable and an iterator.

<br>
<hr>

A regular strictly convex polygon is a polygon that has the following characteristics:
all interior angles are less than 180
all sides have equal length

For a regular strictly convex polygon with:
$interiorAngle\:=\:\left(n\:-\:2\right)\cdot\frac{180}{n}$
<br>
$edgeLength,\:s\:=\:2\cdot R\cdot\sin\left(\frac{\pi}{n}\right)$

$apothem,\:a\:=\:R\cdot\cos\left(\frac{\pi}{n}\right)$

$area\:=\:\frac{1}{2}\cdot n\cdot s\cdot a$

$ perimeter\:=\:n\cdot s$

### Objective 1 [pts:400]:

Create a Polygon Class:
where initializer takes in:
number of edges/vertices
circumradius
that can provide these properties:

- edges
- vertices
- interior angle
- edge length
- apothem
- area
- perimeter

that has these functionalities:

- a proper **repr** function
- implements equality (==) based on # vertices and circumradius (**eq**)
- implements > based on number of vertices only (**gt**)

### Objective 2 [pts:600]:

Implement a Custom Polygon sequence type:
where initializer takes in:

- number of vertices for largest polygon in the sequence
- common circumradius for all polygons

that can provide these properties:

- max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
  that has these functionalities:

- functions as a sequence type (**getitem**)
- supports the len() function (**len**)
- has a proper representation (**repr**)

```python
from polygon import Polygon
```

```python
help(Polygon)
```

Help on class Polygon in module polygon:

class Polygon(builtins.object)
| Polygon(n_edges: int, circumradius: float)
|  
 | Polygon class to create polygons which are regular strictly convex.
| Regular strict polygons have two properties:
| 1- All interior angles are less than 180.  
 | 2- All sides have equal length
|  
 | Methods defined here:
|  
 | **eq**(self, poly)
| Provides ability to compare two objects for euality (==).
|  
 | **gt**(self, poly)
| Provide ability to compare two objects for greater than '>' test.
|  
 | **init**(self, n_edges: int, circumradius: float)
| Initialize self. See help(type(self)) for accurate signature.
|  
 | **repr**(self)
| Return repr(self).
|  
 | ----------------------------------------------------------------------
| Readonly properties defined here:
|  
 | apothem
| Apothem length for the polygon
|  
 | area
| Area of the polygon
|  
 | edge_length
| Edge length of individual edge in the polygon
|  
 | interior_angle
| Interior angle value of each angle in the polygon
|  
 | perimeter
| Perimeter of the polygon
|  
 | ----------------------------------------------------------------------
| Data descriptors defined here:
|  
 | **dict**
| dictionary for instance variables (if defined)
|  
 | **weakref**
| list of weak references to the object (if defined)
|  
 | circumradius
| Circumradius of the polygon
|  
 | n_edges
| Number of edges in the polygon
|  
 | ----------------------------------------------------------------------
| Data and other attributes defined here:
|  
 | **hash** = None

```python
Polygon(n_edges=4, circumradius=4)
```

    Polygon class to create polygons which are regular strictly convex.
            Regular strict polygons have two properties:
     1- All interior angles are less than 180.
     2- All sides have equal length

<h3> Objective 1 </h3>

```python
poly1 = Polygon(4, 4)
poly2 = Polygon(5, 3)
poly3 = Polygon(4, 6)
```

```python
poly1.n_edges
```

    4

```python
poly1.interior_angle
```

    90.0

```python
poly1.edge_length
```

    5.65685424949238

```python
poly1.apothem
```

    2.8284271247461903

```python
poly1.area
```

    32.0

```python
poly1.perimeter
```

    22.62741699796952

**\_\_repr\_\_**

```python
Polygon(n_edges=4, circumradius=4)
```

    Polygon class to create polygons which are regular strictly convex.
            Regular strict polygons have two properties:
     1- All interior angles are less than 180.
     2- All sides have equal length

**EQUAL TO '=='**

```python
poly1 == poly2
```

    False

```python
poly1 == poly3
```

    False

```python
poly1 == Polygon(n_edges=4, circumradius=4) # Same vertices and circumradius
```

    True

**GREATER THAN '>'**

```python
poly1 > poly2
```

    False

```python
poly2 > poly1
```

    True

```python
poly1 > poly3
```

    False

```python

```

```python

```

### Objective 2

### Custom polygon sequence

```python
from poly_list import PolyList
```

```python
help(PolyList)
```

Help on class PolyList in module poly_list:

class PolyList(builtins.object)
| PolyList(n_edges_max: int, circumradius: float)
|  
 | Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
| by n_edges_max and circumradius for all polygons is is given by circumradius and is same for all polygons"
|  
 | Methods defined here:
|  
 | **getitem**(self, index)
|  
 | **init**(self, n_edges_max: int, circumradius: float)
| Initialize self. See help(type(self)) for accurate signature.
|  
 | **len**(self)
|  
 | **repr**(self)
| Return repr(self).
|  
 | ----------------------------------------------------------------------
| Readonly properties defined here:
|  
 | most_efficient
| Most efficient polygon in terms of area:perimeter ratio.
|  
 | ----------------------------------------------------------------------
| Data descriptors defined here:
|  
 | **dict**
| dictionary for instance variables (if defined)
|  
 | **weakref**
| list of weak references to the object (if defined)

```python
my_poly = PolyList(5,4)
```

```python
my_poly[1]
```

Polygon(n_edges: 5, circumradius: 4)

```python
print(my_poly)
```

[Polygon(n_edges: 3, circumradius: 4), Polygon(n_edges: 4, circumradius: 4), Polygon(n_edges: 5, circumradius: 4), Polygon(n_edges: 6, circumradius: 4), Polygon(n_edges: 7, circumradius: 4)]

```python
my_poly.most_efficient
```

Polygon(n_edges: 5, circumradius: 4)

For n=25, most efficient polygon:

```python
new_list = PolyList(25, 7)
```

```python
new_list.most_efficient
```

Polygon(n_edges: 25, circumradius: 7)

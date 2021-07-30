import pytest
import os
import inspect
import re
import polygon, poly_list
from polygon import Polygon
from poly_list import PolyList

README_CONTENT_CHECK_FOR = [
    'polygon',
    'poly_list',
    'init',
    'repr',
    'eq',
    'gt',
    'len',
    'getitem',
    'area',
    'perimeter',
    'apothem',
    'circumradius',
    'edge_length',
    'most_efficient',
    'n_edges',
    'n_edges_max',
]

def test_session12_readme_exists():
    """
    Method checks if there is a README.md file. 
    failure_message: "README.md file missing!"  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session12_readme_500_words():
    """
    Method checks if there are atleast 500 words in the README.md file
    failures_message: Make your README.md file interesting! Add atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session12_readme_proper_description():
    """
    Method checks if all the functions are described in the README.md file
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_session12_readme_file_for_more_than_10_hashes():
    """
    Method checks if README.md file has atleast 10 '#' (indentations)
    failures_message: You have not described all the functions/classes well in your README.md file 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_polygon_indentations():
    """
    Method checks for proper indentations \
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(polygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_poly_list_indentations():
    """
    Method checks for proper indentations
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(poly_list)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_polygon_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session10.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_poly_list_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session10.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(poly_list, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_poly_class():
    poly1 = Polygon(4, 4)
    poly2 = Polygon(5, 3)

    assert poly1.area == 32.0, "area calculated is wrong"
    assert poly2.area == 21.398771616640957, "area calculated is wrong"

    assert poly1.perimeter == 22.62741699796952, "perimeter calculated is wrong"
    assert poly2.perimeter == 17.633557568774194, "perimeter calculated is wrong"

    assert poly1.apothem == 2.8284271247461903, "apothem value is wrong"
    assert poly2.apothem == 2.4270509831248424, "apothem value is wrong" 

    assert poly1.circumradius == 4, "Circumradius is not correct"
    assert poly2.circumradius == 3, "Circumradius is not correct"

    assert poly1.edge_length == 5.65685424949238, "Edge length is not correct"
    assert poly2.edge_length == 3.526711513754839, "Edge length is not correct"

    poly3 = Polygon(4,4)

    assert poly1 == poly3, "Equality check doesn't work properly"
    assert poly2 > poly1, "Greater than check doesn't work properly"

def test_polygon_sequence():
    my_poly = PolyList(7,7)

    len(my_poly) == 5, "Length of the sequence is incorrect"



    my_poly.most_efficient == Polygon(7, 7), "Most efficient item in the sequence is not correct."
    
    my_poly = iter(my_poly)
    first_poly = next(my_poly)
    first_poly == Polygon(3,7), "First element in the sequence is incorrect"
    next(my_poly) == Polygon(7,7), "Last element in the sequence is incorrect"
    next(my_poly) == Polygon(6,7), "Second to last element in the sequence is incorrect"
    next(my_poly) == Polygon(5,7), "Third to last element in the sequence is incorrect"
    next(my_poly) == Polygon(4,7), "Fourth to last element in the sequence is incorrect"



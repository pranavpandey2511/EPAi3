import pytest
import os
import inspect
import re
import session_9
from session_9 import nt_approach, dict_approach, tsai_index

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"
    

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session_9, inspect.isfunction)
    for function in functions:
        #print(f"Name:{function}")
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_nt_approach():
    result = nt_approach(num_profiles=10000)
    assert any(["largest_blood_type" in o for o in list(result._fields)]), "Largest blood type not present in output."
    assert any(["mean_location" in o for o in list(result._fields)]), "Mean location not present in output."
    assert any(["oldest_person" in o for o in list(result._fields)]), "Oldest person age not present in output."
    assert any(["average_age" in o for o in list(result._fields)]), "Average age not present in output."
    assert (result[0]) in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], 'largest blood type not correct'
    assert (result[1]) > (-360,-360), 'mean_current_location not correct'
    assert (result[2]) > 0, 'oldest_person_age not correct'
    assert (result[3]) > 0, 'average_age not correct'

# Create test for funciton dict_approach
def test_dict_approach():
    result = dict_approach(num_profiles=10000)
    assert len(result) == 4
    assert any(["largest_blood_type" in o for o in list(result.keys())]), "Largest blood type not present in output."
    assert any(["mean_location" in o for o in list(result.keys())]), "Mean location not present in output."
    assert any(["oldest_person" in o for o in list(result.keys())]), "Oldest person age not present in output."
    assert any(["average_age" in o for o in list(result.keys())]), "Average age not present in output."
    assert (result['largest_blood_type']) in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], 'largest blood type not correct'
    assert (result['mean_location']) > (-360,-360), 'mean_current_location not correct'
    assert (result['oldest_person']) > 0, 'oldest_person_age not correct'
    assert (result['average_age']) > 0, 'average age note correct'

# Create a test function for tsai_index function
def test_tsai_index():
    result = tsai_index(num_comp=100)
    assert len(result) == 4
    assert any(["open" in o for o in list(result._fields)])
    assert any(["high" in o for o in list(result._fields)])
    assert any(["close" in o for o in list(result._fields)])
    assert any(["low" in o for o in list(result._fields)])
    assert (result[0][0]) > 0 #open
    assert (result[1][1]) > 0 #high
    assert (result[3][3]) > 0 #close
    assert (result[2][2]) > 0 #low
    assert (result[2][2]) < result[1][1] #low < high




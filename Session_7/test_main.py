from main import doc_checker, fibonacci, keep_count, count_dict, mult, addition, divide, keep_count_mod


def doc_test_func():
    """This is sample function to be used in performing tests of ducment checker function 
    for testing the docstring character length.
    """
    pass

def doc_test_func2():
    """This is sample function.
    """
    pass

def doc_test_func3():
    """"""
    pass

def doc_test_func4():
    """This is sample function to be used in performing tests of ducment checker function 
    for testing the docstring character length. This is just a copy of first function docstring.
    """
    pass


def test_doc_checker():
    assert doc_checker(doc_test_func)() == True, "Functiion docstring is less than 50 characters"
    assert doc_checker(doc_test_func2)() == False, "Functiion docstring is not less than 50 characters but returned False"
    assert doc_checker(doc_test_func3)() == False, "Functiion docstring is not less than 50 characters but returned False"
    assert doc_checker(doc_test_func4)() == True, "Functiion docstring is less than 50 characters"

def test_fibonacci():
    next_fib = fibonacci()
    assert next_fib() == 2, "Wrong fibonacci number in the series" 
    assert next_fib() == 3, "Wrong fibonacci number in the series"
    assert next_fib() == 5, "Wrong fibonacci number in the series"
    assert next_fib() == 8, "Wrong fibonacci number in the series"

def test_keep_count():
    mul = keep_count(mult)
    add = keep_count(addition)
    div = keep_count(divide)
    assert mul(3,3) == 9, "Wrong multiplication"
    assert mul(2,3) == 6, "Wrong multiplication"
    assert add(6,4) == 10, "Wrong addition"
    assert add(6,7) == 13, "Wrong addition"
    assert div(6,2) == 3, "Wrong division"
    assert div(6,1) == 6, "Wrong division"
    assert count_dict == {"mult": 2, "addition": 2, "divide": 2}, "Counting is not correct"

def test_keep_count_mod():
    first_dict = {}
    second_dict = {}
    mul = keep_count_mod(mult)
    add = keep_count_mod(addition)
    div = keep_count_mod(divide)
    assert mul(3,3, curr_dict=first_dict) == 9, "Wrong multiplication"
    assert mul(2,3, curr_dict=first_dict) == 6, "Wrong multiplication"
    assert add(6,4, curr_dict=first_dict, curr_dict2=second_dict) == 10, "Wrong addition"
    assert add(6,7,curr_dict=first_dict,curr_dict2=second_dict) == 13, "Wrong addition"
    assert div(6,2, curr_dict=first_dict, curr_dict2=second_dict) == 3, "Wrong division"
    assert div(6,1,curr_dict=first_dict,curr_dict2=second_dict) == 6, "Wrong division"
    assert first_dict == {"mult": 2, "addition": 2, "divide": 2}, "Counting is not correct"
    assert second_dict == {"addition": 2, "divide": 2}, "Counting is not correct"

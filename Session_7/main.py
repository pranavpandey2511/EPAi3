from typing import Callable, Dict
from functools import reduce


count_dict = {}

def doc_checker(func: Callable):
    """Closure which returns a function for checking docstring length for any function passed to it."""
    func_len = 0
    def len_checker():
        """This function takes another function as input and checks the length of the docstring of the input function.
        """
        nonlocal func_len
        func_len = len(func.__doc__)
        return True if func_len>50 else False
    return len_checker

def fibonacci():
    """Create a closure which returns a function which on being called
    returns the next number in the fibonacci series.
    Returns:
        next_fib (Callable): Function which retruns next fibonacci number everytime it's called.
    """

    first = 1
    second = 1
    def next_fib():
        """Takes the previous two fibonacci numbers and adds them to give th next number in the series.

        Returns:
            Integer: Next number in the fibonacci series.
        """
        nonlocal first, second
        first, second = second, first+second

        return second
    return next_fib

def keep_count(func: Callable):
    """ Closure which returns 3 function - mul, add, and div and keep track of how many times each of these functions are called.
    """
    cnt = 0
    def inner(*args, **kwargs):
        """Given a function arguments keep cpunt of function calls and returns the value. 
        """
        nonlocal cnt
        cnt += 1
        global count_dict
        count_dict[func.__name__] = cnt
        return func(*args, **kwargs)
    return inner


def mult(*args, **kwargs):
    """Given a sequence of numbers multiply all elements in the sequence and return the final value.
    Returns:
        Float : Multiplication of all elements passed in to the function.
    """

    return reduce(lambda a, b: a*b, args)

def addition(*args, **kwargs):
    """Given a sequence of numbers add all elements in the sequence and return the final value.

    Returns:
        Float : Addition of all the arguments passed to the function
    """

    return reduce(lambda a, b: a+b, args)

def divide(*args, **kwargs):
    """Given a sequence of numbers divide each element with the next element and return the final value.

    Returns:
        Float : Final divison result
    """

    return reduce(lambda a, b: a/b, args) if any(args)!=0 else 0


def keep_count_mod(func: Callable):
    """ Closure which returns 3 function - mul, add, and div and keep track of how many times each of these functions are called.
    """
    cnt = 0
    def inner(*args, **kwargs):
        """ Given a function arguments keep count of function calls and returns the value. 
        """
        nonlocal cnt
        cnt += 1
        for curr_dict in kwargs.values():
            curr_dict[func.__name__] = cnt
        return func(*args, **kwargs)
    return inner


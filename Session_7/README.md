# EPAi3

## Assignment

Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200

Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100 
We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250 
Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250  
Once done, upload the code to github, run actions, and then proceed to answer S7 - Assignment Solutions.   

## Implementation

1) Implemented a document character length checker closure which return a function thich in turns take an input and check \_\_doc__ length to find out if the docstring is more that 50 character long or not.

2) Implemented a closure which returns a function which upon being called returns the next fibonacci number in the series everytime it is called.

3) Implemented a closure to keep track of number of calls made for each function.

4) Implemented a closure which takes as input the function and then takes the dictionary as input


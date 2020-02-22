#!/usr/bin/env python3

"""
Fibonacci Series Exercise 
Computing the Fibonacci and Lucas Series
Author: Clifford Butler
"""

def fibonacci(n):
    """compute the nth Fibonacci number"""
    if (n < 0):
        return None
    
    elif (n == 0):
        return 0
    
    elif (n == 1):
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    # run some tests for fibonacci(n)
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13


    print("tests passed")


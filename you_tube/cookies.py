'''
How many cookies did cookie monster eat???
Different approaches
'''
from timeit import default_timer as timer
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt

DAYS = 12

def method_a (days):
    '''
    Long method for recursively counting 
    cookies. 
    '''

    cookies = 0
    for i in range(1, days+1):
        for j in range(1, i+1):
            cookies += j

    return cookies

def method_b (days):
    '''
    Euler method
    '''
    cookies = 0
    for i in range(1, days+1):
        cookies += (i*(i+1))/2
    return cookies
def method_c (days):
    return (Fraction(1,6)*days**3) + (0.5*days**2) + (Fraction(1,3)*days)
def plot (d):
    y = np.array([method_b(x) for x in range(1,d+1)])    
    x = np.array(range(1,d+1))
    plt.plot(x, y)
    plt.show()

def test(d):
    y = np.array([method_b(x) for x in range(1,d+1)])
    
    x = np.array(range(1,d+1))
    p = np.poly1d(np.polyfit(x,y,3))
    print(p(6))
    print(np.polyfit(x,y,3))

def run():
    start = timer()
    cookies = method_a(DAYS)
    end = timer()
    a_time = end - start
    a = f'Cookie monster ate {cookies} cookies in {a_time}'
    print(a)

    start = timer()
    cookies = method_b(DAYS)
    end = timer()
    b_time = end - start
    b = f'Cookie monster ate {cookies} cookies in {b_time}'
    print(b)

    start = timer()
    cookies = method_c(DAYS)
    end = timer()
    c_time = end - start
    c = f'Cookie monster ate {cookies} cookies in {c_time}'
    print(c)

    print(f'method b is {a_time/b_time} times faster')

if __name__ == "__main__":
    plot(DAYS)

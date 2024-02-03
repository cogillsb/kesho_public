'''
How many cookies did cookie monster eat???
'''
import numpy as np
from timeit import default_timer as timer

DAYS = 12

def method_a(days):
    '''
    the bad method
    '''
    cookies = 0
    for i in range(1,days+1):
        for j in range(1, 1+1):
            cookies += j
    return cookies
def run():
    start = timer()
    cookies = method_a(DAYS)
    end = timer()
    a_time = end - start
    print(f'Cookie Monster ate {cookies} in {a_time}')

if __name__ == "__main__": 
    run()

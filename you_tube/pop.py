from numpy.random import randint
from numpy.random import rand
import random

import warnings
warnings.filterwarnings("ignore")

def gen_pop(pop_sz, mx_len):
    N = 5
    chars = ['N', '(', ')', '*','^', '/', '+', '-', ' ' ] + [str(i) for i in (range(10))]
    pop = []
    while len(pop) < pop_sz:
        l = randint(0, mx_len)
        ind = ''
        for _ in range(l):
            ind += random.choice(chars)
        try: 
            eval(ind)
        except:
            continue
        if 'N' in ind:
            pop.append(ind)
    return pop


def mths(x):
    (1/2)*()



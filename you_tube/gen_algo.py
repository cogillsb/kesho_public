# genetic algorithm search for continuous function optimization
from numpy.random import randint
from numpy.random import rand
import random

import warnings
warnings.filterwarnings("ignore")
chars = ['N', '(', ')', '*','^', '/', '+', '-', ' ' ] + [str(i) for i in (range(10))]

# objective function
def objective(ns, p):
    scr = 0   
    for n in ns:
       
        N = n[0]
        try:
            e = eval(p)
            scr += 1 - (min(e,n[1])/max(e,n[1]))
        except:        
            return 1
        
        
        
    return scr/len(ns)
        

def selection(pop, scores, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        # check if better (e.g. per
        # form a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]
 


 
# crossover two parents to create two children
def crossover(p1, p2, r_cross):
    # crossover two parents to create two 
    # children are copies of parents by default
    c1, c2 = p1, p2
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
       
        
        pt1 = randint(1, max(2,len(p1)-2))
        pt2 = randint(1,max(2,len(p2)-2))

        # perform crossover
        c1 = p1[:pt1] + p2[pt2:]
        c2 = p2[:pt2] + p1[pt1:]

    return [c1, c2]

 
# mutation operator
def mutation(c, r_mut):
    chld = c
    for i in range(len(chld)):
        # check for a mutation
        if rand() < r_mut:            
            # change
            s = list(chld)
            s[i] = random.choice(chars)
            chld = ''.join(s)
    return chld

def gen_pop(pop_sz, mx_len):
    N = 0
    
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
 
# genetic algorithm
def genetic_algorithm(ns, pop_sz, mx_len, n_iter, r_cross=.9, r_mut=.25):
        print('generating pop')
        # initial pop
        pop = gen_pop(pop_sz, mx_len)

        # keep track of best solution
        best, best_eval = pop[0],  2000

        # enumerate generations
        for gen in range(n_iter):
            print(gen)
            # evaluate all candidates in the population
           
            scores = [objective(ns, p) for p in pop]
            # check for new best solution
            for i in range(pop_sz):
                if scores[i] < best_eval:
                    best, best_eval = pop[i], scores[i]
                    print(f">{gen}, new best {pop[i]} = {scores[i]}")

            # select parents
            selected = [selection(pop, scores) for _ in range(int(pop_sz/2))]
            selected += gen_pop(int(pop_sz/2), mx_len)
           
            # create the next generation
            children = list()

            for i in range(0, pop_sz, 2):
                # get selected parents in pairs
                p1, p2 = selected[i], selected[i+1]
                cs = crossover(p1, p2, r_cross)
                children += [mutation(c, r_mut) for c in cs]
            pop = children
        
        return [best, best_eval]



     


ns = [(x, (x*(x+1))/2) for x in range(1, 100)] 
#p = 'N'
#print(objective(ns, p))

pop_sz = 100
mx_len = 20
n_iter = 1000


best, score = genetic_algorithm(ns, pop_sz, mx_len, n_iter)
print('Done!')

print(f'{best} {score}')




import sys, os.path, math, timeit
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

def main():
    print('''    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ? (6,857)''')
    N = 600851475143
    n = 10
    r = 3
    t = [1]
    o = sys.modules[__name__]
    u = usage
    util.runTests({'N': N}, {'n': n, 'r': r, 't': t, 'o': o, 'u': u})

def usage(a1={}, a2={}):
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    print("    Usage: 'N n r t' where N ({}) product #, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))

def test1(args={'dbg': 1}):
    '''uses util.isPrime() (3, sqrt(N)+1, 2)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    p = []
    M = int(math.sqrt(N))
    for i in (range(3, M+1, 2)): 
        if N % i == 0:
            if util.isPrime(i):
                p.append(i)
#    if dbg: print(p)
    if dbg: print('\n{} largest prime factor = {:,}'.format(test, p[-1]), end=' ')

def test2(args={'dbg': 1}):
    '''uses util.isPrime() i=odd while(i*i <= N)'''
    test = 'test2'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    p = []
    i = 3
    while i * i <= N:
        if N % i == 0:
#            print('{} is a factor of N ({})'.format(i, N/i), end=' ')
            if util.isPrime(i):
                p.append(i)
        i += 2
#    if dbg: print('{} {} {} {}'.format(N, i, p, p[-1]))
    if dbg: print('\n{} Largest prime factor = {:,}'.format(test, p[-1]), end=' ')

def test3(args={'dbg': 1}):
    '''uses util.isPrime() (i <= M) (M % i)'''
    test = 'test3'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    pf = []
    i = 3
    M = N
    while i <= M:
        while M % i == 0:
            if util.isPrime(i):
#                if dbg: print('M={}, i={}'.format(M, i))
                pf.append(i)
                M = int(M/i)
        i += 1
#    if dbg: print('prime factors = {}'.format(pf))
    if dbg: print('\n{} largest prime factor = {:,}'.format(test, pf[-1]), end=' ')

if __name__ == "__main__":
    main()
    
import sys, os.path, math, timeit
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

def main():
    print('''    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
    Find the sum of all primes below two million. (142,913,828,922)''')
    N = 100000
    n = 10
    r = 3
    t = [1, 2]
    o = sys.modules[__name__]
    u = usage
    util.runTests({'N': N}, {'n': n, 'r': r, 't': t, 'o': o, 'u': u})

def usage(a1={}, a2={}):
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    print("    Usage: 'N n r t' where N ({}) upper limit of primes, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))
    
def test1(args={'dbg': 1}):
    '''range(3, N, 2) isPrime(n)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    p, s = [2], 2
    for n in range(3, N, 2):
        if util.isPrime(n):
            p.append(n)
            s += n
#    print('{}'.format(p))
    if dbg: print('\n{} the sum of primes below {:,} = {:,}'.format(test, N, s), end=' ')
    
def test2(args={'dbg': 1}):
    '''range(3, N) isPrime(n)'''
    test = 'test2'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    p, s = [2], 2
    for n in range(3, N, 2):
        if util.isPrime(n):
            p.append(n)
            s += n
#    print('{}'.format(p))
    if dbg: print('\n{} the sum of primes below {:,} = {:,}'.format(test, N, s), end=' ')

if __name__ == "__main__":
    main()

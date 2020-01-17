import sys, os.path, math, timeit
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

def main():
    print('''    The sum of the squares of the first ten natural numbers is 1**2 + 2**2 + ... + 10**2 = 385
    The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)**2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum (25,164,150)''')
    N = 100
    n = 20
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
    print("    Usage: 'N n r t' where N ({}) # natural numbers, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))

def test1(args={'dbg': 1}):
    '''(1, N+1)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    m, p = 2, 1
    sum1, sum2 = 0, 0
    for i in range(1, N + 1):
        sum1 += i
        sum2 += i * i
    sum1 *= sum1
    if dbg: print('\n{} sum1={:,} sum2={:,} diff={:,}'.format(test, sum1, sum2, sum1 - sum2), end=' ')
    
def test2(args={'dbg': 1}):
    '''(1, N+1) and sum'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    s = sum([x for x in range(N+1)])**2 - sum([x*x for x in range(N+1)])
    if dbg: print('\n{} {}'.format(test, s), end=' ')

def test3(args={'dbg': 1}):
    '''(1, N+1)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    s = sum([x*x*(x-1) for x in range(1, N+1)])
    if dbg: print('\n{} {}'.format(test, s), end=' ')

def test4(args={'dbg': 1}):
    '''(1, N+1)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    squaredsum = lambda n: (n * (n + 1) / 2) ** 2
    sumsquares = lambda n: n * (n + 1) * (n * 2 + 1) / 6
    if dbg: print('\n{} {}'.format(test, squaredsum(N) - sumsquares(N)), end=' ')

if __name__ == "__main__":
    main()

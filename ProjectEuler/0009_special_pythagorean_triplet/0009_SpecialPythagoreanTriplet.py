import sys, os.path, math, timeit
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

def main():
    print('''    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a**2 + b**2 = c**2
    For example 3**2 + 4**2 = 9 + 16 = 25 = 5**2
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the product abc. (31,875,000)''')
    N = 1000
    M = 4
    n = 10
    r = 1
    t = [1]
    o = sys.modules[__name__]
    u = usage
    util.runTests({'N': N}, {'n': n, 'r': r, 't': t, 'o': o, 'u': u})
        
def usage(a1={}, a2={}):
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    print("    Usage: 'N n r t' where N ({}) is the sum of a + b + c, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))
   
def test1(args={'dbg': 1}):
    '''for a(1, N) for i(1, N-a) math.sqrt()'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    p = 1
    for a in range(1, N):
        for i in range(1, N - a):
            b = a + i
            cSqrd = a**2 + b**2
            cf = math.sqrt(cSqrd)
            c = int(cf)
            if c * c == cSqrd:
#                print('{} {} {}, {} {} {} a+b+c={}'.format(a, b, c, a**2, b**2, cSqrd, s))
                s = a + b + c
                if s == N:
                    p = a * b * c
                    break
        if p > 1: break
    if dbg:
        if p == 0: print('\n    {} NOT FOUND', test)
        else: print('\n{} a * b * c = {:,}  {} + {} + {} = {}  {:,} + {:,} = {:,}'.format(test, p, a, b, c, N, a**2, b**2, c**2), end=' ')
    
def test2(args={'dbg': 1}):
    '''Dummy'''
    test = 'test2'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if not dbg: print('.', end='')
    if dbg: print('\n{} {}'.format(test, test2.__doc__), end=' ')

if __name__ == "__main__":
    main()

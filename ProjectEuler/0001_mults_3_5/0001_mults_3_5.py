import sys, os.path, timeit
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util
"""
def main():
    print('''    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000. (233,168)''')
    N = 10
    prods = [3, 5]
    argMap = {}
    argMap = cmdArgs.parseCmdLine(dbg=0)
    print('argMap={}'.format(argMap))
    if '' in argMap:
        N = int(argMap[''][0])
        for i in range(1, len(argMap[''])):
            prods.append(int(argMap[''][i]))
    print('N={}, prods={}'.format(N, prods))

def usage(a1={}, a2={}):
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    print("    Usage: 'N n r t' where N ({}) max #, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))

def test1(args={'dbg': 1}):
    '''(2, N) (prods)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    pSum, pList = 0, []
    for i in range(2, N):
        for j in prods:
            if i % j == 0:
                pSum += i
                pList.append(i)
                break;
#    if dbg: print('pList={}'.format(pList))
    if dbg: print('\n{}, sum={}'.format(test, pSum), end=' ')
"""

def main():
    print('''    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000. (233,168)''')
    N = 100
    P = [3, 5]
    n = 10
    r = 3
    t = [1]
    o = sys.modules[__name__]
    u = usage
    util.runTests({'N': N, 'P': P}, {'n': n, 'r': r, 't': t, 'o': o, 'u': u})
#    print('N={}, P={}'.format(N, P))

def usage(a1={}, a2={}):
    if 'P' in a1: P = a1['P']
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    print("    Usage: 'N n r t' where N ({}) max #, P ({}) prod list, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, P, n, r, t))

def test1(args={'dbg': 1}):
    '''(2, N) [P]'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if 'P'   in args:   P = args['P']   
    if dbg == 0: print('.', end='')
    pSum, pList = 0, []
    for i in range(2, N):
        for j in P:
            if i % j == 0:
                pSum += i
                pList.append(i)
                break;
#    if dbg: print('pList={}'.format(pList))
    if dbg: print('\n{}, sum={:,}'.format(test, pSum), end=' ')
    
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
    
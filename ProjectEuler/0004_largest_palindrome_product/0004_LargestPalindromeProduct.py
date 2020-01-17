import sys, os.path, math, timeit
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

def main():
    print('''    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
    Find the largest palindrome made from the product of two 3-digit numbers. (906,609)''')
    N = 3
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
    print("    Usage: 'N n r t' where N ({}) half #digits 'palindromic', n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))

def test1(args={'dbg': 1}):
    '''(n, 99, -1) (n, 99, -1)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    n = 1
    for i in range(N):
        n *= 10
    n -= 1
    pList = []
    for i in range(n, 99, -1):
        for j in range(n, 99, -1):
            p = i * j
            s = str(p)
            l = len(s)
            left = s[0:int(l/2)]
            right = s[int(l/2):]
#            print('{} {} {} {} {}'.format(i, j, p, left, right))
            if right[::-1] == left:
                tmp = [p, i, j]
                pList.append(tmp)
#                print('found palindrome for {} digit product {}'.format(N, p))
    pList.sort()
#    print('{}'.format(pList))
    if dbg: print('\n{} largest palindrome for {} digit products {:,} = {} * {}'.format(test, N, pList[-1][0], pList[-1][1], pList[-1][2]), end=' ')

if __name__ == "__main__":
    main()
    
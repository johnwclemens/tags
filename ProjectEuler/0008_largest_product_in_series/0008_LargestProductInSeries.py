import sys, os.path, math, timeit
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

d = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''
d = d.replace('\n', '')

def main():
    print('''    The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    23,514,624,000 = 5 * 5 * 7 * 6 * 6 * 8 * 9 * 6 * 6 * 4 * 8 * 9 * 5''')
    N = 1000
    M = 4
    n = 10
    r = 1
    t = [1]
    o = sys.modules[__name__]
    u = usage
    print('{}'.format(d))
    util.runTests({'N': N, 'M': M}, {'n': n, 'r': r, 't': t, 'o': o, 'u': u})

def usage(a1={}, a2={}):
    if 'M' in a1: M = a1['M']
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    print("    Usage: 'N n r t' where N ({}) #digits, M ({}) #adjacent , n ({}) loops, r ({}) repeats, t ({}) test#".format(N, M, n, r, t))

def test1(args={'dbg': 1}):
    '''range(N - M + 1) range(M)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if 'M'   in args:   M = args['M']
    if dbg == 0: print('.', end='')
    P = 0
    for i in range(N - M + 1):
        s = d[i:i+M]
        p = 1
        for j in range(M):
            p *= int(s[j])
        if p > P: 
            P = p
            S = s
#        print('i={} s={} p={:,} P={:,} S={}'.format(i, s, p, P, S))
    if dbg:
        print('\n{} {:,} ='.format(test, P), end=' ')
        print('({})'.format(' * '.join(S)), end=' ')
    
def test2(args={'dbg': 1}):
    '''Dummy'''
    test = 'test2'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if dbg == 0: print('.', end='')
    if dbg: print('\n{} {}'.format(test, test2.__doc__), end=' ')
    
if __name__ == "__main__":
    main()
    
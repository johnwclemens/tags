import sys, os.path, math, timeit, functools
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

def main():
    print('''    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? (232,792,560)''')
    N = 20
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
    print("    Usage: 'N n r t' where N ({}) max #, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))

# 10 2520
# 20 232792560
# 30 2329089562800
# 40 5342931457063200
# 50 3099044504245996706400
def test1(args={'dbg': 1}):
    '''(3, N, 2) util.isPrime()'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    m = 2
    while m < N / 2:
        m *= 2
    M = m
#    if dbg: print('m = {}'.format(m))
    for n in range(3, N, 2):
        if util.isPrime(n):
            m = n
            while m < N / n:
                m *= n
            M *= m
    if dbg: print('\n{} {:,}'.format(test, M), end=' ')

def test1B(args={'dbg': 1}):
    '''(3, N, 2) util.isPrime() & list primes'''
    test = 'test1B'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    pList = []
    m = 2
    while m < N / 2:
        m *= 2
    pList.append(m)
#    if dbg: print('m = {}'.format(m))
    for n in range(3, N, 2):
        if util.isPrime(n):
            m = n
            while m < N / n:
                m *= n
            pList.append(m)
    if dbg: 
#        print('{}'.format(pList))
        M = 1
        for p in pList:
            M *= p
        print('\n{} {:,}'.format(test, M), end=' ')

def test2(args={'dbg': 1}):
    '''k(1, N+1) j(1, N+1)'''
    test = 'test2'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    pList = []
    i = 1
    for k in (range(1, N + 1)):
        if i % k > 0:
            for j in range(1, N + 1):
                if (i * j) % k == 0:
                    i *= j
                    pList.append(j)
                    break
#    if dbg: print('{}'.format(pList))
    if dbg: print('\n{} {:,}'.format(test, i), end=' ')

def test3(args={'dbg': 1}):
    '''m=2520 i(3, N)'''
    test = 'test3'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    n = 0
    m = 2520 # 8 * 5 * 7 * 9
    found = 0
    while found == 0:
        n += m
        found = 1
        for i in range(3, N):
            if n % i != 0:
                found = 0
                break
#            if dbg: print('n={}, i={}'.format(n, i))
    if dbg: print('\n{} {:,}'.format(test, n), end=' ')

def test5(args={'dbg': 1}):
    '''while(1) y(N-1, 0, -1) x+=N'''
    test = 'test5'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    x = N
    while 1:
        for y in range(N-1, 0, -1):
#            dbg: print('x={}, y={}'.format(x, y))
            if x % y != 0:
                break
        if y == 0:
            print('{}'.format(x))
            break
        x += N
        
def test6(args={'dbg': 1}):
    '''while(test<=N, 1) k(primes) while(t%k==0 & t !=k & k!=1)'''
    test = 'test6'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    primes = []
    product = 1
    test = 1
    n = 1
    while test <= N:
        if not product % test == 0:
            t = test
            for k in primes:
                while t % k == 0 and t != k and k != 1:
                    t //= k
            primes += [t]
            product *= t
        test += 1
    if dbg: print('\n{} {}'.format(test, product), end=' ')

'''
def testB():
    test = 'testB'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    prime = primes(N) # you need a prime sieve up to N.
    res = 1
    for p in prime:
        q = p
        n_p = n//p
        while q <= n_p:
            q *= p
        res *= q
    res = str(res)
    return len(res), res[:9], res[-20:] # nb of digits, start, end
'''

def pfact(n):
    res=[]
    i=2 
    while i < n/2: 
        if n/i == float(n)/i:
            res.append(i)
            n=n/i
        else:
            i+=1
    res.append(n)
    return res

def test7(args={'dbg': 1}):
    '''i(2, N+1) reduce'''
    test = 'test7'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    allfacts={}
    for i in range(2,N+1):
        facts=pfact(i)
        for i in facts:
           allfacts[i] = max(allfacts.get(i,0), facts.count(i))
    d=[item**value for (item,value) in allfacts.items()]
    return functools.reduce(int.__mul__,d)
    
if __name__ == "__main__":
    main()
    
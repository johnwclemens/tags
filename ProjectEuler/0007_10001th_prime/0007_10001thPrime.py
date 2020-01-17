import sys, os.path, math, timeit, inspect
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

def main():
    print('''    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number? (104,743)''')
    N = 10001
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
    print("    Usage: 'N n r t' where N ({}) Nth prime, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, n, r, t))

def test1(args={'dbg': 1}):
    '''Inline version of isPrime(): (m<=N) (i^2<=p, 2)'''
    test = 'test1'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    m, p = 2, 1
    if dbg == 0: print('.', end='')
    elif dbg > 1: print('m={} is {} prime ? yes'.format(m-1, p+1))
    while m <= N:
        p += 2
        if dbg > 1: print('m={} is {} prime ?'.format(m, p), end=' ')
        i = 3
        isPrime = 1
        while i * i <= p:
            if dbg > 1: print('    i={} i*i={} p={}'.format(i, i * i, p), end=' ')
            if p % i == 0:
                if dbg > 1: print('No divisible by {} => {}'.format(i, p//i))
                isPrime = 0
                break
            i += 2
#            print('    i={} i*i={} p={}'.format(i, i*i, p), end=' ')
        if isPrime == 1:
            if dbg > 1: print('yes')
#                print('n={} p={} isPrime={}'.format(n, p, isPrime))
            m += 1
    if dbg: print('\n{} {:,}th prime = {:,}'.format(test, N, p), end=' ')

def test1B(args={'dbg': 1}):
    '''Inline version of isPrime(): (m<=N) (i^2<=p, 2) with loop counts'''
    test = 'test1B'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    m, p = 2, 1
    if dbg == 0: print('.', end='')
    elif dbg > 1: print('m={} is {} prime ? yes'.format(m-1, p+1))
    tpt = 0
    while m <= N:
        tpt += 1
        p += 2
        if dbg > 1: print('m={} is {} prime ?'.format(m, p), end=' ')
        i = 3
        isPrime = 1
        pt = 0
        while i * i <= p:
            pt += 1
            tpt += 1
            if dbg > 1: print('    {} {}, i={} i*i={} p={}'.format(tpt, pt, i, i * i, p), end=' ')
            if p % i == 0:
                if dbg > 1: print('No divisible by {} => {}'.format(i, p//i))
                isPrime = 0
                break
            i += 2
#            print('    i={} i*i={} p={}'.format(i, i*i, p), end=' ')
        if isPrime == 1:
            if dbg > 1: print('yes')
#                print('n={} p={} isPrime={}'.format(n, p, isPrime))
            m += 1
    if dbg: print('\n{} {:,}th prime = {:,}'.format(test, N, p), end=' ')
    if dbg: print('(total steps={:,} avg # steps={})'.format(tpt, tpt//N), end=' ')

def test1C(args={'dbg': 1}):
    '''uses util.isPrime() for odd #s >= 3'''
    test = 'test3'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    n, p = 2, 3
    while 1:
        if util.isPrime(p):
#            print('{} {}'.format(n, p))
            n += 1 
        if n == N+1: break
        p += 2
    if dbg: print('\n{} {:,}th prime = {:,}'.format(test, N, p), end=' ')

#######
def test2(args={'dbg': 1}):
    '''uses util.isPrime() for odd #s >= 3 and a generator'''
    test = 'test2'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    nth(test, N, genPrimes(), dbg)
    
def nth(test, N, gen, dbg=1):
    for i in range(N - 1):
        p = next(gen)
#        print('{}'.format(p))
    if dbg: print('\n{} {:,}th prime = {:,}'.format(test, N, next(gen)), end=' ')

def genPrimes():
    yield 2
    i = 3
    while True:
        if util.isPrime(i):
            yield i
        i += 2
#######
def test3(args={'dbg': 1}):
    '''uses a Sieve on a list of primes tests if any are a factor until the last prime^2 > n'''
    test = 'test3'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    n = 3
    primes = [2]
    while len(primes) < N:
        if dbg > 1: print('n={} {} {}'.format(n, primes, len(primes)))
        for p in primes:
            if dbg > 1: print('    {} {} p={}, (p * p)={}'.format(tpt, pt, p, p * p))
            if p * p > n:
                if dbg > 1: print('        p * p > n, {} * {} > {}, {} is PRIME'.format(p, p, n, n))
                primes.append(n)
                break
            if n % p == 0:
                if dbg > 1: print('        n % p == 0, {} % {} == 0, {} is NOT'.format(n, p, n))
                break
        n += 1
    if dbg > 1: print('{} {}'.format(primes, len(primes)))
    if dbg: print('\n{} {:,}th prime = {:,}'.format(test, N, primes[N-1]), end=' ')
    
def test3B(args={'dbg': 1}):
    '''uses a Sieve on a list of primes tests if any are a factor until the last prime^2 > n with loop counts'''
    test = 'test3B'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    n = 3
    primes = [2]
    tpt = 0
    while len(primes) < N:
        if dbg > 1: print('n={} {} {}'.format(n, primes, len(primes)))
        pt = 0
        for p in primes:
            pt += 1
            tpt += 1
            if dbg > 1: print('    {} {} p={}, (p * p)={}'.format(tpt, pt, p, p * p))
            if p * p > n:
                if dbg > 1: print('        p * p > n, {} * {} > {}, {} is PRIME'.format(p, p, n, n))
                primes.append(n)
                break
            if n % p == 0:
                if dbg > 1: print('        n % p == 0, {} % {} == 0, {} is NOT'.format(n, p, n))
                break
        n += 1
    if dbg > 1: print('{} {}'.format(primes, len(primes)))
    if dbg: print('\n{} {:,}th prime = {:,}'.format(test, N, primes[N-1]), end=' ')
    if dbg: print('(total steps={:,} avg # steps={})'.format(tpt, tpt//N), end=' ')
    
def test3C(args={'dbg': 1}):
    '''uses a Sieve on a list of primes tests if any are a factor until the last prime > sqrt(n)'''
    test = 'test3C'
    dbg = 1
#    print('{} args={}'.format(test, args))
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']   
    if dbg == 0: print('.', end='')
    n = 3
    primes = [2]
    while len(primes) < N:
        max = math.sqrt(n)
        for p in primes:
            if p > max:
                primes.append(n)
                break
            if n % p == 0: break
        n += 1
    if dbg: print('\n{} {:,}th prime = {:,}'.format(test, N, primes[N-1]), end=' ')
#    print('{}'.format(primes))
    
if __name__ == "__main__":
    main()
    
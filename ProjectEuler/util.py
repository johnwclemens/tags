import sys, timeit, inspect
import cmdArgs

def isPrime(N):
#    print('is {} prime ?'.format(N), end=' ')
    if N == 2:
#        print('yes')
        return 1
    elif N < 2 or N % 2 == 0: 
#        print('No divisible by {} => {}'.format(2, int(N/2)))
        return 0
    i = 3
    while i * i <= N:
        if N % i == 0:
#            print('No divisible by {} => {}'.format(i, int(N/i)))
            return 0
        i += 2
#    print('yes')
    return 1

def usage(u, a1, a2):
    u(a1, a2)
    fs = inspect.getmembers(a2['o'], inspect.isfunction)
    for f in fs:
        if f[0].count('test') > 0:
            print("{} '{}'".format(f[0], f[1].__doc__))
    exit()
    
def runTests(a1={}, a2={}, dbg=0):
    if dbg > 2: print('a1={}'.format(a1))
    if dbg > 2: print('a2={}'.format(a2))
    if 'P' in a1: P = a1['P']
    if 'M' in a1: M = a1['M']
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    if 'o' in a2: o = a2['o']
    if 'u' in a2: u = a2['u']
    argMap = {}
    argMap = cmdArgs.parseCmdLine(dbg=0)
    if dbg > 2: print('argMap={}'.format(argMap))
    if '' in argMap:
        if len(argMap['']) == 1 and argMap[''][0] == '?': usage(u, a1, a2)
        if len(argMap['']) > 0: N = int(argMap[''][0])
        if len(argMap['']) > 1: n = int(argMap[''][1])
        if len(argMap['']) > 2: r = int(argMap[''][2])
        if len(argMap['']) > 3: dbg = int(argMap[''][3])
        if len(argMap['']) > 4:
            t = []
            for i in range(4, len(argMap[''])):
                t.append(argMap[''][i])
    else:
        if 'P' in argMap and len(argMap['P']) > 0:
            P = []
            for i in range(0, len(argMap['P'])):
                P.append(int(argMap['P'][i]))
        if 'M' in argMap and len(argMap['M']) > 0: M = int(argMap['M'][0])
        if 'N' in argMap and len(argMap['N']) > 0: N = int(argMap['N'][0])
        if 'n' in argMap and len(argMap['n']) > 0: n = int(argMap['n'][0])
        if 'r' in argMap and len(argMap['r']) > 0: r = int(argMap['r'][0])
        if 'd' in argMap and len(argMap['d']) > 0: dbg = int(argMap['d'][0])
        if 't' in argMap and len(argMap['t']) > 0:
            t = []
            for i in range(0, len(argMap['t'])):
                t.append(argMap['t'][i])
    if 'P' in a1: a1['P'] = P
    if 'M' in a1: a1['M'] = M
    a1['N'] = N
    tf = []
    for i in t:
        ts = 'test{}'.format(i)
        tf.append(getattr(o, ts))
    if dbg > 2: print('N={} n={} r={} t={}'.format(N, n, r, t))
    run(tf, n, r, a1, dbg)
        
def run(ts, n=0, r=3, a=[], dbg=0):
    if dbg > 2: print('a={}'.format(a))
    for t in ts:
        T = t.__name__
        if n < 1:
            if n == 0: a['dbg'] = 0
            elif n == -1: a['dbg'] = dbg
            print("\nRun {} n={} r={} '{}'".format(T, n, r, t.__doc__), flush=True)
            t(a)
        else:
            a['dbg'] = 0
            p = T + '({})'.format(a)
            a['dbg'] = dbg
            d = T + '({})'.format(a)
            s = 'from __main__ import {}; {}'.format(T, d)
            print("Run {} n={:,} r={} '{}'".format(T, n, r, t.__doc__), flush=True)
            if n   ==       1000: u, q = 'msec/loop', ' @'
            elif n ==    1000000: u, q = 'usec/loop', ' @'
            elif n == 1000000000: u, q = 'nsec/loop', ' @'
            else:              u, q = 'sec', ''
            x = timeit.repeat('{}'.format(p), setup=s, repeat=r, number=n)
            print('    {} n={:,} loops{} ('.format(T, n, q), end=' ')
            for i in x: print('{:8.4}'.format(i), end=' ')
            print(') {}  MIN = {:,} usec/loop'.format(u, int(min(x)*1000000/n)))

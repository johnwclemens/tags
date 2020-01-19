import sys, os.path, math, timeit, numpy
from functools import reduce
from operator import mul
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../'))
import cmdArgs, util

data = \
'''\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48\
'''
grid = data.splitlines() # ~ 2usec

def main():
    print('''    In the 20*20 grid below, four numbers along a diagonal line have been marked in red.
    The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20*20 grid?''')
    N = 20
    M = 4
    n = 1
    r = 1
    t = [1]
    o = sys.modules[__name__]
    u = usage
    util.runTests({'N': N, 'M': M}, {'n': n, 'r': r, 't': t, 'o': o, 'u': u}, dbg=1)

def usage(a1={}, a2={}):
    if 'M' in a1: M = a1['M']
    if 'N' in a1: N = a1['N']
    if 'n' in a2: n = a2['n']
    if 'r' in a2: r = a2['r']
    if 't' in a2: t = a2['t']
    print("    Usage: 'N n r t' where N ({}) #lines, M () #cells, n ({}) loops, r ({}) repeats, t ({}) test#".format(N, M, n, r, t))
    
def print2da(a, reason=''):
    if len(reason) > 0: print('\n{}'.format(reason))
#    N = len(a)
#    [[print(a[i][j], end=' ') for j in range(N)] for i in range(N)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print('{:2} '.format(a[i][j]), end= '')
        print()

def docstring(docstr, sep="\n"):
    '''this is what the Decorator does: Prepend to a function's docstring.'''
    def _decorator(func):
        if func.__doc__ == None:
            func.__doc__ = docstr
        else:
            func.__doc__ = sep.join([docstr, func.__doc__])
        return func
    return _decorator
    
def findMaxProdH(m, test, M, a, dir, dbg):
    p, P = 0, []
    for i in range(len(a)):
        h = []
        for j in range(len(a[i]) - M):
            h = a[i][j:j+M]
            q = 1
            for e in h:
                q *= e
            if q > p:
                P = h
                p = q
                I, J = i, j
#            if dbg: print('{} {:,} {:,}'.format(h, q, p))
    if dbg > 1: print("{} greatest product of {} cells '{}' [{}][{}] = {} = {:,}".format(test, M, dir, I, J, P, p))
    if len(m) == 0 or p > m[4]: m = [dir, I, J, P, p]
    return m

def findMaxProdV(m, test, M, a, dir, dbg):
    p, P = 0, []
    for j in range(len(a)):
        for i in range(len(a[j]) - M+1):
            v, q = [], 1
            for k in range(i, i+M):
                v.append(int(a[k][j]))
            for e in v:
                q *= e
            if q > p:
                P = v
                p = q
                I, J = i, j
#            print('({},{}) {} {:,} {:,}'.format(i, j, v, q, p))
#        print()
    if dbg > 1: print("{} greatest product of {} cells '{}' [{}][{}] = {} = {:,}".format(test, M, dir, I, J, P, p))
    if len(m) == 0 or p > m[4]: m = [dir, I, J, P, p]
    return m

#test1A greatest product of 4 cells 'Horizontal' [8][10] = [78, 78, 96, 83] = 48,477,312
#test1A greatest product of 4 cells 'Vertical' [6][15] = [66, 91, 88, 97] = 51,267,216
#test1A greatest product of 4 cells 'Diaginal 1A' [5][9] = [84, 66, 66, 89] = 40,304,286
#test1A greatest product of 4 cells 'Diaginal 1B' [9][7] = [94, 99, 71, 61] = 32,565,456
#test1A greatest product of 4 cells 'Diaginal 2A' [12][1] = [89, 94, 97, 87] = 70,600,674
#test1A greatest product of 4 cells 'Diaginal 2B' [1][13] = [98, 93, 40, 85] = 30,987,600
#test1A greatest product of 4 cells in any direction is 'Diaginal 2A' [12][1] = [89, 94, 97, 87] = 70,600,674
#test1B greatest product of 4 cells 'Horizontal' [8][10] = [78, 78, 96, 83] = 48,477,312
#test1B greatest product of 4 cells 'Vertical' [15][6] = (66, 91, 88, 97) = 51,267,216
#test1B greatest product of 4 cells 'Diaginal 1A' [9][7] = [94, 99, 71, 61] = 40,304,286
#test1B greatest product of 4 cells 'Diaginal 1B' [5][9] = [84, 66, 66, 89] = 32,565,456
#test1B greatest product of 4 cells 'Diaginal 2A' [3][1] = [87, 97, 94, 89] = 70,600,674
#test1B greatest product of 4 cells 'Diaginal 2B' [2][13] = [85, 40, 93, 98] = 30,987,600
#test1B greatest product of 4 cells in any direction is 'Diaginal 2A' [3][1] = [87, 97, 94, 89] = 70,600,674
"""
def testB2(args={'dbg': 1}):
    '''a = [[0]*(N+M-1)]*3 + [[int(grid[i].split()[j]) j(N)] + [0,0,0] i(N)] + [[0]*(N+M-1)]*3'''
    test = 'testB2'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = [[0]*(N+M-1)]*3 + [[int(grid[i].split()[j]) for j in range(N)] + [0, 0, 0] for i in range(N)] + [[0]*(N+M-1)]*3
    if dbg: print2da(a)

def testC2(args={'dbg': 1}):
    '''a = [[0]*(N+M-1)]*3 + [[int(x) x in g.split()) + [0,0,0] g(grid)] + [[0]*(N+M-1)]*3'''
    test = 'testC2'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = [[0]*(N+M-1)]*3 + [[int(x) for x in g.split()] + [0, 0, 0] for g in grid] + [[0]*(N+M-1)]*3
    if dbg: print2da(a)
"""

def testA(args={'dbg': 0}):
    '''testA: i(len(grid)) a.append(grid[i].split()) j(len(grid[i]) a[i][j] = int(a[i][j])'''
    dbg = 0
    if 'dbg' in args: dbg = args['dbg']
    a = []
    for i in range(len(grid)):
        a.append(grid[i].split())
        for j in range(len(a[i])):
            a[i][j] = int(a[i][j])
    if dbg > 2: print2da(a)
    return a

"""
def testA1(args={'dbg': 1}):
    '''i(N) a.append(grid[i].split()) j(N) a[i][j] = int(a[i][j])'''
    dbg = 0
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    a = []
    for i in range(N):
        a.append(grid[i].split())
        for j in range(N):
            a[i][j] = int(a[i][j])
    if dbg > 2: print2da(a)
    return a
"""

def testB(args={'dbg': 1}):
    '''a = [[int(grid[i].split()[j]) j(N)] i(N)]'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = [[int(grid[i].split()[j]) for j in range(len(grid))] for i in range(len(grid))]
    if dbg > 2: print2da(a)
    return a

def testC(args={'dbg': 1}):
    '''a = [[int(x) for x in g.split()] for g in grid]'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = [[int(x) for x in g.split()] for g in grid]
    if dbg > 2: print2da(a)
    return a

def testD(args={'dbg': 1}):
    '''testD(): [a = list(map(int, g.split()) g(grid)]'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = [list(map(int, g.split())) for g in grid]
    if dbg > 2: print2da(a)
    return a

def testE(args={'dbg': 1}):
    '''a = list(map(lambda x:list(map(int, x.split())), grid))'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = list(map(lambda x:list(map(int, x.split())), grid))
    if dbg > 2: print2da(a)
    return a

def testF(args={'dbg': 1}):
    '''a = list(map(lambda x:list(map(int, x)), list(map(lambda x:x.split(), grid))))'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = list(map(lambda x:list(map(int, x)), list(map(lambda x:x.split(), grid))))
    if dbg > 2: print2da(a)
    return a

def testG(args={'dbg': 1}):
    '''c = testB(): [[0]*(N+M-1)]*3 + [[int(grid[i].split()[j]) for j in range(N)] + [0,0,0] for i in range(N)] + [[0]*(N+M-1)]*3'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    m = 1
    c = [[0]*(N+M-1)]*3 + [[int(grid[i].split()[j]) for j in range(N)] + [0,0,0] for i in range(N)] + [[0]*(N+M-1)]*3
    if dbg > 2: print2da(c)
    return c

def testH(args={'dbg': 1}):
    '''c = testC(): m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] n(M)]) x(N) y(M-1,N+M-1) d in ((0,1),(1,0),(1,1),(-1,1))])'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    m = 1
    c = [[0]*(N+M-1)]*3 + [[int(x) for x in g.split()] + [0,0,0] for g in grid] + [[0]*(N+M-1)]*3
    if dbg > 2: print2da(c)
    return c

def testQ(args={'dbg': 1}):
    '''testQ(ONE-DIM): b = data.replace("\\n"," ") b = list(map(int, b.split())) ONE-DIM'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    b = data.replace("\n"," ")
    b = list(map(int, b.split()))
    if dbg > 2: print(b)
    return b

def testR(args={'dbg': 1}):
    '''testR(ONE-DIM): b = data.replace("\\n"," ") b = b.split() Does NOT call int() ONE-DIM'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    b = data.replace("\n"," ")
    b = b.split()
    if dbg > 2: print(b)
    return b

def testS(args={'dbg': 1}):
    '''testS(ONE-DIM): d=802229738...89196748 b=[0]*N*N i(N*N-1,-1,-1) b[i]=d%100 d//=100  ONE-DIM'''
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    d = 8022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748
    b = [0] * N * N
    for i in range(N*N-1, -1, -1):
        b[i] = d % 100
        d //= 100
    if dbg > 2: print(b)
    return b

##########################################################################################################################

def test0A(args={'dbg': 1}):
    ''''''
    test = 'test0A'
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = [list(map(int, g.split())) for g in grid]
    m1 = m2 = m3 = m4 = 1
#    '''
    if dbg > 2: print('Horizontal')
    if dbg > 2: print2da(a)
    for i in range(N):
        for j in range(N-M+1):
            m1 = max(m1, reduce(lambda x,y:x*y, a[i][j:j+M]))
            if dbg >2: print('[{}][{}]{}'.format(i, j, a[i][j:j+M]), end=' ')
        if dbg >2: print()
#    '''
    ###############
    a = list(zip(*a)) # transpose the orig to avoid creating another instance
    if dbg > 2: print('Vertical')
    if dbg > 2: print2da(a)
    for i in range(N):
        for j in range(N-M+1):
            m2 = max(m2, reduce(lambda x,y:x*y, a[i][j:j+M]))
            if dbg >2: print('[{}][{}]{}'.format(i, j, a[i][j:j+M]), end=' ')
        if dbg >2: print()
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

def test0B(args={'dbg': 1}):
    ''''''
    test = 'test0B'
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    a = [list(map(int, g.split())) for g in grid]
    m1 = m2 = m3 = m4 = 1
    '''
    if dbg > 2: print('Horizontal')
    if dbg > 2: print2da(a)
    for i in range(N):
        for j in range(N-M+1):
            m1 = max(m1, reduce(lambda x,y:x*y, a[i][j:j+M]))
            if dbg >2: print('[{}][{}]{}'.format(i, j, a[i][j:j+M]), end=' ')
        if dbg >2: print()
    '''
    ###############
    if dbg > 2: print('Vertical')
    if dbg > 2: print2da(a)
    for j in range(N):
        for i in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(a[i+k][j])
            if dbg > 2: print('[{}][{}]{}'.format(i, j, tmp), end=' ')
            m2 = max(m2, reduce(lambda x,y:x*y, tmp))
        if dbg > 2: print()
    ###############
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testD.__doc__)
def test1A(args={'dbg': 1}):
    '''h = testD(): m = findMaxProdH(h) m = findMaxProdV(h) findMaxProdV(d1A, d1B, d2A, d2B)'''
    test = 'test1A'
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m, dir = [], 'Horizontal'
    h = testD()
#    for i in range(N):
#        h.append(grid[i].split())
#        for j in range(N):
#            h[i][j] = int(h[i][j])
    if dbg > 2: print2da(h, dir)
    m = findMaxProdH(m, test, M, h, dir, dbg)
    
    dir = 'Vertical'
    # reuse the orig but call findMaxProdV() to avoid creating another instance
    if dbg > 3: print2da(h, dir)
    m = findMaxProdV(m, test, M, h, dir, dbg)

# > 0,0 0,1 0,2 0,3 0,4 ... 0,N
# >     1,1 1,2 1,3 1,4 ... 1,N
# >         2,2 2,3 2,4 ... 2,N
# >             3,3 3,4 ... 3,N
# >                         N,N
    d1A, dir = [], 'Diaginal 1A'
    for i in range(N):
        tmp = []
        for j in range(i, N):
            tmp.append('{}'.format(h[i][j]))
        d1A.append(tmp)
    if dbg > 3: print2da(d1A, dir)
    m = findMaxProdV(m, test, M, d1A, dir, dbg)

# > 0,0
# > 1,0 1,1
# > 2,0 2,1 2,2
# > 3,0 3,1 3,2 3,3
# > N,0 N,1 N,2 N,3 N,4 ... N,N
    d1B, dir = [], 'Diaginal 1B'
    for j in range(N):
        tmp = []
        for i in range(j, N):
            tmp.append('{}'.format(h[i][j]))
        d1B.append(tmp)
    if dbg > 3: print2da(d1B, dir)
    m = findMaxProdV(m, test, M, d1B, dir, dbg)

# < 0,0 0,1 0,2 ... 0,N-3 0,N-2 0,N-1 0,N
# < 1,0 1,1 1,2 ... 1,N-3 1,N-2 1,N-1
# < 2,0 2,1 2,2 ... 2,N-3 2,N-2
# < 3,0 3,1 3,2 ... 3,N-3
# < N,0
    d2A, dir = [], 'Diaginal 2A'
    for i in range(N):
        tmp = []
        for j in range(N-i-1, -1, -1):
            tmp.append('{}'.format(h[i][j]))
        d2A.append(tmp)
    if dbg > 3: print2da(d2A, dir)
    m = findMaxProdV(m, test, M, d2A, dir, dbg)

#                                          0,N
#                                    1,N-1 1,N
#                              2,N-2 2,N-1 2,N
#        N-1,1 N-1,2 ... N,N-3 N,N-2 N,N-1 N,N
#    N,0   N,1   N,2 ... N,N-3 N,N-2 N,N-1 N,N
    d2B, dir = [], 'Diaginal 2B'
    for j in range(N-1, -1, -1):
        tmp = []
        for i in range(N-j-1, N):
            tmp.append('{}'.format(h[i][j]))
        d2B.append(tmp)
    if dbg > 3: print2da(d2B, dir)
    m = findMaxProdV(m, test, M, d2B, dir, dbg)
    if dbg: print("{} greatest product of {} cells in any direction is '{}' [{}][{}] = {} = {:,}".format(test, M, m[0], m[1], m[2], m[3], m[4]))
    
@docstring('Uses: ' + testD.__doc__)
def test1B(args={'dbg': 1}):
    '''h = testD(): m = findMaxProdH(h) h = list(zip(*h)) m = findMaxProdH(h) findMaxProdV(d1A, d1B, d2A, d2B)'''
    test = 'test1B'
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m, dir = [], 'Horizontal'
    h = testD()
#    for i in range(N):
#        h.append(grid[i].split())
#        for j in range(N):
#            h[i][j] = int(h[i][j])
    if dbg > 2: print2da(h, dir)
    m = findMaxProdH(m, test, M, h, dir, dbg)
    
    dir = 'Vertical'
    h = list(zip(*h)) # transpose the orig to avoid creating another instance
    if dbg > 3: print2da(h, dir)
    m = findMaxProdH(m, test, M, h, dir, dbg)

# > 0,0 0,1 0,2 0,3 0,4 ... 0,N
# >     1,1 1,2 1,3 1,4 ... 1,N
# >         2,2 2,3 2,4 ... 2,N
# >             3,3 3,4 ... 3,N
# >                         N,N
    d1A, dir = [], 'Diaginal 1A'
    for j in range(N):
        tmp = []
        for i in range(j, N):
            tmp.append('{}'.format(h[i][j]))
        d1A.append(tmp)
    if dbg > 3: print2da(d1A, dir)
    m = findMaxProdV(m, test, M, d1A, dir, dbg)

# > 0,0
# > 1,0 1,1
# > 2,0 2,1 2,2
# > 3,0 3,1 3,2 3,3
# > N,0 N,1 N,2 N,3 N,4 ... N,N
    d1B, dir = [], 'Diaginal 1B'
    for i in range(N):
        tmp = []
        for j in range(i, N):
            tmp.append('{}'.format((h[i][j])))
        d1B.append(tmp)
    if dbg > 3: print2da(d1B, dir)
    m = findMaxProdV(m, test, M, d1B, dir, dbg)

# < 0,0 0,1 0,2 ... 0,N-3 0,N-2 0,N-1 0,N
# < 1,0 1,1 1,2 ... 1,N-3 1,N-2 1,N-1
# < 2,0 2,1 2,2 ... 2,N-3 2,N-2
# < 3,0 3,1 3,2 ... 3,N-3
# < N,0
    d2A, dir = [], 'Diaginal 2A'
    for i in range(N):
        tmp = []
        for j in range(N-i-1, -1, -1):
            tmp.append('{}'.format((h[i][j])))
        d2A.append(tmp)
    if dbg > 3: print2da(d2A, dir)
#    m = findMaxProdV2(m, test, M, d2A, dir, dbg)
    m = findMaxProdV(m, test, M, d2A, dir, dbg)

#                                          0,N
#                                    1,N-1 1,N
#                              2,N-2 2,N-1 2,N
#        N-1,1 N-1,2 ... N,N-3 N,N-2 N,N-1 N,N
#    N,0   N,1   N,2 ... N,N-3 N,N-2 N,N-1 N,N
    d2B, dir = [], 'Diaginal 2B'
    for j in range(N-1, -1, -1):
        tmp = []
        for i in range(N-j-1, N):
            tmp.append('{}'.format(h[i][j]))
        d2B.append(tmp)
    if dbg > 3: print2da(d2B, dir)
#    m = findMaxProdV2(m, test, M, d2B, dir, dbg)
    m = findMaxProdV(m, test, M, d2B, dir, dbg)
    if dbg: print("{} greatest product of {} cells in any direction is '{}' [{}][{}] = {} = {:,}".format(test, M, m[0], m[1], m[2], m[3], m[4]))

    '''
    if dbg:
        print()
        n = N//2
        t = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append('{}{}'.format(i, j))
            t.append(tmp)
    print2da(t, 't')
    d1 = []
    print()
    for i in range(n):
        tmp = []
        for j in range(i, n):
            tmp.append('{}{}'.format(i, j))
        d1.append(tmp)
    print2da(d1, 'd1')
    d2 = []
    print()
    for j in range(n):
        tmp = []
        for i in range(j, n):
            tmp.append('{}{}'.format(i, j))
        d2.append(tmp)
    print2da(d2, 'd2')
    '''

@docstring('Uses: ' + testD.__doc__)
def test2A(args={'dbg': 1}):
    '''h = testD(): m = findMaxProdH(h) m findMaxProdV(v, d1A, d1B, d2A, d2B)'''
    test = 'test2A'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m, dir = [], 'Horizontal'
    h = testD()
#    h = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(h, dir)
    m = findMaxProdH(m, test, M, h, dir, dbg)

    dir = 'Vertical'
    v = [[int(grid[j].split()[i]) for i in range(N)] for j in range(N)]
    if dbg > 3: print2da(v, dir)
    m = findMaxProdV(m, test, M, v, dir, dbg)
    
    dir = 'Diaginal 1A'
    d1A = [[int(grid[i].split()[j]) for j in range(i, N)] for i in range(N)]
    if dbg > 3: print2da(d1A, dir)
    m = findMaxProdV(m, test, M, d1A, dir, dbg)

    dir = 'Diaginal 1B'
    d1B = [[int(grid[i].split()[j]) for i in range(j, N)] for j in range(N)]
    if dbg > 3: print2da(d1B, dir)
    m = findMaxProdV(m, test, M, d1B, dir, dbg)

    dir = 'Diaginal 2A'
    d2A = [[int(grid[i].split()[j]) for j in range(N-i-1, -1, -1)] for i in range(N)]
    if dbg > 3: print2da(d2A, dir)
    m = findMaxProdV(m, test, M, d2A, dir, dbg)

    dir = 'Diaginal 2B'
    d2B = [[int(grid[i].split()[j]) for i in range(N-j-1, N)] for j in range(N-1, -1, -1)]
    if dbg > 3: print2da(d2B, dir)
    m = findMaxProdV(m, test, M, d2B, dir, dbg)
    if dbg: print("{} greatest product of {} cells in any direction is '{}' [{}][{}] = {} = {:,}".format(test, M, m[0], m[1], m[2], m[3], m[4]))

@docstring('Uses: ' + testD.__doc__)
def test2B(args={'dbg': 1}):
    '''h = testD(): m = findMaxProdH(h) v = list(zip(*h)) m = findMaxProdV(v, d1A, d1B, d2A, d2B)'''
    test = 'test2B'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m, dir = [], 'Horizontal'
    h = testD()
#    h = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(h, dir)
    m = findMaxProdH(m, test, M, h, dir, dbg)

    dir = 'Vertical'
    v = list(zip(*h)) # transpose the orig to avoid creating another instance
    if dbg > 3: print2da(v, dir)
    m = findMaxProdH(m, test, M, v, dir, dbg)
    
    dir = 'Diaginal 1A'
    d1A = [[int(grid[i].split()[j]) for j in range(i, N)] for i in range(N)]
    if dbg > 3: print2da(d1A, dir)
    m = findMaxProdV(m, test, M, d1A, dir, dbg)

    dir = 'Diaginal 1B'
    d1B = [[int(grid[i].split()[j]) for i in range(j, N)] for j in range(N)]
    if dbg > 3: print2da(d1B, dir)
    m = findMaxProdV(m, test, M, d1B, dir, dbg)

    dir = 'Diaginal 2A'
    d2A = [[int(grid[i].split()[j]) for j in range(N-i-1, -1, -1)] for i in range(N)]
    if dbg > 3: print2da(d2A, dir)
    m = findMaxProdV(m, test, M, d2A, dir, dbg)

    dir = 'Diaginal 2B'
    d2B = [[int(grid[i].split()[j]) for i in range(N-j-1, N)] for j in range(N-1, -1, -1)]
    if dbg > 3: print2da(d2B, dir)
    m = findMaxProdV(m, test, M, d2B, dir, dbg)
    if dbg: print("{} greatest product of {} cells in any direction is '{}' [{}][{}] = {} = {:,}".format(test, M, m[0], m[1], m[2], m[3], m[4]))

@docstring('Uses: ' + testD.__doc__)
def test3A(args={'dbg': 1}):
    '''a = testD(): i(N) j(N) if j<=N-M: m1=max(m1, reduce(lambda x,y:x*y, a[i][j:j+M] k(M)]) if i<=N-M reduce(lambda x,y:x*y, [a[i+k][j] k(M)])'''
    test = 'test3A'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    a = testD()
#    a = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(a)
    m1 = m2 = m3 = m4 = 1
    for i in range(N):
        for j in range(N):
            if j <= N-M:
                m1 = max(m1, reduce(lambda x,y:x*y, [a[i][j+k] for k in range(M)]))
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m1 = {:,}'.format(i,j,a[i][j], i,j+1,a[i][j+1], i,j+2,a[i][j+2], i,j+3,a[i][j+3], m1))
            if i <= N-M:
                m2 = max(m2, reduce(lambda x,y:x*y, [a[i+k][j] for k in range(M)]))
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m2 = {:,}'.format(i,j,a[i][j], i+1,j,a[i+1][j], i+2,j,a[i+2][j], i+3,j,a[i+3][j], m2))
            if i <= N-M and j <= N-M:
                m3 = max(m3, reduce(lambda x,y:x*y, [a[i+k][j+k] for k in range(M)]))
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m3 = {:,}'.format(i,j,a[i][j], i+1,j+1,a[i+1][j+1], i+2,j+2,a[i+2][j+2], i+3,j+3,a[i+3][j+3], m3))
            if i <= N-M and j >= M-1:
                m4 = max(m4, reduce(lambda x,y:x*y, [a[i+k][j-k] for k in range(M)]))
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m4 = {:,}'.format(i,j,a[i][j], i+1,j-1,a[i+1][j-1], i+2,j-2,a[i+2][j-2], i+3,j-3,a[i+3][j-3], m4))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testD.__doc__)
def test3B(args={'dbg': 1}):
    '''a = testD(): i(N) j(N) if j<=N-M: m1 = max(m1, reduce(lambda x,y:x*y, a[i][j:j+M]) if i<=N-M reduce(lambda x,y:x*y, [e[j] for e in a[i:i+M]])'''
    test = 'test3B'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    a = testD()
#    a = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(a)
    m1 = m2 = m3 = m4 = 1
    for i in range(N):
        for j in range(N):
            if j <= N-M:
                m1 = max(m1, reduce(lambda x,y:x*y, a[i][j:j+M]))
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m1 = {:,}'.format(i,j,a[i][j], i,j+1,a[i][j+1], i,j+2,a[i][j+2], i,j+3,a[i][j+3], m1))
            if i <= N-M:
#                m2 = max(m2, reduce(lambda x,y:x*y, a[i:i+M][j]))
                m2 = max(m2, reduce(lambda x,y:x*y, [e[j] for e in a[i:i+M]]))
                if dbg > 3: print('[{:02}][{:02}]{:02} [{:02}][{:02}]{:02} [{:02}][{:02}]{:02} [{:02}][{:02}]{:02} m2 = {:,}'.format(i,j,a[i][j], i+1,j,a[i+1][j], i+2,j,a[i+2][j], i+3,j,a[i+3][j], m2))
            if i <= N-M and j <= N-M:
                m3 = max(m3, reduce(lambda x,y:x*y, [a[i+k][j+k] for k in range(M)]))
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m3 = {:,}'.format(i,j,a[i][j], i+1,j+1,a[i+1][j+1], i+2,j+2,a[i+2][j+2], i+3,j+3,a[i+3][j+3], m3))
            if i <= N-M and j >= M-1:
                m4 = max(m4, reduce(lambda x,y:x*y, [a[i+k][j-k] for k in range(M)]))
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m4 = {:,}'.format(i,j,a[i][j], i+1,j-1,a[i+1][j-1], i+2,j-2,a[i+2][j-2], i+3,j-3,a[i+3][j-3], m4))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testD.__doc__)
def test3C(args={'dbg': 1}):
    '''a = testD(): i(N) j(N) if j<=N-M: m1=max(m1,a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]) if i<=N-M: m2=max(m2,a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j])'''
    test = 'test3C'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    a = testD()
#    a = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(a)
    m1 = m2 = m3 = m4 = 1
    for i in range(N):
        for j in range(N):
            if j <= N-M:
                m1 = max(m1, a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3])
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m1 = {:,}'.format(i,j,a[i][j], i,j+1,a[i][j+1], i,j+2,a[i][j+2], i,j+3,a[i][j+3], m1))
            if i <= N-M:
                m2 = max(m2, a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j])
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m2 = {:,}'.format(i,j,a[i][j], i+1,j,a[i+1][j], i+2,j,a[i+2][j], i+3,j,a[i+3][j], m2))
            if i <= N-M and j <= N-M:
                m3 = max(m3, a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3])
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m3 = {:,}'.format(i,j,a[i][j], i+1,j+1,a[i+1][j+1], i+2,j+2,a[i+2][j+2], i+3,j+3,a[i+3][j+3], m3))
            if i <= N-M and j >= M-1:
                m4 = max(m4, a[i][j] * a[i+1][j-1] * a[i+2][j-2] * a[i+3][j-3])
                if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m4 = {:,}'.format(i,j,a[i][j], i+1,j-1,a[i+1][j-1], i+2,j-2,a[i+2][j-2], i+3,j-3,a[i+3][j-3], m4))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testD.__doc__)
def test4(args={'dbg': 1}):
    '''a = testD(): i(N) j(N-M+1) if a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3] > m1: m1=a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3] if a[j][i]*a[j+1][i]*a[j+2][i]*a[j+3][i] > m2: m2=a[j][i]*a[j+1][i]*a[j+2][i]*a[j+3][i]'''
    test = 'test4'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m1, m2, m3, m4 = 1, 1, 1, 1
    a = testD()
#    a = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(a)
    for i in range(N):
        for j in range(N-M+1):
            if a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3] > m1: m1 = a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3]
            if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m1={:,}'.format(i,j,a[i][j], i,j+1,a[i][j+1], i,j+2,a[i][j+2], i,j+3,a[i][j+3], m1))
            if a[j][i] * a[j+1][i] * a[j+2][i] * a[j+3][i] > m2: m2 = a[j][i] * a[j+1][i] * a[j+2][i] * a[j+3][i]
            if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m2={:,}'.format(j,i,a[j][i], j+1,i,a[j+1][i], j+2,i,a[j+2][i], j+3,i,a[j+3][i], m2))
    for i in range(N-M+1):
        for j in range(N-M+1):
            if a[i][j]     * a[i+1][j+1]   * a[i+2][j+2]   * a[i+3][j+3]   > m3: m3 = a[i][j]     * a[i+1][j+1]   * a[i+2][j+2]   * a[i+3][j+3]
            if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m3={:,}'.format(i,j,a[i][j], i+1,j+1,a[i+1][j+1], i+2,j+2,a[i+2][j+2], i+3,j+3,a[i+3][j+3], m3))
            if a[N-1-i][j] * a[N-2-i][j+1] * a[N-3-i][j+2] * a[N-4-i][j+3] > m4: m4 = a[N-1-i][j] * a[N-2-i][j+1] * a[N-3-i][j+2] * a[N-4-i][j+3]
            if dbg > 3: print('({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} ({:2},{:2}){:2} m4={:,}'.format(N-1-i,j,a[N-1-i][j], N-2-i,j+1,a[N-2-i][j+1], N-3-i,j+2,a[N-3-i][j+2], N-4-i,j+3,a[N-4-i][j+3], m4))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testD.__doc__)
def test5(args={'dbg': 1}):
    '''rows = testD(): for row in rows: prods.extend([y[0]*y[1]*y[2]*y[3] y in [row[i:i+4] i(N-M+1)]]) [[rows[i][j] i(N)] j(N)]'''
    test = 'test5'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    rows = testD()
#    rows = [list(map(int, g.split())) for g in grid]
    if dbg > 3: print('len = {} data:\n{}'.format(len(data), data))
    if dbg > 3: print('len = {} grid:\n{}'.format(len(grid), grid))
    rowproducts = []
    for row in rows:
        rowproducts.extend([y[0]*y[1]*y[2]*y[3] for y in [row[i:i+M] for i in range(N-M+1)]])
    if dbg > 3: print('h = {}'.format(rowproducts))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', max(rowproducts)))

    cols = [[rows[i][j] for i in range(N)] for j in range(N)]
    colproducts = []
    for col in cols:
        colproducts.extend([y[0]*y[1]*y[2]*y[3] for y in [col[i:i+M] for i in range(N-M+1)]])
    if dbg > 3: print('v = {}'.format(colproducts))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical', max(colproducts)))

    r_upper_rows = [[rows[i][j] for j in range(i, N)] for i in range(N)]
    upper_rdiags = [[x[i] for x in r_upper_rows[:-i]] for i in range(1, N)]
    r_lower_cols = [[cols[i][j] for j in range(i, N)] for i in range(N)]
    lower_rdiags = [[x[i] for x in r_lower_cols[:-i]] for i in range(1, N)]
    if dbg > 3:
        print('r_upper_rows:')
        fill = '   '
        [print('{}'.format(r)) for r in r_upper_rows]
        print('upper_rdiags:')
        [print('{}'.format(d)) for d in upper_rdiags]
        print('r_lower_cols:')
        [print('{}'.format(r)) for r in r_lower_cols]
        print('lower_rdiags:')
        [print('{}'.format(d)) for d in lower_rdiags]
    rdiags_all = upper_rdiags + lower_rdiags + [[rows[i][i] for i in range(N)]]

    rdiags = [x for x in rdiags_all if len(x) >= M]
    rdiagproducts = []
    for rdiag in rdiags:
        rdiagproducts.extend([y[0]*y[1]*y[2]*y[3] for y in [rdiag[i:i+M] for i in range(len(rdiag) - M-1)]])
    if dbg > 3: print('rd = {}'.format(rdiagproducts))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', max(rdiagproducts)))

    l_upper_rows = [[rows[i][j] for j in range(N-1-i, -1, -1)] for i in range(N)]
    upper_ldiags = [[x[i] for x in l_upper_rows[:-i]] for i in range(1, N)]
    l_lower_cols = [[cols[i][j] for j in range(N-1-i, N)] for i in range(N-1, -1, -1)]
    lower_ldiags = [[x[i] for x in l_lower_cols[:-i]] for i in range(1, N)]
    ldiags_all = upper_ldiags + lower_ldiags + [[rows[i][N-1-i] for i in range(N)]]

    ldiags = [x for x in ldiags_all if len(x) >= M]
    ldiagproducts = []
    for ldiag in ldiags:
        ldiagproducts.extend([y[0]*y[1]*y[2]*y[3] for y in [ldiag[i:i+M] for i in range(len(ldiag) - M-1)]])
    if dbg > 3: print('ld = {}'.format(ldiagproducts))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', max(ldiagproducts)))

    m = max([max(rowproducts), max(colproducts), max(rdiagproducts), max(ldiagproducts)])
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))
    
@docstring('Uses: ' + testB.__doc__)
def test6A(args={'dbg': 1}):
    '''a = testG(): m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] for n in range(M)]) for x in range(N) for y in range(M-1, N+M-1) for d in ((0,1),(1,0),(1,1),(-1,1))])'''
    test = 'test6A'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m = 1
    a = [[0]*(N+M-1)]*3 + [[int(grid[i].split()[j]) for j in range(N)] + [0,0,0] for i in range(N)] + [[0]*(N+M-1)]*3
    if dbg > 2:
        for g in a:
            for f in g:
                print('{:2}'.format(f), end= ' ')
            print()
#    m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] for n in range(M)]) for x in range(N) for y in range(M-1, N+M-1) for d in ((0,1),(1,0),(1,1),(-1,1))])
    m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] for n in range(M)]) for x in range(N) for y in range(M-1, N+M-1) for d in ((0,1),(1,0),(1,1),(-1,1))])
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testC.__doc__)
def test6B(args={'dbg': 1}):
    '''a = testH(): m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] for n in range(M)]) for x in range(N) for y in range(M-1, N+M-1) for d in ((0,1),(1,0),(1,1),(-1,1))])'''
    test = 'test6B'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m = 1
    a = [[0]*(N+M-1)]*3 + [[int(x) for x in g.split()] + [0,0,0] for g in grid] + [[0]*(N+M-1)]*3
    if dbg > 2:
        for g in a:
            for f in g:
                print('{:2}'.format(f), end= ' ')
            print()
    m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] for n in range(M)]) for x in range(N) for y in range(M-1, N+M-1) for d in ((0,1),(1,0),(1,1),(-1,1))])
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

def cell(x, y): return int(grid[y-1][(x-1)*3:(x-1)*3+2])
def allCombinations(N, M, dbg):
    L = 18
#    if dbg: print()
    for y in range(1, N+1):
        for x in range(1, L):
#            if dbg: print('({} {} {} {})'.format(cell(x, y), cell(x+1, y), cell(x+2, y), cell(x+3, y)), end=' ')
            yield [cell(x, y), cell(x+1, y), cell(x+2, y), cell(x+3, y)]
#    if dbg: print('\n')
    for x in range(1, N+1):
        for y in range(1, L):
#            if dbg: print('({} {} {} {})'.format(cell(x, y), cell(x, y+1), cell(x, y+2), cell(x, y+3)), end=' ')
            yield [cell(x, y), cell(x, y+1), cell(x, y+2), cell(x, y+3)]
#    if dbg: print('\n')
    for x in range(1, L):
        for y in range(1, L):
#            if dbg: print('({} {} {} {})'.format(cell(x, y), cell(x+1, y+1), cell(x+2, y+2), cell(x+3, y+3)), end=' ')
            yield [cell(x, y), cell(x+1, y+1), cell(x+2, y+2), cell(x+3, y+3)]
#    if dbg: print('\n')
    for x in range(M, N+1):
        for y in range(1, L):
#            if dbg: print('({} {} {} {})'.format(cell(x, y), cell(x-1, y+1), cell(x-2, y+2), cell(x-3, y+3)), end=' ')
            yield [cell(x, y), cell(x-1, y+1), cell(x-2, y+2), cell(x-3, y+3)]
def prod7(values):
    result = 1
    for value in values:
        result *= value
    return result
def allProducts(N, M, dbg):
    for fourNumbers in allCombinations(N, M, dbg):
        yield prod7(fourNumbers)
def test7(args={'dbg': 1}):
    '''cell(x, y): return int(grid[y-1][(x-1)*3:(x-1)*3+2]) y(1, N+1) x(1,L) yield [cell(x, y), cell(x+1, y), cell(x+2, y), cell(x+3, y)]'''
    test = 'test7'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m = 1
    m = max(allProducts(N, M, dbg))
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

def prod8(n):
    return(reduce(lambda x,y:x*y,n))
@docstring('Uses: ' + testD.__doc__)
def test8(args={'dbg': 1}):
    '''a = testD(): i(N) j(N-M+1) m1 = max(m1, prod([a[i][j+k] for k in range(M)]))'''
    test = 'test8'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m1, m2, m3, m4 = 1, 1, 1, 1
    a = testD()
#    a = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(a)
    for i in range(N): #horizontal lines
        for j in range(N-M+1):
            m1 = max(m1, reduce(lambda x,y:x*y, [a[i][j+k] for k in range(M)]))
    for i in range(N-M+1): #vertical lines
        for j in range(N): 
            m2 = max(m2, prod8([a[i+k][j] for k in range(M)]))
    for i in range(N-M+1): # diagonal lines
        for j in range(N-M+1):
            m3 = max(m3, prod8([a[i+k][j+k] for k in range(M)]))
    for i in range(N-M+1): # other diagonal 
        for j in range(M-1, N):
            m4 = max(m4, prod8([a[i+k][j-k] for k in range(M)]))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

def prod9(a, i, j, M, N):
    if j < N+1-M:               yield reduce(mul, [a[i][j+k]   for k in range(M)])
    if i < N+1-M:               yield reduce(mul, [a[i+k][j]   for k in range(M)])
    if i < N+1-M and j < N+1-M: yield reduce(mul, [a[i+k][j+k] for k in range(M)])
    if i < N+1-M and j > 2:     yield reduce(mul, [a[i+k][j-k] for k in range(M)])
    yield 0
@docstring('Uses: ' + testD.__doc__)
def test9(args={'dbg': 1}):
    '''a = testD(): m = max([max(list(prod9))) i(N) j(N)] prod9: if j<N-M+1 yield reduce(mul, [a[i][j+k] for k in range(M)])'''
    test = 'test9'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    a = testD()
#    a = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    if dbg > 2: print2da(a)
    m = max([max(list(prod9(a, i, j, M, N))) for i in range(N) for j in range(N)])
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testQ.__doc__)
def test10A(args={'dbg': 1}):
    '''b = testQ(): i(len(b)) if i%N<N-M+1: m1 = max(m1, reduce(lambda x,y:x*y, b[i:i+M]))'''
    test = 'test10A'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    b = testQ()
    if dbg > 2: print2da(b)
    m = m1 = m2 = m3 = m4 = 1
    for i in range(len(b)):
        if i % N < N-M+1:
            m1 = max(m1, reduce(lambda x,y:x*y, b[i:i+M]))
        if i < 360:
            m2 = max(m2, reduce(lambda x,y:x*y, b[i:i+61:N]))
        if i % N < N-M+1 and i < 360:
            m3 = max(m3, reduce(lambda x,y:x*y, b[i:i+64:N+1]))
        if i < 360 and 2 < i % N:
            m4 = max(m4, reduce(lambda x,y:x*y, b[i:i+61:N-1]))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testR.__doc__)
def test10B(args={'dbg': 1}): # int() is not called when parsing, but rather when computing the max products (array init is faster, but max products is much slower) calls int() more than once on each cell
    '''b = testR(): i(len(b)) if i%N<N-M+1: m1 = max(m1, reduce(lambda x,y:int(x)*int(y), b[i:i+M]))  ###  Calls int() more than once/node  ###'''
    test = 'test10B'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    b = testR()
    if dbg > 2: print2da(a)
    m = m1 = m2 = m3 = m4 = 1
    for i in range(len(b)):
        if i % N < N-M+1:
            m1 = max(m1, reduce(lambda x,y:int(x)*int(y), b[i:i+M]))
        if i < 360:
            m2 = max(m2, reduce(lambda x,y:int(x)*int(y), b[i:i+61:N]))
        if i % N < N-M+1 and i < 360:
            m3 = max(m3, reduce(lambda x,y:int(x)*int(y), b[i:i+64:N+1]))
        if i < 360 and 2 < i % N:
            m4 = max(m4, reduce(lambda x,y:int(x)*int(y), b[i:i+61:N-1]))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    m = max(m1, m2, m3, m4)
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testD.__doc__)
def test11(args={'dbg': 1}):
    '''a = testD(): prod = lambda s: reduce(lambda x,y:x*y, s) i(N-M) j(N-M) m1 = max(m1, prod(a[i][j:j+M])) m2 = max(m2, prod([d[j] for d in a[i:i+M]]))'''
    test = 'test11'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    a = testD()
#    a = [[int(grid[i].split()[j]) for j in range(N)] for i in range(N)]
    m1 = m2 = m3 = m4 = 0
    prod = lambda s: reduce(lambda x,y:x*y, s)
    for i in range(N-M+1):
        for j in range(N-M+1):
            m1 = max(m1, prod(a[i][j:j+M]))
            m2 = max(m2, prod([d[j] for d in a[i:i+M]]))
            m3 = max(m3, a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3])
            if j >= M-1 and i <= N-M+1:
                m4 = max(m4, a[i][j] * a[i+1][j-1] * a[i+2][j-2] * a[i+3][j-3])
    m = max(m1, m2, m3, m4)
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

def prod12A(a, i, j, dir = "up", reach = 4):
    product = a[i][j]
    for k in range(1, reach):
        if dir == "down" and i+k < len(a):
            product *= a[i+k][j]
        elif dir == "right" and j+k < len(a[i]):
            product *= a[i][j+k]
        elif dir == "diag_left" and i-k >= 0 and j-k >= 0:
            product *= a[i-k][j-k]
        elif dir == "diag_right" and i-k >= 0 and j+k < len(a[i]):
            product *= a[i-k][j+k]
    return product
def prod12B(n):
    return(reduce(lambda x,y:x*y,n))
@docstring('Uses: ' + testD.__doc__)
def test12A(args={'dbg': 1}):
    '''a = testD(): i(a) j(a[i]) prods.append(prod12A()) m = max(prods, key=lambda item:item[3])'''
    test = 'test12A'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    a = testD()
#    a = [list(map(int, g.split(''))) for g in grid]
    products = []
    for i, line in enumerate(a):
        for j, num in enumerate(line):
                for dir in ["down", "right", "diag_left", "diag_right"]:
                    products.append((i, j, dir, prod12A(a, i, j, dir)))
    m = max(products, key=lambda item:item[3])
    if dbg: print("{} greatest product of {} cells in any direction is '{}' [{}][{}] = [?] = {:,}".format(test, M, m[2], m[0], m[1], m[3]))

@docstring('Uses: ' + testD.__doc__)
def test12B(args={'dbg': 1}):
    '''a = testD(): i(a) j(a[i]) if j+M < len(a[i]): m1 = max(m1, prod12B(a[i][j:j+M]))'''
    pass
    test = 'test12B'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m1 = m2 = m3 = m4 = 0
    a = testD()
#    a = [list(map(int, g.split())) for g in grid]
#    prod = lambda s: reduce(lambda x,y:x*y, s)
#    prod = reduce(lambda x,y:x*y)
    for i, line in enumerate(a):
        for j, num in enumerate(line):
            if j+M < len(a[i]): m1 = max(m1, prod12B(a[i][j:j+M]))
            if i+M < len(a):    m2 = max(m2, prod12B(d[j] for d in a[i:i+M]))
#            if i-k >= 0 and j-k >= 0:        m3 = max(m3, a[i-k][j-k])
#            if i-k >= 0 and j+k < len(a[i]): m4 = max(m4, a[i-k][j+k])
    m = max(m1, m2, m3, m4)
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testQ.__doc__)
def test13A(args={'dbg': 1}):
    '''\
         b=testQ(): i(N*N) if i%N<N-M+1: m1=max(m1,b[i]*b[i+1]*b[i+2]*b[i+3])                                if i<N*N-N*(M-1): m2=max(m2,b[i]*b[i+N]*b[i+2*N]*b[i+3*N]) 
         if i%N<N-M+1 and i<N*N-N*(M-1): m3=max(m3,b[i]*b[i+N+1]*b[i+2*N+2]*b[i+3*N+3]) j=N*N-1-i if i%N>=M-1 and j>(M-1)*N-1: m4=max(m4,b[j]*b[j-N+1]*b[j-2*N+2]*b[j-3*N+3])'''
    test = 'test13A'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
    m1 = m2 = m3 = m4 = 0
    b = testQ(args={'dbg':dbg})
    if dbg > 2:
        for i in range(N*N):
            print('{:2}'.format(b[i]), end=' ')
            if (i + 1) % N == 0: print()
    for i in range(N*N):
        if i % N < N-M+1:
            m1 = max(m1, b[i] * b[i+1] * b[i+2] * b[i+3])
#            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(i, b[i], i+1, b[i+1], i+2, b[i+2], i+3, b[i+3]), end=' ')
        if i < N*N - N*(M-1):
            m2 = max(m2, b[i] * b[i+N] * b[i+2*N] * b[i+3*N])
#            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(i, b[i], i+N, b[i+N], i+2*N, b[i+2*N], i+3*N, b[i+3*N]), end=' ')
        if i % N < N-M+1 and i < N*N - N*(M-1):
            m3 = max(m3, b[i] * b[i+N+1] * b[i+2*N+2] * b[i+3*N+3])
#            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(i, b[i], i+N+1, b[i+N+1], i+2*N+2, b[i+2*N+2], i+3*N+3, b[i+3*N+3]), end=' ')
#            if dbg > 3 and i > 0 and i % N == 0: print()
        j = N*N-1-i
        if i % N >= M-1 and j > (M-1)*N-1:
            m4 = max(m4, b[j] * b[j-N+1] * b[j-2*N+2] * b[j-3*N+3])
            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(j, b[j], j-N+1, b[j-N+1], j-2*N+2, b[j-2*N+2], j-3*N+3, b[j-3*N+3]), end=' ')
            if dbg > 3 and (i+1) % N == 0: print()
    if dbg > 3: print()
    m = max(m1, m2, m3, m4)
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

@docstring('Uses: ' + testS.__doc__)
def test13B(args={'dbg': 1}):
    '''\
         b=testS(): i(N*N) if i%N<N-M+1: m1=max(m1,b[i]*b[i+1]*b[i+2]*b[i+3])                                if i<N*N-N*(M-1): m2=max(m2,b[i]*b[i+N]*b[i+2*N]*b[i+3*N]) 
         if i%N<N-M+1 and i<N*N-N*(M-1): m3=max(m3,b[i]*b[i+N+1]*b[i+2*N+2]*b[i+3*N+3]) j=N*N-1-i if i%N>=M-1 and j>(M-1)*N-1: m4=max(m4,b[j]*b[j-N+1]*b[j-2*N+2]*b[j-3*N+3])'''
    test = 'test13B'
    dbg = 1
    if 'dbg' in args: dbg = args['dbg']
    if 'N'   in args:   N = args['N']
    if 'M'   in args:   M = args['M']
#    if dbg > 0: print('.', end='')
    m1 = m2 = m3 = m4 = 0
    b = testS(args={'N':20})
    if dbg > 2:
        for i in range(N*N):
            print('{:2}'.format(b[i]), end=' ')
            if (i + 1) % N == 0: print()
    for i in range(N*N):
        if i % N < N-M+1:
            m1 = max(m1, b[i] * b[i+1] * b[i+2] * b[i+3])
#            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(i, b[i], i+1, b[i+1], i+2, b[i+2], i+3, b[i+3]), end=' ')
        if i < N*N - N*(M-1):
            m2 = max(m2, b[i] * b[i+N] * b[i+2*N] * b[i+3*N])
#            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(i, b[i], i+N, b[i+N], i+2*N, b[i+2*N], i+3*N, b[i+3*N]), end=' ')
        if i % N < N-M+1 and i < N*N - N*(M-1):
            m3 = max(m3, b[i] * b[i+N+1] * b[i+2*N+2] * b[i+3*N+3])
#            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(i, b[i], i+N+1, b[i+N+1], i+2*N+2, b[i+2*N+2], i+3*N+3, b[i+3*N+3]), end=' ')
#            if dbg > 3 and i > 0 and i % N == 0: print()
        j = N*N-1-i
        if i % N >= M-1 and j > (M-1)*N-1:
            m4 = max(m4, b[j] * b[j-N+1] * b[j-2*N+2] * b[j-3*N+3])
            if dbg > 3: print('({:3},{:2} {:3},{:2} {:3},{:2} {:3},{:2})'.format(j, b[j], j-N+1, b[j-N+1], j-2*N+2, b[j-2*N+2], j-3*N+3, b[j-3*N+3]), end=' ')
            if dbg > 3 and (i+1) % N == 0: print()
    if dbg > 3: print()
    m = max(m1, m2, m3, m4)
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Horizontal', m1))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Vertical',   m2))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal A', m3))
    if dbg > 1: print("{} greatest product of {} cells '{}' [?][?] = [?] = {:,}".format(test, M, 'Diaginal B', m4))
    if dbg: print("{} greatest product of {} cells in any direction is '?' [?][?] = [?] = {:,}".format(test, M, m))

if __name__ == "__main__":
    main()

'''
Jwclemens@LAPTOP-IUJAQF4L MINGW64 /c/Python36/my/tags/ProjectEuler/0011_largest_product_in_grid (master)
$ python 0011_LargestProductInGrid.py 20 10000 3 0 A B C D E F G H I J 0A 0B 1A 1B 2A 2B 3A 3B 3C 4 5 6A 6B 7 8 9 10A 10B 11 12A 12B 13A
    In the 20*20 grid below, four numbers along a diagonal line have been marked in red.
    The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20*20 grid?
Run testA n=10,000 r=3 'testA: i(len(grid)) a.append(grid[i].split()) j(len(grid[i]) a[i][j] = int(a[i][j])'
    testA n=10,000 loops (    1.146    1.352     1.19 ) sec  MIN = 114 usec/loop
Run testB n=10,000 r=3 'a = [[int(grid[i].split()[j]) j(N)] i(N)]'
    testB n=10,000 loops (    3.922    4.023    3.651 ) sec  MIN = 365 usec/loop
Run testC n=10,000 r=3 'a = [[int(x) for x in g.split()] for g in grid]'
    testC n=10,000 loops (   0.8181   0.8072   0.7729 ) sec  MIN = 77 usec/loop
Run testD n=10,000 r=3 '[a = list(map(int, g.split()) g(grid)]'
    testD n=10,000 loops (   0.6789   0.6659   0.6704 ) sec  MIN = 66 usec/loop
Run testE n=10,000 r=3 'a = list(map(lambda x:list(map(int, x.split())), grid))'
    testE n=10,000 loops (   0.7302   0.7021   0.7474 ) sec  MIN = 70 usec/loop
Run testF n=10,000 r=3 'a = list(map(lambda x:list(map(int, x)), list(map(lambda x:x.split(), grid))))'
    testF n=10,000 loops (   0.7651   0.7901   0.7231 ) sec  MIN = 72 usec/loop
Run testG n=10,000 r=3 'b = data.replace("\n"," ") b = list(map(int, b.split()))'
    testG n=10,000 loops (   0.6957    0.681   0.6658 ) sec  MIN = 66 usec/loop
Run testH n=10,000 r=3 'b = data.replace("\n"," ") b = b.split()  ###  Does Not call int()  ###'
    testH n=10,000 loops (   0.1668   0.1646   0.1632 ) sec  MIN = 16 usec/loop
Run testI n=10,000 r=3 'c = testB(): [[0]*(N+M-1)]*3 + [[int(grid[i].split()[j]) for j in range(N)] + [0,0,0] for i in range(N)] + [[0]*(N+M-1)]*3'
    testI n=10,000 loops (    3.724    3.912    3.652 ) sec  MIN = 365 usec/loop
Run testJ n=10,000 r=3 'c = testC(): m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] n(M)]) x(N) y(M-1,N+M-1) d in ((0,1),(1,0),(1,1),(-1,1))])'
    testJ n=10,000 loops (   0.9665   0.9472   0.8125 ) sec  MIN = 81 usec/loop
Run test0A n=10,000 r=3 ''
    test0A n=10,000 loops (    5.959    6.957    6.496 ) sec  MIN = 595 usec/loop
Run test0B n=10,000 r=3 ''
    test0B n=10,000 loops (    6.288    6.166     6.16 ) sec  MIN = 616 usec/loop
Run test1A n=10,000 r=3 'Uses: testA: i(len(grid)) a.append(grid[i].split()) j(len(grid[i]) a[i][j] = int(a[i][j])
h = testA(): m = findMaxProdH(h) m = findMaxProdV(h) findMaxProdV(d1A, d1B, d2A, d2B)'
    test1A n=10,000 loops (    24.13     23.3    23.83 ) sec  MIN = 2,329 usec/loop
Run test1B n=10,000 r=3 'Uses: testA: i(len(grid)) a.append(grid[i].split()) j(len(grid[i]) a[i][j] = int(a[i][j])
h = testA(): m = findMaxProdH(h) h = list(zip(*h)) m = findMaxProdH(h) findMaxProdV(d1A, d1B, d2A, d2B)'
    test1B n=10,000 loops (     17.7    19.78    19.41 ) sec  MIN = 1,770 usec/loop
Run test2A n=10,000 r=3 'Uses: a = [[int(grid[i].split()[j]) j(N)] i(N)]
h = testB(): m = findMaxProdH(h) m findMaxProdV(v, d1A, d1B, d2A, d2B)'
    test2A n=10,000 loops (    32.24    32.59    33.07 ) sec  MIN = 3,224 usec/loop
Run test2B n=10,000 r=3 'Uses: a = [[int(grid[i].split()[j]) j(N)] i(N)]
h = testB(): m = findMaxProdH(h) v = list(zip(*h)) m = findMaxProdV(v, d1A, d1B, d2A, d2B)'
    test2B n=10,000 loops (    26.47    25.27    26.35 ) sec  MIN = 2,526 usec/loop
Run test3A n=10,000 r=3 'Uses: a = [[int(grid[i].split()[j]) j(N)] i(N)]
a = testB(): i(N) j(N) if j<=N-M: m1 = max(m1, reduce(lambda x,y:x*y, a[i][j:j+M]) if i<=N-M reduce(lambda x,y:x*y, [a[i+k][j] for k in range(M)])'
    test3A n=10,000 loops (    23.15    23.73    22.67 ) sec  MIN = 2,267 usec/loop
Run test3B n=10,000 r=3 'Uses: a = [[int(grid[i].split()[j]) j(N)] i(N)]
a = testB(): i(N) j(N) if j<=N-M: m1 = max(m1, reduce(lambda x,y:x*y, a[i][j:j+M]) if i<=N-M reduce(lambda x,y:x*y, [e[j] for e in a[i:i+M]])'
    test3B n=10,000 loops (    24.04    22.59     21.3 ) sec  MIN = 2,129 usec/loop
Run test3C n=10,000 r=3 'Uses: a = [[int(grid[i].split()[j]) j(N)] i(N)]
a = testB(): i(N) j(N) if j<=N-M: m1 = max(m1, a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3]) if i<=N-M: m2 = max(m2, a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j])'
    test3C n=10,000 loops (    12.08    12.05    11.17 ) sec  MIN = 1,117 usec/loop
Run test4 n=10,000 r=3 'Uses: a = [[int(grid[i].split()[j]) j(N)] i(N)]
a = testB(): i(N) j(N-M+1) if a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3] > m1: m1 = a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3] if a[j][i]*a[j+1][i]*a[j+2][i]*a[j+3][i] > m2: m2 = a[j][i]*a[j+1][i] * a[j+2][i] * a[j+3][i]'
    test4 n=10,000 loops (    10.76    9.941    9.369 ) sec  MIN = 936 usec/loop
Run test5 n=10,000 r=3 'Uses: [a = list(map(int, g.split()) g(grid)]
rows = testD(): for row in rows: prods.extend([y[0]*y[1]*y[2]*y[3] y in [row[i:i+4] i(N-M+1)]]) [[rows[i][j] i(N)] j(N)]'
    test5 n=10,000 loops (     8.05    8.157     9.02 ) sec  MIN = 804 usec/loop
Run test6A n=10,000 r=3 'Uses: a = [[int(grid[i].split()[j]) j(N)] i(N)]
a = testI(): m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] for n in range(M)]) for x in range(N) for y in range(M-1, N+M-1) for d in ((0,1),(1,0),(1,1),(-1,1))])'
    test6A n=10,000 loops (    31.31    31.31    25.81 ) sec  MIN = 2,580 usec/loop
Run test6B n=10,000 r=3 'Uses: a = [[int(x) for x in g.split()] for g in grid]
a = testJ(): m = max([reduce(mul, [a[y+n*d[0]][x+n*d[1]] for n in range(M)]) for x in range(N) for y in range(M-1, N+M-1) for d in ((0,1),(1,0),(1,1),(-1,1))])'
    test6B n=10,000 loops (    26.93     26.1    28.27 ) sec  MIN = 2,609 usec/loop
Run test7 n=10,000 r=3 'cell(x, y): return int(grid[y-1][(x-1)*3:(x-1)*3+2]) y(1, N+1) x(1,L) yield [cell(x, y), cell(x+1, y), cell(x+2, y), cell(x+3, y)]'
    test7 n=10,000 loops (    33.86    31.03     32.6 ) sec  MIN = 3,103 usec/loop
Run test8 n=10,000 r=3 'Uses: [a = list(map(int, g.split()) g(grid)]
a = testD(): i(N) j(N-M+1) m1 = max(m1, prod([a[i][j+k] for k in range(M)]))'
    test8 n=10,000 loops (    22.58    20.52    18.28 ) sec  MIN = 1,828 usec/loop
Run test9 n=10,000 r=3 'Uses: [a = list(map(int, g.split()) g(grid)]
a = testD(): m = max([max(list(prod9))) i(N) j(N)] prod9: if j<N-M+1 yield reduce(mul, [a[i][j+k] for k in range(M)])'
    test9 n=10,000 loops (    18.92     17.3    17.69 ) sec  MIN = 1,730 usec/loop
Run test10A n=10,000 r=3 'Uses: b = data.replace("\n"," ") b = list(map(int, b.split()))
b = testG(): i(len(b)) if i%N<N-M+1: m1 = max(m1, reduce(lambda x,y:x*y, b[i:i+M]))'
    test10A n=10,000 loops (    11.27    11.38    11.35 ) sec  MIN = 1,126 usec/loop
Run test10B n=10,000 r=3 'Uses: b = data.replace("\n"," ") b = b.split()  ###  Does Not call int()  ###
b = testH(): i(len(b)) if i%N<N-M+1: m1 = max(m1, reduce(lambda x,y:int(x)*int(y), b[i:i+M]))  ###  Calls int() more than once/node  ###'
    test10B n=10,000 loops (    21.34    21.25    21.51 ) sec  MIN = 2,124 usec/loop
Run test11 n=10,000 r=3 'Uses: [a = list(map(int, g.split()) g(grid)]
a = testD(): prod = lambda s: reduce(lambda x,y:x*y, s) i(N-M) j(N-M) m1 = max(m1, prod(a[i][j:j+M])) m2 = max(m2, prod([d[j] for d in a[i:i+M]]))'
    test11 n=10,000 loops (     9.35     9.36    8.911 ) sec  MIN = 891 usec/loop
Run test12A n=10,000 r=3 'Uses: [a = list(map(int, g.split()) g(grid)]
a = testD(): n(a) p('
    test12A n=10,000 loops (    21.64    21.59     21.1 ) sec  MIN = 2,110 usec/loop
Run test12B n=10,000 r=3 'Uses: [a = list(map(int, g.split()) g(grid)]
a = testD(): '
    test12B n=10,000 loops (    8.306    10.11    8.963 ) sec  MIN = 830 usec/loop
Run test13A n=10,000 r=3 ''
    test13A n=10,000 loops (    12.66    12.97    12.32 ) sec  MIN = 1,232 usec/loop
'''

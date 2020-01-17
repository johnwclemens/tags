def getProds(a=None, dbg=1):
    aDefault = (4, 7, 3, 2, 5)
    if a is None or len(a) is 0:
        a = aDefault
    max = len(a)
    print('a = {}'.format(a))
    l, p = 1, []
    for i in range(0, max):
        if i > 0:
            l *= a[i-1]
        if dbg: print('i={}, l={}'.format(i, l))
        r = 1
        for j in range(max-1, i, -1):
            r *= a[j]
            if dbg: print('    j={}, r={}'.format(j, r))
        if dbg: print('p = {}'.format(l*r))
        p.append(l*r)
    return p
    
if __name__ == "__main__":
    inP = (1,2,3,4,5)
    outP = getProds(a=None)
    print('products = {}'.format(outP))
    
'''
4, 7, 3, 2, 5 PROD=840
-------------------------------------------------------------------------
| I |     LEFT    |   RIGHT    | LEFT INDEX | RIGHT INDEX | 0->I | I->L |
|---|-------------|------------|-----------------------------------------
| 0 |           1 | 7, 3, 2, 5 | N          | 1, 2, 3, 4  |      | 1->4 | 
| 1 |  4          |    3, 2, 5 | 0          |    2, 3, 4  | 0->0 | 2->4 |
| 2 |  4, 7       |       2, 5 | 0, 1       |       3, 4  | 0->1 | 3->4 |
| 3 |  4, 7, 3    |          5 | 0, 1, 2    |          4  | 0->2 | 4->4 |
| 4 |  4, 7, 3, 2 | 1          | 0, 1, 2, 3 | N           | 0->3 |      |
-----------------------------------------------------------------|------|
840/4, 840/7, 840/3, 840/2, 840/5
210, 120, 280, 420, 168
'''

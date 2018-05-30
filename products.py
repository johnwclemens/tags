def getProds(a=None):
    aDefault = (4, 7, 3, 2, 5)
    if a is None or len(a) is 0:
        a = aDefault
    la = len(a)
    print('a = (', end='')
    print('{}'.format(a[0]), end='')
    for i in range(1, la):
        print(',{}'.format(a[i]), end='')
    print(')')
    lp, rp, r = 1, 1, []
    for i in range(0, la):
        if i > 0:
            lp *= a[i-1]
        if i < la-1:
            rp *= a[i+1]
        r.append(lp*rp)
    return r
#    return aDefault[0]
    
if __name__ == "__main__":
#    inP = (5, 4, 8, 6, 3)
#    inP = [2, 1]
#    inP = [2,]
    inP = []
    outP = getProds(a=inP)
#    outP = getProds()
#    outP = getProds(a=None)
    print('prod = {}'.format(outP))
    
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
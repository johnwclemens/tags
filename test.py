#print(int("1306 Mr. Burns ltd."))
#file = open("test.txt", "r")
#stuff = file.read()
#print(stuff)
#for x in file:
#    print(x)
#x = 25.00
#print(x)
#print(5%7)
#print(12%5)

'''
def Pmt(rate, npmts, presv, futv):
    interest = (1 + rate/100) / npmts
    pmt = presv * interest
    futv = pmt * npmts
    print('interest={}, futv={}', interest, futv)
    return pmt
    0
tot = 0
pmt = Pmt(rate=2, npmts=18, presv=5000, futv=tot)
print('pmt={}, tot={}'.format(pmt, tot))
'''

import pickle

file = open("testPickle.txt", "wb")
a1 = ['ketchup', 'mustard', 'mayo']
pickle.dump(a1, file)
b1 = 1
pickle.dump(b1, file)
c1 = ['cheese', 'lettace', 'tomatoe']
pickle.dump(c1, file)
d1 = 'whats up doc?'
pickle.dump(d1, file)
print('a1={}, b1={}, c1={}, d1={}'.format(a1, b1, c1, d1))
file.close()

file = open("testPickle.txt", "rb")
a2 = pickle.load(file)
b2 = 2
b2 = pickle.load(file)
c2 = pickle.load(file)
d2 = pickle.load(file)
e2 = pickle.load(file)
print('a2={}, b2={}, c2={}, d2={}'.format(a2, b2, c2, d2))
file.close()

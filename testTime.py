import os, sys, re, collections, time
from functools import wraps
sys.path.insert(0, os.path.abspath('..\lib'))
import jwcCmdArgs

def main(): 
    t = Test()
    t.run()

class Test(object):
    def __init__(self):
        self.count = 10000
        self.NANOS_PER_SEC = 1000000000
        self.getCmdArgs()

    def getCmdArgs(self):
        self.argMap = jwcCmdArgs.parseCmdLine()
        print('argMap={}'.format(self.argMap))
        if 'c' in self.argMap and len(self.argMap['c']) > 0:
            self.count = int(self.argMap['c'][0].upper())

    def run(self):
        ss = []
        ss.append('a b c d e f g h i j k l m n o p q r s t u v w x y z')
        ss.append('at be ci do eb fe go he in je ku la me no on pi qu re so to up vi we xo yy zz')
        ss.append('ant bed cat dog elf fox gem hot ink jam key lip map new old pig que rat sit top urn van win xyz yes zig')
        ss.append('atom beta corn dorm elle feet golf help inch join kelp live moon neon open pity quit root suit tech used visa west xray your zero')
        ss.append('attic bathe cache dirty earth filth germs horse ivory juice karma liver month north ounce pinch quiet ripen story tower utter vixan wagon xrays yield zoned')
        ss.append('almost better combat dormer evenly filthy gutter hotdog insect jumped killed loosen mirror nordic office poplar quiets report stairs tarmac uneven velvet wanted xyzxyz youths zigzag')
        ss.append('aluring brother compact dentist earthen follows greased hollows inspect jumping killing loosely mirrors normals offices popcorn quieted respect started totaled useless velveta wanting xyzxyzx yellows zigzags')
        for s in ss:
            with Timer(self.NANOS_PER_SEC, self.count) as t:
                for i in range(self.count):
                    v = s.split()
                    s = ' '.join(v)
            print('dt={:.0f}, dt={:.1f}, s[{}]={}'.format(t.interval, t.interval/len(s), len(s), s))

class Timer(object):
    def __init__(self, nanosPerSec, count):
        self.nanosPerSec = nanosPerSec
        self.count = count

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = (self.end - self.start) * self.nanosPerSec / self.count

if __name__ == "__main__":
    main()

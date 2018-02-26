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
        s1 = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
        s2 = 'at be ci do eb fe go he in je ku la me no on pi qu re so to up vi we xo yy zz'
        s3 = 'ant bed cat dog elf fox gem hot ink jam key lip map new old pig que rat sit top urn van win xyz yes zig'
        s4 = 'atom beta corn dorm elle feet golf help inch join kelp live moon neon open pity quit root suit tech used visa west xray your zero'
        s5 = 'attic, bathe, cache, dainty, earth, filth, germs, horse, ivory, juice, karma, month, north, ounce, pinch, quiet, ripen, story, tower, utter, vixan, wagon, xrays, yield, zoned'
        with Timer(self.NANOS_PER_SEC, self.count) as t:
            for i in range(self.count):
                l = s1.split()
                s1 = ' '.join(l).upper()
        print('dt={:.0f}, count={}, nps={}, s1[{}]={}'.format(t.interval, self.count, self.NANOS_PER_SEC, len(s1), s1))
        with Timer(self.NANOS_PER_SEC, self.count) as t:
            for i in range(self.count):
                l = s2.split()
                s2 = ' '.join(l).upper()
        print('dt={:.0f}, count={}, nps={}, s2[{}]={}'.format(t.interval, self.count, self.NANOS_PER_SEC, len(s2), s2))
        with Timer(self.NANOS_PER_SEC, self.count) as t:
            for i in range(self.count):
                l = s3.split()
                s3 = ' '.join(l).upper()
        print('dt={:.0f}, count={}, nps={}, s3[{}]={}'.format(t.interval, self.count, self.NANOS_PER_SEC, len(s3), s3))
        with Timer(self.NANOS_PER_SEC, self.count) as t:
            for i in range(self.count):
                l = s4.split()
                s4 = ' '.join(l).upper()
        print('dt={:.0f}, count={}, nps={}, s4[{}]={}'.format(t.interval, self.count, self.NANOS_PER_SEC, len(s4), s4))
        with Timer(self.NANOS_PER_SEC, self.count) as t:
            for i in range(self.count):
                l = s5.split()
                s5 = ' '.join(l).upper()
        print('dt={:.0f}, count={}, nps={}, s5[{}]={}'.format(t.interval, self.count, self.NANOS_PER_SEC, len(s5), s5))

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

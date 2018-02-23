import os, sys, re, collections, time
from functools import wraps
sys.path.insert(0, os.path.abspath('..\lib'))
import jwcCmdArgs

#'''
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
#'''

def main():
    Tags()
    '''
    def timed(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = time()
            for r in range(args[0]):
                retVal = f(*args, **kwargs)
            print('dt={}'.format(time() - start))
            return retVal
        return wrapper

    @timed
    def f(count, d):
        l = d.split()
        d = ' '.join(l)
        return 'f({}, \'{}\')'.format(count, d)

    d = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    print('f.__name__={}'.format(f.__name__))
    print('f.__doc__={}'.format(f.__doc__))
    r = f(100000, d)
    print('r={}'.format(r))
    exit()
    '''

class Tags(object):
    def timer(self, count, func, *args, **kwargs):
        t1 = time.monotonic()
        for i in range(0, count):
            retVal = func(*args, **kwargs)
        dt = self.NANOS_PER_SEC * (time.monotonic() - t1) / (count)
        return dt, retVal

    def __init__(self, inFileName = 'in.txt', outFileName='out.txt'):
        self.t0 = time.monotonic()
        self.tokenCount = 0
        self.tags, self.type = None, 'R'
        self.reDate = r'\s*(?P<reDate>1[0-2]|0[1-9]|[1-9])-(1[0-9]|2[0-9]|3[0-1]|0[1-9]|[1-9])-(\d{2})\s*'
        self.cres = {'Title1':re.compile(r"[A-Za-z]+('[A-Za-z]+)?"), 'Title2':re.compile('\((.*?)\)'), 'Date':re.compile(self.reDate)}
        self.titleFuncMap = {'A':self.getTitleA, 'B':self.getTitleB, 'Q':self.getTitleQ, 'R':self.getTitleR}
        self.dateFuncMap  = {'A':self.getDateR,  'B':self.getDateR,  'Q':self.getDateQ,  'R':self.getDateR}
        self.NANOS_PER_SEC, self.timerCount = 1000000000, 1000
        self.dtTitle, self.dtParse, self.dtDate = 0, 0, 0
        self.len, self.fileSize, self.charCount = 0, 0, 0
        self.inFileName, self.outFileName = inFileName, outFileName
        self.getCmdArgs()
        with open(self.outFileName, 'w+') as self.outFile, open(self.inFileName, 'r') as self.inFile: self.readFile()

    def getCmdArgs(self):
        self.argMap = jwcCmdArgs.parseCmdLine()
        print('argMap={}'.format(self.argMap))
        if 'c' in self.argMap and len(self.argMap['c']) > 0:
            self.timerCount = int(self.argMap['c'][0].upper())
        if 'i' in self.argMap and len(self.argMap['i']) > 0:
            self.inFileName = self.argMap['i'][0]
        if 'o' in self.argMap and len(self.argMap['o']) > 0:
            self.outFileName = self.argMap['o'][0]
        if 't' in self.argMap and len(self.argMap['t']) > 0:
            self.type = self.argMap['t'][0].upper()

    def readFile(self):
        for line in self.inFile:
            i = 0
            self.fileSize += len(line) + 1 #account for the line termination char?
            self.getTags(line.strip())
            for k, v in self.tags.items():
                i += 1
                length = len(v)
                self.len += length
                self.printn('    {:>20}[{:>2}:{:>2}:{:>3}] {}'.format(k, i, length, self.len, v))
            self.printn('tags({}) = ['.format(self.len), end='')
            for k in self.tags.keys(): self.printn('{}'.format(self.tags[k]), end=',')
            self.printn("]")
            self.len = 0
        self.printn('Avg time title/char = {:7.3f} nano seconds, avg time parse = {:.0f} nano seconds, avg time date = {:.0f} nano seconds'.format(self.dtTitle, self.dtParse, self.dtDate), file = 'BOTH')
        self.printn('Total time = {:.1f} seconds, type = {}, fileSize={} bytes'.format(time.monotonic() - self.t0, self.type, self.fileSize), file = 'BOTH')

    def getTags(self, line, idx=[0]):
        n = idx[0]
        idx[0] += 1
        self.printn('line[{},{},{},{}] = {}'.format(idx[0], len(line), self.fileSize, self.type, line))
        self.tags = collections.OrderedDict()
        dtTitle, title = self.timer(self.timerCount, self.titleFuncMap[self.type], line)
        dtTitle /= len(line)
        self.dtTitle = (n * self.dtTitle + dtTitle) / idx[0]
        self.printn('dtTitle[{}]={:7.3f} nsec, self.dtTitle={:7.3f} nsec'.format(idx[0], dtTitle, self.dtTitle))
        self.addTag('Title', ''.join(title.split(',')))
#        dtParse, remainder = self.timer(self.timerCount, self.parse, title, ', ', ['Name', 'Venue', 'City', 'State'])
#        self.dtParse = (n * self.dtParse + dtParse / self.tokenCount) / idx[0]
#        self.printn('dtParse={:.0f} nsec, self.dtParse = {:.0f} nsec'.format(dtParse / self.tokenCount, self.dtParse))
        with Timer(self.NANOS_PER_SEC, self.timerCount) as dtParse:
            for x in range(self.timerCount):
                remainder = self.parse(title, ', ', ['Name', 'Venue', 'City', 'State'])
        self.dtParse = (n * self.dtParse + dtParse.interval / self.tokenCount) / idx[0]
        self.printn('dtParse={:.0f} nsec, self.dtParse = {:.0f} nsec'.format(dtParse.interval / self.tokenCount, self.dtParse))
        dtDate, ret = self.timer(self.timerCount, self.dateFuncMap[self.type], remainder)
        self.dtDate = (n * self.dtDate + dtDate) / idx[0]
        self.printn('dtDate={:.0f} nsec, self.dtDate = {:.0f} nsec'.format(dtDate, self.dtDate))
        self.group()

    def getTitleA(self, s):
        t = ''
        for w in s.split():
            if w[0] not in {'(', ')'}: t += w[0].upper()
            for i in range(1, len(w)):
                if w[i] not in {'(', ')'}: t += w[i]
            t += ' ' 
        return t

    def getTitleB(self, s):
        t = ''
        isWord = True
        for i in range(0, len(s)):
            if s[i] not in {'(', ')'}:
                if isWord:
                    t += s[i].upper()
                    isWord = False
                else: t += s[i]
                if s[i] == ' ': isWord = True
        return t

    def getTitleQ(self, s):
        s = self.cres['Title1'].sub(lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:], s)
        return self.cres['Title2'].sub(r'\1', s)

    def getTitleR(self, s):
        s = re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:], s)
        return re.sub(r'\((.*?)\)', r'\1', s)

    def addTag(self, key, value):
        self.tags[key] = value

    def parse(self, s, delim, keys):
        max = len(keys)
        tokens = s.split(delim, max+1)
        self.tokenCount = len(tokens)
        for i in range(0, max):
            self.addTag(keys[i], tokens[i])
        i += 1
        remainder = tokens[-1]
        return remainder

    def getDateQ(self, s):
        m = self.cres['Date'].search(s)
        if m.start() != 0: self.addTag('Other1', s[:m.start()])
        self.addTag('Date', m.group(1) + '-' + m.group(2) + '-' + m.group(3))
        remainder = s[m.end():]
        if remainder: self.tags['Other2'] = remainder

    def getDateR(self, s):
        m = re.search(self.reDate, s)
        if m.start() != 0: self.addTag('Other1', s[:m.start()])
        self.addTag('Date', m.group(1) + '-' + m.group(2) + '-' + m.group(3))
        remainder = s[m.end():]
        if remainder: self.tags['Other2'] = remainder

    def group(self):
        self.addTag('Name_Date', self.tags['Name'] + " " + self.tags['Date'])
        self.addTag('Name_Venue', self.tags['Name'] + " " + self.tags['Venue'])
        self.addTag('Name_City', self.tags['Name'] + " " + self.tags['City'])
        self.addTag('Name_Venue_Date', self.tags['Name'] + " " + self.tags['Venue'] + " " + self.tags['Date'])
        self.addTag('Name_Venue_City', self.tags['Name'] + " " + self.tags['Venue'] + " " + self.tags['City'])
        self.addTag('Name_City_Date', self.tags['Name'] + " " + self.tags['City'] + " " + self.tags['Date'])
        self.addTag('City_Date', self.tags['City'] + " " + self.tags['Date'])
        self.addTag('Venue_Date', self.tags['Venue'] + " " + self.tags['Date'])

        self.addTag('Name_City_Live', self.tags['Name'] + " Live " + self.tags['City'])
        self.addTag('Name_Date_Live', self.tags['Name'] + " Live " + self.tags['Date'])
        self.addTag('Name_Venue_Live', self.tags['Name'] + " Live " + self.tags['Venue'])
        self.addTag('Name_Venue_Date_Live', self.tags['Name'] + " Live " + self.tags['Venue'] + " " + self.tags['Date'])

    def printn(self, msg='', sep=' ', end='\n', file=None, flush=True):
        if not file: print(msg, sep=sep, end=end, file=self.outFile, flush=flush)
        elif file == 'BOTH':
            print(msg, sep=sep, end=end, file=self.outFile, flush=flush)
            print(msg, sep=sep, end=end, file=sys.stdout, flush=flush)
        else: print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()

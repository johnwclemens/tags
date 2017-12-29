import os, sys, re

reDate       = r'\s*(?P<reDate>\d{1,2}-\d{1,2}-\d{2})\s*'

def main():
    tags = Tags(inFileName='titles.txt', outFileName='tags.txt')
    tags.run()

class Tags(object):
    def __init__(self, inFileName = 'titles.txt', outFileName='tags.txt'):
        self.tags = None
        self.cres = {}
        self.inFileName = inFileName
        self.outFileName = outFileName

    def run(self):
        with open(self.outFileName, 'w') as self.outFile, open(self.inFileName, 'r') as self.inFile:
            self.getTitles()
        print('inFile={}'.format(self.inFile))
        self.inFile = None
        print('inFile={}'.format(self.inFile))
        print('outFile={}'.format(self.outFile))
        self.outFile = None
        print('outFile={}'.format(self.outFile))

    def getTitles(self):
        for line in self.inFile:
            self.getTags(line.strip())
            printn('tags = {', file=self.outFile)
            for k in self.tags.keys(): printn('    {} => {},'.format(k, self.tags[k]), file=self.outFile)
            printn("}", file=self.outFile)

    def getTags(self, line):
        printn('line = {}'.format(line), file=self.outFile)
        self.tags = {}
        title = self.titleCase(line)
        self.tags['Title'] = title
    #    words = title.split()
    #    printn('words = [', file=self.outFile, end='')
    #    for w in words:
    #        w = w.strip('),(')
    ##        tags.append(w)
    #        printn(' {}'.format(w), file=self.outFile, end='')
    #    printn(']', file=self.outFile)
    ##    tags['Title'] = ' '.join(words)
        remainder = self.parse(title, ' At ', ['Name'])
        remainder = self.parse(remainder, ', ', ['Venue', 'City'])
        self.getDate(remainder)

    def titleCase(self, s):
        printn('titleCase({})'.format(s))
    #    return re.sub(r"([A-Za-z]+)", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)
        return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)

    def parse(self, s, delim, keys):
        max = len(keys)
        tokens = s.split(delim, max+1)
    #    printn('parse(delim = [{}], keys = {})'.format(delim, keys), file=self.outFile)
        printn('parse([{}], delim = [{}], keys = ['.format(s, delim), file=self.outFile, end='')
        for i in range(0, max):
            self.tags[keys[i]] = tokens[i]
            printn(' {}'.format(keys[i]), file=self.outFile, end='')
        printn('])', file=self.outFile)
        for i in range(0, max):
            printn('    [{}], {} = {}'.format(i, keys[i], tokens[i]), file=self.outFile)
        i += 1
        remainder = tokens[-1]
        printn('    [{}], {} = {}'.format(i, 'Remainder', tokens[i]), file=self.outFile)
        return remainder

    def getDate(self, dStr):
        m = self.findString(dStr, 'reDate', reDate)
        if m:
            print('m={}'.format(m))
            grpMap = m.groupdict()
            if 'reDate' in grpMap:
                date = m.group('reDate')
                print('    date = {}'.format(date), file=self.outFile)
                self.tags['Date'] = date

    def findString(self, s, key, pattern):
        if key not in self.cres:
            self.cres[key] = re.compile(pattern)
        return self.cres[key].search(s)

def printn(msg='', sep=' ', end='\n', file=sys.stdout, flush=False):
    print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()


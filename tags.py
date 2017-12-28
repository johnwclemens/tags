#Funktional Family At Kiss The Sky Batavia IL 12-03-17 (Camera 1)
import os, sys, re

cres = {}
#reVenue      = r'(?P<reVenue>\S+\s)+'
reDate       = r'\s*(?P<reDate>\d{1,2}-\d{1,2}-\d{2})\s*'

def main():
    Tags()
    '''
    with open('tags.txt', 'w') as outFile:
        with open('titles.txt', 'r') as inFile:
            getTitles(inFile, outFile)
        print('inFile={}'.format(inFile))
        inFile = None
        print('inFile={}'.format(inFile))
    print('outFile={}'.format(outFile))
    outFile = None
    print('outFile={}'.format(outFile))
    '''

class Tags(object):
    def __init__(self, inFileName = 'titles.txt', outFileName='tags.txt'):
        self.inFileName = inFileName
        self.outFileName = outFileName
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
            tags = self.getTags(line.strip())
            printn('tags = {', file=self.outFile)
            for k in tags.keys(): printn('    {} => {},'.format(k, tags[k]), file=self.outFile)
            printn("}", file=self.outFile)

    def getTags(self, line):
        printn('line = {}'.format(line), file=self.outFile)
        tags = {}
        title = self.titleCase(line)
        tags['Title'] = title
    #    words = title.split()
    #    printn('words = [', file=self.outFile, end='')
    #    for w in words:
    #        w = w.strip('),(')
    ##        tags.append(w)
    #        printn(' {}'.format(w), file=self.outFile, end='')
    #    printn(']', file=self.outFile)
    ##    tags['Title'] = ' '.join(words)
        remainder = self.parse(title, ' At ', ['Name'], tags)
        remainder = self.parse(remainder, ', ', ['Venue', 'City'], tags)
        self.getDate(remainder, tags)
        return tags

    def titleCase(self, s):
        printn('titleCase({})'.format(s))
    #    return re.sub(r"([A-Za-z]+)", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)
        return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)

    def parse(self, s, delim, keys, tags):
        max = len(keys)
        tokens = s.split(delim, max+1)
    #    printn('parse(delim = [{}], keys = {})'.format(delim, keys), file=self.outFile)
        printn('parse([{}], delim = [{}], keys = ['.format(s, delim), file=self.outFile, end='')
        for i in range(0, max):
            tags[keys[i]] = tokens[i]
            printn(' {}'.format(keys[i]), file=self.outFile, end='')
        printn('])', file=self.outFile)
        for i in range(0, max):
            printn('    [{}], {} = {}'.format(i, keys[i], tokens[i]), file=self.outFile)
        i += 1
        remainder = tokens[-1]
        printn('    [{}], {} = {}'.format(i, 'Remainder', tokens[i]), file=self.outFile)
        return remainder

    def getDate(self, dStr, tags):
        m = findString(dStr, cres, 'reDate', reDate)
        if m:
            print('m={}'.format(m))
            grpMap = m.groupdict()
            if 'reDate' in grpMap:
                date = m.group('reDate')
                print('    date = {}'.format(date), file=self.outFile)
                tags['Date'] = date

def genTags0(title, outFile):
    title = title.title()
    tags = [title]
    words = title.split()
    printn('words = [', end='', file=outFile)
    for w in words:
        printn('{}'.format(w), end=' ', file=outFile)
    printn(']', file=outFile)
    stuff = title.split(' At ')
    printn('stuff[{}] = {}'.format(len(stuff), stuff), file=outFile)
    name = stuff[0]
    stuff = stuff[1]
    printn('    name = {}'.format(name), file=outFile)
    printn('stuff[{}] = {}'.format(len(stuff), stuff), file=outFile)
    stuff = stuff.split(',')
    printn('stuff[{}] = {}'.format(len(stuff), stuff), file=outFile)
    venue = stuff[0]
    city = stuff[1]
    stuff = stuff[2]
    printn('    venue = {}'.format(venue), file=outFile)
    printn('    city = {}'.format(city), file=outFile)
    printn('stuff[{}] = {}'.format(len(stuff), stuff), file=outFile)
    printn('########################', file=outFile)
    remainder = split(title, ' At ', ['Name'], outFile)
    split(remainder, ', ', ['Venue', 'City'], outFile)
    printn('########################', file=outFile)

def genTags1(title, outFile):
    title = title.title()
    tags = [title]
    words = title.split()
    printn('words = ', end='', file=outFile)
    for w in words:
        printn('{}'.format(w), end=' ', file=outFile)
    printn(',', file=outFile)
    stuff = title.split(' At ')
    printn('stuff = {}'.format(stuff), file=outFile)
    name = stuff[0]
    stuff1 = stuff[1]
    printn('    name = {}'.format(name), file=outFile)
#    printn('    stuff1 = {}'.format(stuff1), file=outFile)
    stuff2 = stuff1.split(',')
#    printn('    stuff2 = {}'.format(stuff2), file=outFile)
    venue = stuff2[0]
    stuff3 = stuff2[1]
    printn('    venue = {}'.format(venue), file=outFile)
    printn('    stuff3 = {}'.format(stuff3), file=outFile)
    stuff4 = stuff3.split(',')
    city = stuff4[0]
    stuff5 = stuff4[1]
    state = stuff5[0]
    stuff6 = stuff5[1]
    key = 'parse'
    pattern = reDate
    print('pattern={}'.format(pattern))
    m = findString(stuff6, cres, key, pattern)
    if m:
        print('m={}'.format(m))
        grpMap = m.groupdict()
        if 'reDate' in grpMap:
            date = m.group('reDate')
            print('    date = {}'.format(date), file=outFile)
            tags.append(date)
#        if 'reVenue' in grpMap:
#            venue = m.group('reVenue')
#            print('    venue = {}'.format(venue), file=outFile)
#            tags.append(venue)

def genTags2(title, outFile):
    tags = [title]
    words = title.split()
    printn('    ', end='', file=outFile)
    for word in words:
        printn('{}'.format(word), end=' ', file=outFile)
    printn(',', file=outFile)
#    idx = title.find('At')
#    if idx != -1:
#        name = title[:idx-1]
#        print('{}'.format(name), file=outFile)
#        tags.append(name)
    printn("title={}".format(title))
    key = 'date'
    pattern = reName + reAt# + reName + reAt + reName# + reDate
    print('pattern={}'.format(pattern))
    m = findString(title, cres, key, pattern)
    if m:
        print('m={}'.format(m))
        print('group(0)={}, group(1)={}, group(2)={}'.format(m.group(0), m.group(1), m.group(2)))
        grpMap = m.groupdict()
        if 'reName' in grpMap:
            name = m.group('reName')
            print('name={}'.format(name))
            tags.append(name)
        if 'reAt' in grpMap:
            at = m.group('reAt')
            print('at={}'.format(at))
            tags.append(at)
        if 'reDate' in grpMap:
            date = m.group('reDate')
            print('date={}'.format(date))
            tags.append(date)
        if 'reName1' in grpMap:
            name1 = m.group('reName1')
            print('name1={}'.format(name1))
            tags.append(name1)
        if 'reName2' in grpMap:
            name2 = m.group('reName2')
            print('name2={}'.format(name2))
            tags.append(name2)
    return tags

def findString(s, cres, key, pattern):
    if key not in cres:
        cres[key] = re.compile(pattern)
    return cres[key].search(s)

def printn(msg='', sep=' ', end='\n', file=sys.stdout, flush=False):
    print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()


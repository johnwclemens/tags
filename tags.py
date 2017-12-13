#Funktional Family At Kiss The Sky Batavia IL 12-03-17 (Camera 1)
import os, sys, re

cres = {}
reAt         = r'(?P<reAt>at|At)\s+'
#reAt         = r'\s*(?P<reAt>at|At)\s*'
reDate       = r'\s*(?P<reDate>\d{2}-\d{2}-\d{2})\s*'
#reName       = r'\s*(\S+)\s*'
#reName       = r'(\s*\S+){1,4}'
#reName       = r'(?P<reName>\s*\S+){1,4}'
#reName1       = r'(?P<reName1>\s*\S+)'
#reName2       = r'(?P<reName2>\s*\S+)'
#reName1       = r'(?P<reName1>\S+\s+)'
#reName2       = r'(?P<reName2>\S+\s+)'
#reName        = r'(?P<reName>\S+\s+){1,4}'
reName        = r'(?P<reName>\S+\s+)+'

def main():
    with open('tags.txt', 'w') as outFile:
        with open('titles.txt', 'r') as inFile:
            getTitles(inFile, outFile)
        inFile = None
    outFile = None
    print('inFile={}'.format(inFile))

def getTitles(inFile, outFile):
    for line in inFile:
        title = line.rstrip('\n')
        printn("title={}".format(title), file=outFile)
        tags = genTags(title, outFile)
        printn("tags={}".format(tags), file=outFile)

def genTags(title, outFile):
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


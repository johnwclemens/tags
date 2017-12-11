#Funktional Family At Kiss The Sky Batavia IL 12-03-17 (Camera 1)
import os, sys, re

cres = {}
reDate       = r'\s*(?P<reDate>\d{2}-\d{2}-\d{2})\s*'

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
    idx = title.find('At')
    if idx != -1:
        name = title[:idx-1]
        print('{}'.format(name), file=outFile)
        tags.append(name)
    key = 'date'
    pattern = reDate
    m = findString(title, cres, key, pattern)
    if m:
        grpMap = m.groupdict()
        if 'reDate' in grpMap:
            date = m.group('reDate')
            print('date={}'.format(date))
            tags.append(date)
    return tags

def findString(s, cres, key, pattern):
    if key not in cres:
        cres[key] = re.compile(pattern)
    return cres[key].search(s)

def printn(msg='', sep=' ', end='\n', file=sys.stdout, flush=False):
    print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()


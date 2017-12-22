#Funktional Family At Kiss The Sky Batavia IL 12-03-17 (Camera 1)
import os, sys, re

cres = {}
#reVenue      = r'(?P<reVenue>\S+\s)+'
reDate       = r'\s*(?P<reDate>\d{1,2}-\d{1,2}-\d{2})\s*'

def main():
    with open('tags.txt', 'w') as outFile:
        with open('titles.txt', 'r') as inFile:
            getTitles(inFile, outFile)
        print('inFile={}'.format(inFile))
        inFile = None
        print('inFile={}'.format(inFile))
    print('outFile={}'.format(outFile))
    outFile = None
    print('outFile={}'.format(outFile))

def getTitles(inFile, outFile):
    for line in inFile:
        title = line.rstrip('\n')
        printn("title = [{}]".format(title), file=outFile)
        tags = getTags(title, outFile)
        printn("tags = {", file=outFile)
        for k in tags.keys(): printn('    {} => {},'.format(k, tags[k]), file=outFile)
        printn("}", file=outFile)

def getTags(title, outFile):
    title = title.title()
    tags = {}
    tags['Title'] = title
    words = title.split()
    printn('words = [', file=outFile, end='')
    for w in words:
        w = w.rstrip(',')
#        tags.append(w)
        printn(' {}'.format(w), file=outFile, end='')
    printn(']', file=outFile)
    remainder = parse(title, ' At ', ['Name'], tags, outFile)
    remainder = parse(remainder, ', ', ['Venue', 'City'], tags, outFile)
#    printn('Remainder = {}'.format(remainder), file=outFile)
    getDate(remainder, tags, outFile)
    return tags

def parse(s, delim, keys, tags, outFile):
    max = len(keys)
    tokens = s.split(delim, max+1)
#    printn('parse(delim = [{}], keys = {})'.format(delim, keys), file=outFile)
    printn('parse([{}], delim = [{}], keys = ['.format(s, delim), file=outFile, end='')
    if max >= 1: 
        tags[keys[0]] = tokens[0]
        printn('{}'.format(keys[0]), file=outFile, end='')
    for i in range(1, max):
        tags[keys[i]] = tokens[i]
        printn(' {}'.format(keys[i]), file=outFile, end='')
    printn('])', file=outFile)
    for i in range(0, max):
        printn('    [{}], {} = {}'.format(i, keys[i], tokens[i]), file=outFile)
    i += 1
    remainder = tokens[-1]
    printn('    [{}], {} = {}'.format(i, 'Remainder', tokens[i]), file=outFile)
    return remainder

def getDate(dStr, tags, outFile):
    m = findString(dStr, cres, 'reDate', reDate)
    if m:
        print('m={}'.format(m))
        grpMap = m.groupdict()
        if 'reDate' in grpMap:
            date = m.group('reDate')
            print('    date = {}'.format(date), file=outFile)
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


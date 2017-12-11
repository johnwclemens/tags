#Funktional Family At Kiss The Sky Batavia IL 12-03-17 (Camera 1)
import os, sys, re

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
    return tags

def printn(msg='', sep=' ', end='\n', file=sys.stdout, flush=False):
    print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()


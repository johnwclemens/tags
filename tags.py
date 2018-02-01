import os, sys, re, collections, inspect

libPath = os.path.abspath('..\lib')
if libPath not in sys.path:
    sys.path.insert(0, libPath)
import jwc_cmdArgs

#myLibPath = os.path.abspath('..\lib')
#print('myLibPath={}'.format(myLibPath))
#if myLibPath not in sys.path:
#    sys.path.insert(0, myLibPath)
#import jwc_cmdArgs
#print('jwc_cmdArgs={}'.format(jwc_cmdArgs))

def main():
    tags = Tags(inFileName='titles.txt', outFileName='tags.txt')
    tags.run()

class Tags(object):
    def __init__(self, inFileName = 'titles.txt', outFileName='tags.txt'):
        self.tags = None
        self.len = 0
        self.cres = {}
        self.inFileName = inFileName
        self.outFileName = outFileName
        self.reDate = r'\s*(?P<reDate>1[0-2]|0[1-9]|[1-9])-(1[0-9]|2[0-9]|3[0-1]|0[1-9]|[1-9])-(\d{2})\s*'
#        self.initMyLib()
#        self.importMyLib()
        self.getCmdArgs()

    def importMyLib(self):
        myLibPath = os.path.abspath('..\lib')
        print('myLibPath={}'.format(myLibPath))
        if myLibPath not in sys.path:
            sys.path.insert(0, myLibPath)
        import jwc_cmdArgs
        self.jwc_cmdArgs = jwc_cmdArgs
        print('jwc_cmdArgs={}'.format(self.jwc_cmdArgs))

    def getCmdArgs(self):
        self.argMap = {}
#        self.jwc_cmdArgs.parse_cmd_line(self.argMap)
        jwc_cmdArgs.parse_cmd_line(self.argMap)
        print('argMap={}'.format(self.argMap))
        if 'i' in self.argMap and len(self.argMap['i']) > 0:
            self.inFileName = self.argMap['i'][0]
        if 'o' in self.argMap and len(self.argMap['o']) > 0:
            self.outFileName = self.argMap['o'][0]

    def initMyLib(self):
        myLibPath = os.path.abspath('..\lib')
        print('myLibPath={}'.format(myLibPath))
        if myLibPath not in sys.path:
            sys.path.insert(0, myLibPath)
        import jwc_cmdArgs
        print('jwc_cmdArgs={}'.format(jwc_cmdArgs))
        self.argMap = {}
        jwc_cmdArgs.parse_cmd_line(self.argMap)
        print('argMap={}'.format(self.argMap))
        if 'i' in self.argMap and len(self.argMap['i']) > 0:
            self.inFileName = self.argMap['i'][0]
        if 'o' in self.argMap and len(self.argMap['o']) > 0:
            self.outFileName = self.argMap['o'][0]

    def run(self):
        with open(self.outFileName, 'w+') as self.outFile, open(self.inFileName, 'r') as self.inFile:
            self.readFile()
        self.close(self.inFileName, self.inFile)
        self.close(self.outFileName, self.outFile)

    def close(self, fileName, file):
        print('{}={}'.format(fileName, file))
        file = None
        print('{}={}'.format(fileName, file))

    def readFile(self):
        i = 0
        for line in self.inFile:
            self.getTags(line.strip())
            self.printn('tags = [', file=self.outFile)
            for k, v in self.tags.items():
                i += 1
                length = len(v)
                self.len += length
                self.printn('    {:>20}[{:>2}:{:>2}:{:>3}] {}'.format(k, i, length, self.len, v), file=self.outFile)
            self.printn(']\ntags({}) = ['.format(self.len), file=self.outFile, end='')
            for k in self.tags.keys(): self.printn('{}'.format(self.tags[k]), file=self.outFile, end=',')
            self.printn("]", file=self.outFile)
            i = 0
            self.len = 0

    def getTags(self, line):
        self.printn('line = {}'.format(line), file=self.outFile)
        self.tags = collections.OrderedDict()
        title = self.getTitle(line)
        self.addTag('Title', title)
        remainder = self.parse(title, ', ', ['Name', 'Venue', 'City', 'State'])
        remainder = self.getDateAndOther(remainder)
        self.group()

    def addTag(self, key, value):
        self.tags[key] = value

    def parse(self, s, delim, keys):
        max = len(keys)
        tokens = s.split(delim, max+1)
        self.printn('parse([{}], delim = [{}], keys = ['.format(s, delim), file=self.outFile, end='')
        for i in range(0, max):
            self.addTag(keys[i], tokens[i])
            self.printn(' {}'.format(keys[i]), file=self.outFile, end='')
        self.printn('])', file=self.outFile)
        for i in range(0, max):
            self.printn('    [{}], {} = {}'.format(i, keys[i], tokens[i]), file=self.outFile)
        i += 1
        remainder = tokens[-1]
        self.printn('    [{}], {} = {}'.format(i, 'Remainder', tokens[i]), file=self.outFile)
        return remainder

    def getDateAndOther(self, s):
        m = self.reSearch(s, 'reDate', self.reDate)
        if m.start() != 0: self.addTag('Other1', s[:m.start()])
        self.addTag('Date', m.group(1) + '-' + m.group(2) + '-' + m.group(3))
        remainder = s[m.end():]
        if remainder: self.tags['Other2'] = remainder
        return remainder

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

    def reSearch(self, s, key, pattern):
        if key not in self.cres:
            self.cres[key] = re.compile(pattern)
        return self.cres[key].search(s)

    def getTitle(self, s):
#        s = re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)
        s = re.sub(r"[A-Za-z]+('[A-Za-z]+)?", self.titleCase, s)
        return re.sub(r'\((.*?)\)', r'\1', s)

    def titleCase(self, mo):
        if mo.group(0).isupper(): return mo.group(0)
        else: return mo.group(0)[0].upper() + mo.group(0)[1:].lower()

    @staticmethod
    def printn(msg='', sep=' ', end='\n', file=sys.stdout, flush=False):
        print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()

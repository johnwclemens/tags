import os, sys, re, collections

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

    def run(self):
        with open(self.outFileName, 'w') as self.outFile, open(self.inFileName, 'r') as self.inFile:
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
            printn('tags = [', file=self.outFile)
            for k, v in self.tags.items():
                i += 1
                length = len(v)
                self.len += length
                printn('    {:>20}[{:>2}:{:>2}:{:>3}] {}'.format(k, i, length, self.len, v), file=self.outFile)
            printn(']\ntags({}) = ['.format(self.len), file=self.outFile, end='')
            for k in self.tags.keys(): printn('{}'.format(self.tags[k]), file=self.outFile, end=',')
            printn("]", file=self.outFile)
            i = 0
            self.len = 0

    def getTags(self, line):
        printn('line = {}'.format(line), file=self.outFile)
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
        printn('parse([{}], delim = [{}], keys = ['.format(s, delim), file=self.outFile, end='')
        for i in range(0, max):
            self.addTag(keys[i], tokens[i])
            printn(' {}'.format(keys[i]), file=self.outFile, end='')
        printn('])', file=self.outFile)
        for i in range(0, max):
            printn('    [{}], {} = {}'.format(i, keys[i], tokens[i]), file=self.outFile)
        i += 1
        remainder = tokens[-1]
        printn('    [{}], {} = {}'.format(i, 'Remainder', tokens[i]), file=self.outFile)
        return remainder

    def getDateAndOther(self, s):
        m = self.reSearch(s, 'reDate', self.reDate)
        self.addTag('Other1', s[:m.start()])
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
        s = re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)
        return re.sub(r'\((.*?)\)', r'\1', s)

def printn(msg='', sep=' ', end='\n', file=sys.stdout, flush=False):
    print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()

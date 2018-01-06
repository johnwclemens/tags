import os, sys, re

def main():
    tags = Tags(inFileName='titles.txt', outFileName='tags.txt')
    tags.run()

class Tags(object):
    def __init__(self, inFileName = 'titles.txt', outFileName='tags.txt'):
        self.tags = None
        self.cres = {}
        self.inFileName = inFileName
        self.outFileName = outFileName
        self.reDate = r'\s*(?P<reDate>1[0-2]|0[1-9]|[1-9])-(1[0-9]|2[0-9]|3[0-1]|0[1-9]|[1-9])-(\d{2})\s*'

    def run(self):
        with open(self.outFileName, 'w') as self.outFile, open(self.inFileName, 'r') as self.inFile:
            self.getTitles()
        self.close(self.inFileName, self.inFile)
        self.close(self.outFileName, self.outFile)

    def close(self, fileName, file):
        print('{}={}'.format(fileName, file))
        file = None
        print('{}={}'.format(fileName, file))

    def getTitles(self):
        for line in self.inFile:
            self.getTags(line.strip())
            printn('tags = {', file=self.outFile)
            for k in self.tags.keys(): printn('    {:>20} => {},'.format(k, self.tags[k]), file=self.outFile)
            printn("}\ntags({}) = [", file=self.outFile, end='')
            for k in self.tags.keys(): printn('{}'.format(self.tags[k]), file=self.outFile, end=',')
            printn("]", file=self.outFile)

    def getTags(self, line):
        printn('line = {}'.format(line), file=self.outFile)
        self.tags = {}
        title = self.titleCase(line)
        self.tags['Title'] = title
        remainder = self.parse(title, ' At ', ['Name'])
        remainder = self.parse(remainder, ', ', ['Venue', 'City'])
        remainder = self.getStateAndDate(remainder)
        self.group()

    def titleCase(self, s):
        return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)

    def parse(self, s, delim, keys):
        max = len(keys)
        tokens = s.split(delim, max+1)
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

    def getStateAndDate(self, s):
        m = self.findString(s, 'reDate', self.reDate)
        self.tags['Date'] = m.group(1) + '-' + m.group(2) + '-' + m.group(3)
        self.tags['State'] = s[:m.start()]
        remainder = s[m.end():]
        if remainder: self.tags['Other'] = remainder
        return remainder

    def group(self):
        self.tags['Name_City'] = self.tags['Name'] + " " + self.tags['City']
        self.tags['Name_Date'] = self.tags['Name'] + " " + self.tags['Date']
        self.tags['Name_Venue'] = self.tags['Name'] + " " + self.tags['Venue']
        self.tags['Name_Venue_City'] = self.tags['Name'] + " " + self.tags['Venue'] + " " + self.tags['City']
        self.tags['Name_Venue_Date'] = self.tags['Name'] + " " + self.tags['Venue'] + " " + self.tags['Date']
        self.tags['Name_City_Date'] = self.tags['Name'] + " " + self.tags['City'] + " " + self.tags['Date']
        self.tags['City_Date'] = self.tags['City'] + " " + self.tags['Date']
        self.tags['Venue_Date'] = self.tags['Venue'] + " " + self.tags['Date']

        self.tags['Name_City_Live'] = self.tags['Name'] + " Live " + self.tags['City']
        self.tags['Name_Date_Live'] = self.tags['Name'] + " Live " + self.tags['Date']
        self.tags['Name_Venue_Live'] = self.tags['Name'] + " Live " + self.tags['Venue']
        self.tags['Name_Venue_Date_Live'] = self.tags['Name'] + " Live " + self.tags['Venue'] + " " + self.tags['Date']

    def findString(self, s, key, pattern):
        if key not in self.cres:
            self.cres[key] = re.compile(pattern)
        return self.cres[key].search(s)

def printn(msg='', sep=' ', end='\n', file=sys.stdout, flush=False):
    print(msg, sep=sep, end=end, file=file, flush=flush)

if __name__ == "__main__":
    main()

#    words = title.split()
#    printn('words = [', file=self.outFile, end='')
#    for w in words:
#        w = w.strip('),(')
##        self.tags.append(w)
#        printn(' {}'.format(w), file=self.outFile, end='')
#    printn(']', file=self.outFile)
##    self.tags['Title'] = ' '.join(words)

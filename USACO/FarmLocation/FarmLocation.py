import sys
import os.path
sys.path.insert(0, os.path.abspath('..\..\..\lib'))
import cmdArgs

def main():
    argMap = {}
    argMap = cmdArgs.parseCmdLine(dbg=0)
    print('argMap={}'.format(argMap))
    inFileNames = argMap['']
    print('inFileNames={}'.format(inFileNames))
    try:
        for f in range(len(inFileNames)):
            with open(inFileNames[f] + '.in', 'r') as inFile:
                print('reading file {}'.format(inFileNames[f]))
                line = inFile.readline().strip()
                tokens = line.split(' ')
                N = int(tokens[0])
                print('{}'.format(N))
                m = inFile.readline().strip()
                print('     {}'.format(m))
                max, imax, jmax = '', 0, 0
                for i in range(N-2):
                    s1, found = '', 0
                    for j in range(i, N-1):
                        s1 = m[i:j+1]
                        if j + 1 < N:
                            s2 = m[j+1:N]
                        k = s2.count(s1)
                        print('{} {} {} {} {}'.format(i, j, s1, s2, k))
                        if found== 0 and k == 0:
                            bgn, end = i, j
                            if len(s1) > len(max): 
                                max, imax, jmax = s1, i, j
                            found = 1
                            print('{} {} {} {}'.format(bgn, end, s1, len(s1)))
                    print('{} {} {} {}'.format(imax, jmax, max, len(max)))
                print('{}'.format(m))
                n, indent = [],''
                for i in range(N-len(max)+1):
                    n.append(m[i:i+len(max)])
                    print('{}{}'.format(indent, m[i:i+len(max)]))
                    indent += ' '
                n.sort()
                for i in n:
                    print('{}'.format(i))
    except FileNotFoundError as e:
        print('init() Exception: {} - {}'.format(e, sys.exc_info()[0]))

if __name__ == "__main__":
    main()

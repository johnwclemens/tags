import sys
import os.path
sys.path.insert(0, os.path.abspath('..\..\..\lib'))
import cmdArgs

def main():
    fileName = 'names.in'
    try:
        with open(fileName, 'r') as inFile:
            print('reading file {}'.format(fileName))
            line = inFile.readline().strip()
            names = line.split(' ')
            print('{} {}'.format(len(names), names))
            names.sort()
            print('{} {}'.format(len(names), names))
    except FileNotFoundError as e:
        print('init() Exception: {} - {}'.format(e, sys.exc_info()[0]))
    argMap = {}
    argMap = cmdArgs.parseCmdLine(dbg=0)
    print('argMap={}'.format(argMap))
    inFileNames = argMap['']
    print('inFileNames={}'.format(inFileNames))
    try:
        for i in range(len(inFileNames)):
            with open(inFileNames[i] + '.in', 'r') as inFile:
                print('reading file {}'.format(inFileNames[i]))
                line = inFile.readline().strip()
                tokens = line.split(' ')
                ruleCnt = int(tokens[0])
                print('{}'.format(ruleCnt))
                matesDict = {}
                for j in range(ruleCnt):
                    line = inFile.readline().strip()
                    tokens = line.split(' ')
                    raw = [tokens[0], tokens[len(tokens)-1]]
                    sorted = list(raw)
                    sorted.sort()
                    if sorted[0] not in matesDict:
                        matesDict[sorted[0]] = [sorted[1]]
                    else:
                        tmp = [matesDict[sorted[0]][0], sorted[1]]
                        tmp.sort()
                        matesDict[sorted[0]] = tmp
                    print('{} => {}'.format(raw, sorted))
                print('{}'.format(matesDict))
                print(names)
                for k in matesDict:
                    print('matesDict[{}]={}'.format(k, matesDict[k]))
                    if len(matesDict[k]) == 1:
                        print('    len=1, moving {} to after {}'.format(matesDict[k][0], k))
                        names.remove(matesDict[k][0])
                        names.insert(names.index(k) + 1, matesDict[k][0])
                    elif len(matesDict[k]) == 2:
                        print('    len=2, moving {} to between {} and {}'.format(k, matesDict[k][0], matesDict[k][1]))
                        names.remove(k)
                        names.insert(names.index(matesDict[k][1]), k)
                    print(names)
    except FileNotFoundError as e:
        print('init() Exception: {} - {}'.format(e, sys.exc_info()[0]))

if __name__ == "__main__":
    main()

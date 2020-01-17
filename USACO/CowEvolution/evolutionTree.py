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
                numLeaves = int(inFile.readline().strip().split(' ')[0])
                print('numLeaves={}'.format(numLeaves))
                traitDict = {}
                leaves = []
                for i in range(numLeaves):
                    line = inFile.readline().strip()
                    tokens = line.split(' ')
                    traitList = tokens[1:]
                    leaves.append(traitList)
                    for t in traitList:
                        if t in traitDict:
                            traitDict[t] = traitDict[t] + 1
                        else:
                            traitDict[t] = 1
                    print('leaf[{}]: nt={} {}'.format(i, tokens[0], traitList))
                print('traitDict={}'.format(traitDict))
                print('leaves={}'.format(leaves))
    except FileNotFoundError as e:
        print('init() Exception: {} - {}'.format(e, sys.exc_info()[0]))

if __name__ == "__main__":
    main()

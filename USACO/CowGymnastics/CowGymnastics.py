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
                K = int(tokens[0])
                N = int(tokens[1])
                cowList = []
                print('K={}, N={}'.format(K, N))
                for i in range(K):
                    line = inFile.readline().strip()
                    tokens = line.split(' ')
                    print('{} {}'.format(i, tokens))
                    tmp = []
                    for k in range(len(tokens)):
                        tmp.append(int(tokens[k]))
                    cowList.append(tmp)
                print('{}'.format(cowList))
                for i in range(K):
                    for j in range(N):
                        print('{}'.format(cowList[i][j]), end=' ')
                    print()
                pairs = []
                for i in range(K):
                    tmp = []
                    for j in range(N-1):
                        for k in range(j, N-1):
                            p = [cowList[i][j], cowList[i][k+1]]
                            tmp.append(p)
                            print('[{} {}]'.format(p[0], p[1]), end=' ')
                    pairs.append(tmp)
                    print()
                for i in range(K):
                    print('{} {}'.format(i, pairs[i]))
                found = 0
                for j in range(len(pairs[0])):
                    cnt = 0
                    for i in range(1, K):
                        if pairs[0][j] in pairs[i]:
                            cnt += 1
                    print('{} checking {}'.format(j, pairs[0][j]))
                    if cnt == K -1:
                        found += 1
                        print('{} found {}'.format(j, pairs[0][j]))
                print('found {} pairs'.format(found))
    except FileNotFoundError as e:
        print('init() Exception: {} - {}'.format(e, sys.exc_info()[0]))

if __name__ == "__main__":
    main()

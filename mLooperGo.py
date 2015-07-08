#!/usr/bin/env python
import subprocess
import sys

# ARGUMENTS:
# first-> number of runs to process (if 0 then run all)
# second-> number of runs to skip before starting processing.

nRuns = int(sys.argv[1])
nStart = int(sys.argv[2])

if nRuns > 0:
    print "Number of runs to process = ", nRuns
else:
    print "Processing all runs in list"

fid = open('../runLists/cl_all-list', 'r')
runList = []
for line in fid.readlines():
    for i in line.split():
        runList.append(int(i))

fid.close()

if nRuns > 0:
    endRun = nRuns + nStart
else:
    endRun = None
    nRuns = len(runList)

for x in runList[nStart:endRun]:
    tmp = 'Processing ' + str(x - runList[nStart] + 1) + 'out of ' +str(nRuns)
    print tmp
    runFile = '-L../runFiles/runFile.' + str(x) + '.list'
    outFile = ' ../rootFiles/massHistos/plotsHSWG.' + str(x) + '.root'
    print "Run Number = ", x
    results = subprocess.call(['mLooperV1', runFile, outFile])

sys.exit()

import csv
import os
import re

rootdir = "C:/Users/encore/Documents/VisualProject/OperandGenerator"
regex = re.compile('(^Distribution\ PLC\ IO\ Used\ Only\ -\ .+\.csv$)')

targetSim = "duplicated"
macroBin = "InOperandGenerator"
macroDec ="InOperandGeneratorDecimal"
operand = "in"


componentFiles = []

for root, dirs, files in os.walk(rootdir):
  for file in files:
    if regex.match(file):
       print(file)
       componentFiles.append(file)

print(componentFiles)

firstline = [
    "line number", "Symbol", "", "", "", "", "", "", "", "", "", "",
    "", "macro name", "standard", "macro type", "user 1", "user 2",
    "user 3", "macro signal", "x-position of group", "y-position of group",
    "width of group", "height of group", "target file name"
]


for componentFile in componentFiles:
    pattern = r"Distribution\ PLC\ IO\ Used\ Only\ -\ (.+)\.csv"
    match = re.search(pattern, componentFile)
    componentName = match.group(1)
    print(componentName)

    currentFile = componentName + ".csv"
    print(currentFile)

    line = 2

    list_I = []
    list_Q = []
    list_IW = []

    with open(componentFile, 'r') as csvfileread:
        csvreader = csv.reader(csvfileread)
        for row in csvreader:
        # Check if the row has at least 4 values and process accordingly
            if len(row) >= 4:
                if row[3].startswith("%IW"):
                    list_IW.append(row[0])
                elif row[3].startswith("%Q"):
                    list_Q.append(row[0])
                elif row[3].startswith("%I"):
                    list_I.append(row[0])
        print(list_I)
        print(list_Q)
        print(list_IW)

    with open(currentFile, 'w', newline='') as csvfilewrite:
        csvwriter = csv.writer(csvfilewrite)
        csvwriter.writerow(firstline)
        for iIndex, i in enumerate(list_I):
            row = [line, i, "", "", "", "", "", "", "", "", "", "", "", macroBin + str(line-1), "", macroBin, "", "", "", operand, "0", 65 + (iIndex * 35), "650", "35", targetSim]
            csvwriter.writerow(row)
            line += 1

        for iwIndex, iw in enumerate(list_IW):
            row = [line, iw, "", "", "", "", "", "", "", "", "", "", "", macroDec + str(line-1), "", macroDec, "", "", "", operand, "0", 65 + (iIndex * 35) + (iwIndex * 70), "650", "70", targetSim]
            csvwriter.writerow(row)
            line += 1

        for qIndex, q in enumerate(list_Q):
            row = [line, q, "", "", "", "", "", "", "", "", "", "", "", macroBin + str(line-1), "", macroBin, "", "", "", operand, "1290", 65 + (qIndex * 35), "650", "35", targetSim]
            csvwriter.writerow(row)
            line += 1
#python 2
import sys

#File input
fileInput = open(sys.argv[1], "r")

#File output
fileOutput = open(sys.argv[2], "w")

count = 1

for strLine in fileInput:
    if (strLine.startswith("A") or strLine.startswith("C") or strLine.startswith("G") or strLine.startswith("T")):
        fileOutput.write(strLine)
        count = count + 1

#Close the input and output file
fileInput.close()
fileOutput.close()

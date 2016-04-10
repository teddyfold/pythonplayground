# Following line opens a file and read it

filePath="sample.txt"

def readSampleFile():

    file = open(filePath)
    print file.read()

    # reset file to byte 0
    file.seek(0)

    # read all lines, and return array
    print file.readlines()

    file.seek(0)
    lineCount = 1;

    # read line in loop
    for line in file:
        print "{lineCount}:\t{line}".format(lineCount=lineCount, line=line)
        lineCount += 1


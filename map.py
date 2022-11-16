# read data from file
def read(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


# convert lines to array
def convertLinesToArray(lines):
    array = []
    for line in lines:
        array += list(line.strip().upper())
    return array


# DNA sequence to EIIP mapping
def mapEIIP(array):
    arr = []
    for i in array:
        if i == 'G':
            arr.append(0.0806)
        elif i == 'A':
            arr.append(0.1260)
        elif i == 'T':
            arr.append(0.1335)
        elif i == 'C':
            arr.append(0.1340)
    return arr


def process(path):
    lines = read(path)
    array = convertLinesToArray(lines)
    arr = mapEIIP(array)
    return arr

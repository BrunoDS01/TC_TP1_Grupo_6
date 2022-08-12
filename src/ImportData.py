
def readSpiceData(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()

    freq = []
    mag = []
    phase = []

    for i in range(1, len(lines)):
        line = lines[i].split('\t')
        freq.append(float(line[0]))

        aux = line[1]
        magAndPhase = aux.split(',')
        mag.append(float(magAndPhase[0][1:-2]))
        phase.append(float(magAndPhase[1][:-3]))

    return freq, mag, phase








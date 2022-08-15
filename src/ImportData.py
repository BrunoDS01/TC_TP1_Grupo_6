
def readSpiceBode(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()

    # Empezamos a guardar datos cuando el primer caracter de un renglón sea un número

    numberCharacters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+'}

    while lines[0][0] not in numberCharacters:
        lines.pop(0)

    # Guardamos los datos
    freq = []
    mag = []
    phase = []

    for i in range(len(lines)):
        line = lines[i].split('\t')
        freq.append(float(line[0]))

        aux = line[1]
        magAndPhase = aux.split(',')
        mag.append(float(magAndPhase[0][1:-2]))
        phase.append(float(magAndPhase[1][:-3]))

    return freq, mag, phase

def readSpiceTime(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()

    # Empezamos a guardar datos cuando el primer caracter de un renglón sea un número

    numberCharacters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+'}

    while lines[0][0] not in numberCharacters:
        lines.pop(0)

    # Guardamos los datos
    numberOfSignals = len(lines[0].split('\t'))

    data = []
    for j in range(numberOfSignals):
        data.append([])

    for i in range(len(lines)):
        line = lines[i].split('\t')
        for j in range(numberOfSignals):
            line[j] = line[j].replace('\n', '')
            if(line[j] == ''):
                data[j].append(0.0)
            else:
                data[j].append(float(line[j]))

    return data

def readCSVBode(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()

    # Empezamos a guardar datos cuando el primer caracter de un renglón sea un número
    numberCharacters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+'}

    while lines[0][0] not in numberCharacters:
        lines.pop(0)

    # Guardamos los datos
    freq = []
    mag = []
    phase = []

    for i in range(len(lines)):
        line = lines[i].split(',')
        freq.append(float(line[0]))
        mag.append(float(line[1]))
        phase.append(float(line[2].replace('n', '')))

    return freq, mag, phase

def readCSVTime(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()

    # Empezamos a guardar datos cuando el primer caracter de un renglón sea un número

    numberCharacters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+'}

    while lines[0][0] not in numberCharacters:
        lines.pop(0)

    # Guardamos los datos
    numberOfSignals = len(lines[0].split(','))

    data = []
    for j in range(numberOfSignals):
        data.append([])

    for i in range(len(lines)):
        line = lines[i].split(',')
        for j in range(numberOfSignals):
            line[j] = line[j].replace('\n', '')
            if(line[j] == ''):
                data[j].append(0.0)
            else:
                data[j].append(float(line[j]))

    return data






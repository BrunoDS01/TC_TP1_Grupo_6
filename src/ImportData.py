
def readSpiceBode(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()

    # Empezamos a guardar datos cuando el primer caracter de un renglón sea un número

    numberCharacters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+', 'e', 'E'}

    while lines[0][0] not in numberCharacters:
        lines.pop(0)

    # Guardamos los datos
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

def readCSVBode(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()

    # Empezamos a guardar datos cuando el primer caracter de un renglón sea un número

    numberCharacters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+', 'e', 'E'}

    while lines[0][0] not in numberCharacters:
        lines.pop()

    # Guardamos los datos
    freq = []
    mag = []
    phase = []

    for i in range(1, len(lines)):
        line = lines[i].split(',', ' ', '\t')
        line.remove('\n')
        freq.append(float(line[0]))
        mag.append(float(line[1]))
        phase.append(float(line[2]))

    return freq, mag, phase








cube = [0] * 54


def setColor(side, item, color):
    cube[side * 9 + item] = color

def getColor(side, item):
    return cube[side * 9 + item]

def shuffleCube():
    for i in range(54):
        cube[i] = int(i % 9)

def arrangeCube():
    for i in range(54):
        cube[i] = int(i / 9)

def rotate(side, direction):
    for i in range(9)
    cube[side * i] = cube[side * i]


arrangeCube()
print (cube)
print (getColor(1, 1))


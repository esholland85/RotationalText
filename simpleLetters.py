from findingPoints import *
def stringToPoints(raw):
    text = raw.upper()

current_letters = {}

def getLetter(a):
    #only does upper case for now
    try:
        return current_letters[a.upper()]
    except:
        print(f"Missing letter {a.upper()}")
        return current_letters['_']

class pixelLetter:
    def __init__(self, lookupChar, drawInstructions):
        self.name = lookupChar
        self.orientations = []
        self.orientations.append(drawInstructions)
        current_letters[lookupChar] = self
        #for now, relative center is an assumed 0,0

    def __str__(self):
        for list in self.orientations:
            print(list)
        return f"The current data representing {self.name}."

    #if draw instructions exist, get them, otherwise create them for every rotation up to the point requested
    def getDraw(self, orientation = 0):
        #get length early and use the same, consistent number throughout, both to make it cleaner to read, and to avoid accidentally changing which int it's working with as calculations are made.
        if orientation > 7:
            orientation = orientation%8
        if len(self.orientations) > orientation:
            return self.orientations[orientation]
        else:
            for i in range(len(self.orientations),orientation+1):
                result = []
                for stroke in self.orientations[i-1]:
                    stroke_directions = []
                    for point in stroke:
                        stroke_directions.append(rotateRight(*point))
                    result.append(stroke_directions)
                self.orientations.append(result)
            return self.orientations[orientation]
    

letter_underscore = pixelLetter('_',[[(-7,10),(7,10)]])
letter_A = pixelLetter('A',[[(-7,10),(0,-10),(7,10)],[(-4,3),(4,3)]])
letter_B = pixelLetter('B',[[(-7,10),(-7,-10),(0,-10),(4,-7),(4,-3),(0,0),(-7,0)],[(0,0),(4,3),(4,7),(0,10),(-7,10)]])
letter_C = pixelLetter('C',[[(5,-6),(2,-9),(0,-10),(-2,-9),(-5,-5),(-7,0),(-5,5),(-2,9),(0,10),(2,9),(5,6)]])
letter_D = pixelLetter('D',[[(2,-9),(0,-10),(-7,-10),(-7,10),(0,10),(2,9),(5,5),(7,0),(5,-5),(2,-9)]])
letter_E = pixelLetter('E',[[(4,-10),(-7,-10),(-7,10),(4,10)],[(-7,0),(0,0)]])
letter_F = pixelLetter('F',[[(4,-10),(-7,-10),(-7,10)],[(-7,0),(0,0)]])
letter_G = pixelLetter('G',[[(5,-6),(2,-9),(0,-10),(-2,-9),(-5,-5),(-7,0),(-5,5),(-2,9),(0,10),(2,9),(5,6),(5,0),(0,0)]])
letter_H = pixelLetter('H',[[(-6,-10),(-6,10)],[(6,-10),(6,10)],[(-6,0),(6,0)]])
letter_I = pixelLetter('I',[[(-5,-10),(5,-10)],[(-5,10),(5,10)],[(0,-10),(0,10)]])
letter_J = pixelLetter('J',[[(-5,-10),(7,-10)],[(2,-10),(2,7),(1,9),(0,10),(-2,10),(-3,9),(-4,7),(-5,5)]])
letter_K = pixelLetter('K',[[(-7,-10),(-7,10)],[(0,-10),(-7,0),(0,10)]])
letter_L = pixelLetter('L',[[(-7,-10),(-7,10),(4,10)]])
letter_M = pixelLetter('M',[[(-7,10),(-7,-10),(0,2),(7,-10),(7,10)]])
letter_N = pixelLetter('N',[[(-5,10),(-5,-10),(5,10),(5,-10)]])
letter_O = pixelLetter('O',[[(2,-9),(0,-10),(-2,-9),(-5,-5),(-7,0),(-5,5),(-2,9),(0,10),(2,9),(5,5),(7,0),(5,-5),(2,-9)]])
letter_P = pixelLetter('P',[[(-7,10),(-7,-10),(0,-10),(4,-7),(4,-3),(0,0),(-7,0)]])
letter_Q = pixelLetter('Q',[[(2,-9),(0,-10),(-2,-9),(-5,-5),(-7,0),(-5,5),(-2,9),(0,10),(2,9),(5,5),(7,0),(5,-5),(2,-9)],[(2,3),(7,10)]])
letter_R = pixelLetter('R',[[(-7,10),(-7,-10),(0,-10),(4,-7),(4,-3),(0,0),(-7,0)],[(0,0),(4,10)]])
letter_S = pixelLetter('S',[[(5,-7),(2,-10),(-2,-10),(-5,-7),(-4,-4),(4,4),(5,7),(2,10),(-2,10),(-5,7)]])
letter_T = pixelLetter('T',[[(-7,-10),(7,-10)],[(0,-10),(0,10)]])
letter_U = pixelLetter('U',[[(-6,-10),(-6,8),(-5,10)],[(6,-10),(6,8),(5,10)],[(-5,10),(5,10)]])
letter_V = pixelLetter('V',[[(-6,-10),(0,10),(6,-10)]])
letter_W = pixelLetter('W',[[(-7,-10),(-7,10),(0,-2),(7,10),(7,-10)]])
letter_X = pixelLetter('X',[[(-7,-10),(7,10)],[(-7,10),(7,-10)]])
letter_Y = pixelLetter('Y',[[(-7,-10),(0,0),(7,-10)],[(0,0),(0,10)]])
letter_Z = pixelLetter('Z',[[(-7,-10),(7,-10),(-7,10),(7,10)]])
letter_O = pixelLetter('0',[[(2,-9),(0,-10),(-2,-9),(-5,-5),(-7,0),(-5,5),(-2,9),(0,10),(2,9),(5,5),(7,0),(5,-5),(2,-9)],[(-3,7),(3,-7)]])
letter_1 = pixelLetter('1',[[(0,-10),(0,10)]])
letter_2 = pixelLetter('2',[[(-5,-7),(-2,-10),(2,-10),(5,-7),(4,-4),(-5,10),(5,10)]])
letter_3 = pixelLetter('3',[[(-4,-10),(7,-10),(7,10),(-4,10)],[(7,0),(0,0)]])
letter_4 = pixelLetter('4',[[(2,10),(2,-10),(-5,4),(6,4)]])
letter_5 = pixelLetter('5',[[(6,-10),(-6,-10),(-6,-2),(1,-1),(3,0),(4,5),(5,7),(2,10),(-2,10),(-6,7)]])
letter_6 = pixelLetter('6',[[(5,0),(5,7),(2,10),(-2,10),(-5,7),(-4,4),(-4,0),(0,-2),(5,0)],[(-4,0),(-4,-5),(-1,-10),(5,-10)]])
letter_7 = pixelLetter('7',[[(-7,-10),(7,-10),(-7,10)]])
letter_8 = pixelLetter('8',[[(5,-7),(2,-10),(-2,-10),(-5,-7),(-4,-4),(4,4),(5,7),(2,10),(-2,10),(-5,7),(-4,4),(4,-4),(5,-7)]])
letter_9 = pixelLetter('9',[[(-5,0),(-5,-7),(-2,-10),(2,-10),(5,-7),(4,-4),(4,0),(0,2),(-5,0)],[(4,0),(4,5),(1,10),(-5,10)]])
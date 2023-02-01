def findPoint(x,y):
    num_found = 0
    if 0 == x and 0 == y:
        num_found += 1
        return 0
    if 0 <= x and 0 <= y and x < y:
        num_found += 1
        return 1
    if 0 < x and 0 < y and x >= y:
        num_found += 1
        return 2
    if 0 < x and 0 >= y and x > -y:
        num_found += 1
        return 3
    if 0 < x and 0 >= y and x <= -y:
        num_found += 1
        return 4
    if 0 >= x and 0 > y and x > y:
        num_found += 1
        return 5
    if 0 > x and 0 > y and x <= y:
        num_found += 1
        return 6
    if 0 > x and 0 <= y and -x > y:
        num_found += 1
        return 7
    if 0 > x and 0 < y and -x <= y:
        num_found += 1
        return 8

    if num_found == 0:
        raise Exception ("not found in the grid")
    if num_found > 1:
        raise Exception ("located in multiple octants")

def rotateRight(x,y):
    current_octant = findPoint(x,y)
    if current_octant == 0:
        return x,y
    #attempting to simplify to even/odd octants
    if current_octant%2 == 1:
        a = y + x
        b = y - x
        return a,b
    if current_octant%2 == 0:
        b = (y - x)/2
        a = x + b
        return a,b

#begin/end points of letters will need to be on coordinates with an even difference between x/y, at least in octants whose '0' line is diagonal
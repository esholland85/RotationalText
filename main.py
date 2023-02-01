from findingPoints import *
from simpleLetters import *
from tkinter import Tk, BOTH, Canvas

class Window:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        #create a root widget using Tk() and save it as a data member
        self.root = Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        #set widget.title to something
        self.root.title("Text Display")
        #attach window "x" to close method
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        #create a Canvas and save it as a data member
        self.background = Canvas(self.root,width = self.width,height = self.height)
        #Pack the canvas to be drawn
        self.background.pack()

    #create a bool that represents the window running = False
    is_window_running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        print("running")
        self.is_window_running = True
        while self.is_window_running:
            self.redraw()
    
    def close(self):
        self.is_window_running = False
        self.root.quit()
        self.root.destroy()
        print("Shutting Down")

    def draw_line(self, line, fill_color = 'red'):
        line.draw(self.background,fill_color)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"

class Line:
    def __init__(self,point_a, point_b):
        self.a = point_a
        self.b = point_b

    def draw(self,canvas,fill_color):
        canvas.create_line(self.a.x,self.a.y,self.b.x,self.b.y, fill = fill_color, width = 2)
        canvas.pack()

    def rotateLine(self, center_x = 0, center_y = 0):
        #put coordinates in terms of a point to rotate around
        print(f"Absolute coordinates of point A: {self.a}")
        print(f"Absolute coordinates of point B: {self.b}")
        relative_a_x = self.a.x - center_x
        relative_a_y = self.a.y - center_y

        relative_b_x = self.b.x - center_x
        relative_b_y = self.b.y - center_y
        
        print(f"Relative coordinates of point A: ({relative_a_x},{relative_a_y})")
        print(f"Relative coordinates of point B: ({relative_b_x},{relative_b_y})")

        #rotate both ends of the line around that point
        relative_a_x, relative_a_y = rotateRight(relative_a_x,relative_a_y)
        relative_b_x, relative_b_y = rotateRight(relative_b_x,relative_b_y)

        print(f"Relative point A after rotating: ({relative_a_x},{relative_a_y})")
        print(f"Relative point B after rotating: ({relative_b_x},{relative_b_y})")

        #adjust for y = 0 being at the top instead of the bottom:
        #positive y values go down and negative y values go up; this currently results in a left rotation instead of right.
        relative_a_x += center_x
        relative_a_y += center_y
        relative_b_x += center_x
        relative_b_y += center_y

        print(f"Normalized A: ({relative_a_x},{relative_a_y})")
        print(f"Normalized B: ({relative_b_x},{relative_b_y})")

        if relative_a_x < 0 or relative_a_y < 0 or relative_b_x < 0 or relative_b_y < 0:
            raise Exception("Rotation is too close to the wall, use a center point further away")

        #record line's new position in local terms
        self.a = Point(relative_a_x, relative_a_y)
        self.b = Point(relative_b_x, relative_b_y)

def drawLetter(a, target_window, offset = (10,10),rotation = 0,color = "black"):
    letter_object = getLetter(a)
    x_offset, y_offset = offset
    print_directions = letter_object.getDraw(rotation)
    for list in print_directions:
        if len(list) == 1:
            point_a = Point(*list[0])
            point_b = Point(*list[0])
            point_a.x += x_offset
            point_a.y += y_offset
            point_b.x += x_offset
            point_b.y += y_offset
            temp_line = Line(point_a,point_b)
            target_window.draw_line(temp_line)
        else:
            for i in range(1, len(list)):
                point_a = Point(*list[i-1])
                point_b = Point(*list[i])
                point_a.x += x_offset
                point_a.y += y_offset
                point_b.x += x_offset
                point_b.y += y_offset
                #print(f"drawing from {point_a} to {point_b}")
                temp_line = Line(point_a,point_b)
                target_window.draw_line(temp_line,color)

def drawString(text, target_window, position = (10,10),rotation = 0,color = "black"):
    x_position, y_position = position
    x_step = 20
    y_step = 0

    rotation = rotation%8

    if rotation == 1:
        x_step = 20
        y_step = -20
    elif rotation == 2:
        x_step = 0
        y_step = -20
    elif rotation == 3:
        x_step = -20
        y_step = -20
    elif rotation == 4:
        x_step = -20
        y_step = 0
    elif rotation == 5:
        x_step = -20
        y_step = 20
    elif rotation == 6:
        x_step = 0
        y_step = 20
    elif rotation == 7:
        x_step = 20
        y_step = 20

    for i in range(0,len(text)):
        drawLetter(text[i],target_window,(x_position + x_step*i,y_position + y_step*i),rotation,color)

def main():
    my_window = Window(1600,1200)

    drawString('ESH',my_window,(20,20),0,'black')
    drawString('ESH',my_window,(25,25),0,'blue')
    drawString('ESH',my_window,(30,30),0,'red')

    for i in range(0,8):
        drawString('raymond',my_window,(200,200),i,'cyan')

    my_window.wait_for_close()

main()
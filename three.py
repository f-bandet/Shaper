### 
### Author: Faye Bandet
### Course: CSC 110
### Description: This is a program with three shapes moving across the screen.
###
from graphics import graphics
import random
def main():
    gui = graphics(600, 600, 'Three Shapes')
    x_coordinate = 0
    y_coordinate = 0
    y1 = 0
    y_coordinate = random.randint(60, 600)
    y2 = y_coordinate + 60
    i = 0
    rec_x_coordinate = -30
    rec_y_coordinate = 0
    ell_x_coordinate = 0
    ell_y_coordinate = 0
    while True:
        gui.clear()
        i += 1
###Rectangle
        gui.rectangle( rec_x_coordinate, rec_y_coordinate, 60, 60, 'dark orange')
        rec_x_coordinate += 15 ### Movement sideways
        
        if rec_x_coordinate > 650:
            rec_x_coordinate = 0
            rec_y_coordinate = random.randint(60, 600) ### Random Y Coordinate
###Ellipse
        gui.ellipse( ell_x_coordinate, ell_y_coordinate, 60, 60, 'light coral')
        ell_x_coordinate += 15 ### Movement sideways
        
        if ell_x_coordinate > 650:
            ell_x_coordinate = 0
            ell_y_coordinate = random.randint(60, 600) ### Random Y Coordinate SHOULD NOT BE IN WHILE LOOP
###Triangle
        gui.triangle(x_coordinate, y_coordinate, x_coordinate+30, y_coordinate+60, x_coordinate-30, y_coordinate+60, 'OrangeRed2')
        x_coordinate += 15
        
        if x_coordinate >= 650:
            x_coordinate = 0
            y_coordinate = random.randint(60, 600) ### Random Y Coordinate
            y2 = y_coordinate + 60
        gui.update_frame(30)
main()
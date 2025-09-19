from turtle import Turtle
import random

BALL_MOVEMENT = 20

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.seth(random.randint(0,359))

    def move(self):
        self.forward(BALL_MOVEMENT)
    
    def bounce(self,heading, ycoord):
        if heading > 0 and heading < 90:
            if ycoord > 280:
                offset = 90 - heading
                new_heading = 270 + offset
                self.seth(new_heading)
            else:
                offset = 90 - heading
                new_heading = 90 + offset
                self.seth(new_heading)
        elif heading > 90 and heading < 180:
            if ycoord > 280:
                offset = 180 - heading
                new_heading = 180 + offset
                self.seth(new_heading)
            else:
                new_heading = 180 - heading
                self.seth(new_heading)
        elif heading > 180 and heading < 270:
            if ycoord < -280:
                offset = 270 - heading
                new_heading = 90 + offset
                self.seth(new_heading)
            else:
                offset = 270 - heading
                new_heading = 270 + offset
                self.seth(new_heading)
        elif heading > 270 and heading < 360:
            if ycoord < -280:
                new_heading = 360 - heading
                self.seth(new_heading)
            else:
                offset = 360 - heading
                new_heading = 180 + offset
                self.seth(new_heading)

    def reset(self):
        self.teleport(0,0)
        self.seth(random.randint(0,359))
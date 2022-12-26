
# 도전
from turtle import *
import random

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car.gif")
    def drive(self):
        self.turtle.forward(self.speed)
    def left_turn(self):
        self.turtle.left(90)
    def right_turn(self):
        self.turtle.right(90)


register_shape("car.gif")
fast = random.randint(0, 100)
direction = random.randint(0,1)
myCar = Car(fast, "red", "E-class")
for i in range(100):
    myCar.drive()
    if(direction == 0):
        myCar.left_turn()
    if(direction == 1):
        myCar.right_turn()
    

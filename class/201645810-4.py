# 4

import turtle
import math

input1 = input("x1을 입력하시오.")
input2 = input("y1을 입력하시오.")
input3 = input("x2을 입력하시오.")
input4 = input("y1을 입력하시오.")
result = (int(input1) - int(input3))**2 + (int(input2) - int(input4))**2
output = math.sqrt(result)

turtle.shape("turtle")
turtle.goto(int(input1), int(input2))
turtle.goto(int(input3), int(input4))
turtle.penup()
turtle.write("선의길이 = " + str(output), move = False , align = "left" , font = ( "Arial" , 15 , "normal"))
turtle.done()
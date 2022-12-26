import turtle as t
from turtle import *
import random

# 정의

# 사각형 만들기 함수
def draw_rec(t, x_pos, y_pos, width, height):
    t.penup() 
    t.color(0, 200, 200)
    t.begin_fill()
    t.goto(x_pos, y_pos)
    t.pendown()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.color(0, 0, 0)

# 사각형 정의(x_pos, y_pos -> 왼쪽 상단 모석리)
rec1 = {
    "x_pos" : -325,
    "y_pos" : 250,
    "width" : 650,
    "height" : 50,
}
rec2 = {
    "x_pos" : -325,
    "y_pos" : 200,
    "width" : 500,
    "height" : 50,
}
rec3 = {
    "x_pos" : -175,
    "y_pos" : 150,
    "width" : 200,
    "height" : 100,
}
rec4 = {
    "x_pos" : -25,
    "y_pos" : 50,
    "width" : 50,
    "height" : 100,
}
rec5 = {
    "x_pos" : -325,
    "y_pos" : 50,
    "width" : 50,
    "height" : 100,
}
rec6 = {
    "x_pos" : -325,
    "y_pos" : -50,
    "width" : 200,
    "height" : 100,
}
rec7 = {
    "x_pos" : -325,
    "y_pos" : -150,
    "width" : 650,
    "height" : 100,
}
rec8 = {
    "x_pos" : 125,
    "y_pos" : 50,
    "width" : 150,
    "height" : 200,
}
rec9 = {
    "x_pos" : 275,
    "y_pos" : 100,
    "width" : 50,
    "height" : 250,
}

# 점수 정의
global point
point = 0

# 수명 정의
global life
life = 3


# 벽과 충돌 확인 함수
def check_colli(x_pos, y_pos):
    colli = 0
    if(x_pos >= rec1["x_pos"] <= x_pos <= rec1["x_pos"] + rec1["width"]):
        if(y_pos <= rec1["y_pos"] and y_pos >= rec1["y_pos"] - rec1["height"]):
            colli = 1
    if(x_pos >= rec2["x_pos"] <= x_pos <= rec2["x_pos"] + rec2["width"]):
        if(y_pos <= rec2["y_pos"] and y_pos >= rec2["y_pos"] - rec2["height"]):
            colli = 2
    if(x_pos >= rec3["x_pos"] and x_pos <= rec3["x_pos"] + rec3["width"]):
        if(y_pos <= rec3["y_pos"] and y_pos >= rec3["y_pos"] - rec3["height"]):
            colli = 3
    if(x_pos >= rec4["x_pos"] and x_pos <= rec4["x_pos"] + rec4["width"]):
        if(y_pos <= rec4["y_pos"] and y_pos >= rec4["y_pos"] - rec4["height"]):
            colli = 4
    if(x_pos >= rec5["x_pos"] and x_pos <= rec5["x_pos"] + rec5["width"]):
        if(y_pos <= rec5["y_pos"] and y_pos >= rec5["y_pos"] - rec5["height"]):
            colli = 5
    if(x_pos >= rec6["x_pos"] and x_pos <= rec6["x_pos"] + rec6["width"]):
        if(y_pos <= rec6["y_pos"] and y_pos >= rec6["y_pos"] - rec6["height"]):
            colli = 6
    if(x_pos >= rec7["x_pos"] and x_pos <= rec7["x_pos"] + rec7["width"]):
        if(y_pos <= rec7["y_pos"] and y_pos >= rec7["y_pos"] - rec7["height"]):
            colli = 7
    if(x_pos >= rec8["x_pos"] and x_pos <= rec8["x_pos"] + rec8["width"]):
        if(y_pos <= rec8["y_pos"] and y_pos >= rec8["y_pos"] - rec8["height"]):
            colli = 8
    if(x_pos >= rec9["x_pos"] and x_pos <= rec9["x_pos"] + rec9["width"]):
        if(y_pos <= rec9["y_pos"] and y_pos >= rec9["y_pos"] - rec9["height"]):
            colli = 9

    return colli


# 캔디와의 충돌후 점수 확인 함수
def check_colli_candy(x, y):
    for i in range(0, 20):
        if(candy_x[i] - 23 <= x <= candy_x[i] + 23):
            if(candy_y[i] - 23 <= y <= candy_y[i] + 23):
                candy[i].hide()
                candy_x[i] = -500
                candy_y[i] = -500
                global point
                point += 50
                t.undo()
                t.penup()
                t.goto(-300,200)
                t.pendown()
                t.write("점수 : " + str(point), font=("Arial", 30))


# 벽과 충돌 후 수명 삭제
def check_life():
    global life
    global point
    if(life == 3):
        life3.hide()
        life = 2
        point -= 100
        if(point < 100):
            point = 0
        t.undo()
        t.penup()
        t.goto(-300,200)
        t.pendown()
        t.write("점수 : " + str(point), font=("Arial", 30))
        car.init_again()
    elif(life == 2):
        life2.hide()
        life = 1
        point -= 100
        if(point < 100):
            point = 0
        t.undo()
        t.penup()
        t.goto(-300,200)
        t.pendown()
        t.write("점수 : " + str(point), font=("Arial", 30))
        car.init_again()
    elif(life == 1):
        life1.hide()
        life = 0
        point -= 100
        if(point < 100):
            point = 0
        t.undo()
        t.penup()
        t.goto(-300,200)
        t.pendown()
        t.write("점수 : " + str(point), font=("Arial", 30))
        car.init_again()
    else:
        t.clear()
        for i in range(0, 20):
            candy[i].hide()
        car.hide()
        t.penup()
        t.goto(-90,0)
        t.pendown()
        t.write("점수 : " + str(point), font=("Arial", 50))


                
                

# 캔디 클래스
class Candy:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.turtle = Turtle()
        self.turtle.shape("candy.gif")
        self.turtle.penup()
        self.turtle.goto(x_pos, y_pos)
    def hide(self):
        self.turtle.hideturtle()


# 수명 클래스
class Life:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.turtle = Turtle()
        self.turtle.shape("car_u.gif")
        self.turtle.penup()
        self.turtle.goto(x_pos, y_pos)
    def hide(self):
        self.turtle.hideturtle()
        

# 자동차 클래스
class Car:
    def __init__(self, img_file, speed, location):
        self.turtle = Turtle()
        self.img_file = img_file
        self.turtle.shape(img_file[0])
        self.turtle.speed(speed)
        self.turtle.penup()
        self.turtle.goto(location)
    def init_again(self):
        self.turtle.goto(-315, 90)
    def hide(self):
        self.turtle.hideturtle()
    
    def left(self):
        if(self.turtle.shape() == "car_d.gif"):
            self.turtle.shape(self.img_file[1])
            self.turtle.right(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        elif(self.turtle.shape() == "car_u.gif"):
            self.turtle.shape(self.img_file[1])
            self.turtle.left(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        elif(self.turtle.shape() == "car_r.gif"):
            self.turtle.shape(self.img_file[1])
            self.turtle.right(180)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        else:
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

    def right(self):
        if(self.turtle.shape() == "car_d.gif"):
            self.turtle.shape(self.img_file[0])
            self.turtle.left(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()
            if(x + 30 > 325):
                t.undo()
                t.penup()
                t.goto(-300,200)
                t.pendown()
                t.write("성공!! 최종점수 : " + str(point), font=("Arial", 30))

        elif(self.turtle.shape() == "car_u.gif"):
            self.turtle.shape(self.img_file[0])
            self.turtle.right(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()
            if(x + 30 > 325):
                print("게임 종료")
                t.undo()
                t.penup()
                t.goto(-300,200)
                t.pendown()
                t.write("성공!! 최종점수 : " + str(point), font=("Arial", 30))

        elif(self.turtle.shape() == "car_l.gif"):
            self.turtle.shape(self.img_file[0])
            self.turtle.right(180)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()
            if(x + 30 > 325):
                print("게임 종료")
                t.undo()
                t.penup()
                t.goto(-300,200)
                t.pendown()
                t.write("성공!! 최종점수 : " + str(point), font=("Arial", 30))

        else:
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+15, y)
            left = check_colli(x-15, y)
            up = check_colli(x, y+7)
            down = check_colli(x, y-7)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()
            if(x + 30 > 325):
                print("게임 종료")
                t.undo()
                t.penup()
                t.goto(-300,200)
                t.pendown()
                t.write("성공!! 최종점수 : " + str(point), font=("Arial", 30))

    def up(self):
        if(self.turtle.shape() == "car_d.gif"):
            self.turtle.shape(self.img_file[2])
            self.turtle.left(180)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        elif(self.turtle.shape() == "car_r.gif"):
            self.turtle.shape(self.img_file[2])
            self.turtle.left(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        elif(self.turtle.shape() == "car_l.gif"):
            self.turtle.shape(self.img_file[2])
            self.turtle.right(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        else:
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

    def down(self):
        if(self.turtle.shape() == "car_u.gif"):
            self.turtle.shape(self.img_file[3])
            self.turtle.right(180)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        elif(self.turtle.shape() == "car_r.gif"):
            self.turtle.shape(self.img_file[3])
            self.turtle.right(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        elif(self.turtle.shape() == "car_l.gif"):
            self.turtle.shape(self.img_file[3])
            self.turtle.left(90)
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()

        else:
            self.turtle.forward(5)
            (x, y) = self.turtle.pos()
            check_colli_candy(x, y)
            right = check_colli(x+7, y)
            left = check_colli(x-7, y)
            up = check_colli(x, y+15)
            down = check_colli(x, y-15)
            if(right != 0):
                check_life()
            if(left != 0):
                check_life()
            if(up != 0):
                check_life()
            if(down != 0):
                check_life()
            
        




# 메인

# 게임 화면의 크기 (650, 500)
win = t.Screen()
win.setup(650, 500)
t.speed(10)
t.shape("turtle")

# 도로 생성
t.colormode(255)
t.bgcolor(120, 120, 120)



# 사각형 생성
draw_rec(t, rec1["x_pos"], rec1["y_pos"], rec1["width"], rec1["height"]) # rec1
draw_rec(t, rec2["x_pos"], rec2["y_pos"], rec2["width"], rec2["height"]) # rec2
draw_rec(t, rec3["x_pos"], rec3["y_pos"], rec3["width"], rec3["height"]) # rec3
draw_rec(t, rec4["x_pos"], rec4["y_pos"], rec4["width"], rec4["height"]) # rec4
draw_rec(t, rec5["x_pos"], rec5["y_pos"], rec5["width"], rec5["height"]) # rec5
draw_rec(t, rec6["x_pos"], rec6["y_pos"], rec6["width"], rec6["height"]) # rec6
draw_rec(t, rec7["x_pos"], rec7["y_pos"], rec7["width"], rec7["height"]) # rec7
draw_rec(t, rec8["x_pos"], rec8["y_pos"], rec8["width"], rec8["height"]) # rec8
draw_rec(t, rec9["x_pos"], rec9["y_pos"], rec9["width"], rec9["height"]) # rec9


# 점수 초기화
t.hideturtle()
t.penup()
t.goto(-300,200)
t.pendown()
t.write("점수 : " + str(point), font=("Arial", 30))


# 자동차 이미지 생성
register_shape("car_r.gif")
register_shape("car_d.gif")
register_shape("car_l.gif")
register_shape("car_u.gif")


# 수명 초기화
life1 = Life(300, 220)
life2 = Life(250, 220)
life3 = Life(200, 220)


# 랜덤한 캔디 설정
register_shape("candy.gif")
candy_x = []
candy_y = []
colli_check = []
candy = []
while len(candy_x) < 20:
    x_pos = random.randint(-200, 200)
    y_pos = random.randint(-150, 200)
    colli = check_colli(x_pos, y_pos)
    if(colli == 0):
        colli_check.append(colli)
        candy_x.append(x_pos)
        candy_y.append(y_pos)
        candy.append(Candy(x_pos, y_pos))


# 자동차 생성
img_file = []
img_file.append("car_r.gif")
img_file.append("car_l.gif")
img_file.append("car_u.gif")
img_file.append("car_d.gif")
car = Car(img_file, 10, (-315, 90))



# 자동차 움직이기
win.listen()
win.onkey(car.left, "Left")
win.onkey(car.right, "Right")
win.onkey(car.up, "Up")
win.onkey(car.down, "Down")

t.mainloop()






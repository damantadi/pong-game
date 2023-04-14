import math
import turtle
import random

wn=turtle.Screen()
wn.setup(800,600)
wn.title("PONG GAME")
wn.bgcolor("black")
wn.tracer(0)#speed up the game

#paddel

paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape("square")
paddel_a.shapesize(stretch_wid=5,stretch_len=1)
paddel_a.color("red")
paddel_a.penup()
paddel_a.goto(-350,0)
#paddel2

paddel_b = turtle.Turtle()
paddel_b.speed(0)
paddel_b.shape("square")
paddel_b.shapesize(stretch_wid=5,stretch_len=1)
paddel_b.color("red")
paddel_b.penup()
paddel_b.goto(350,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

def paddel_a_up():
    y=paddel_a.ycor()
    y+=20
    paddel_a.sety(y)

def paddel_a_down():
    y=paddel_a.ycor()
    y-=20
    paddel_a.sety(y)

wn.listen()
wn.onkeypress(paddel_a_up,"w")
wn.onkeypress(paddel_a_down,"s")

def paddel_b_up():
    y=paddel_b.ycor()
    y+=20
    paddel_b.sety(y)

def paddel_b_down():
    y=paddel_b.ycor()
    y-=20
    paddel_b.sety(y)

wn.listen()
wn.onkeypress(paddel_b_up,"Up")
wn.onkeypress(paddel_b_down,"Down")


while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() >290 :
        ball.sety(290)
        ball.dy*=-1
    elif ball.ycor()<-290:
         ball.sety(-290)
         ball.dy*=-1

         # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.setx(350)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.setx(-350)
        ball.dx *= -1

    if ball.xcor()>340  and  ball.ycor() < paddel_a.ycor()+50 and ball.ycor() > paddel_a.ycor()-50:
       ball.dx*=-1


    elif ball.xcor()<-340 and  ball.ycor() < paddel_b.ycor()+50 and ball.ycor() > paddel_b.ycor()-50:
         ball.dx*=-1




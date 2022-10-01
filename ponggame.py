#pong game
#Made By: Riya Dhami

import turtle

wn = turtle.Screen()
wn.title("PING-PONG by Riya Dhami")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

#player a
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#player b
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("black")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Score
score_a = 0
score_b = 0

#Function 
def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0    Player B: 0", align="center", font=("ariel", 24, "normal"))

#keyboard controls
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main loop for game
while True:
    wn.update()
    #ballmovement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #reset ball
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center", font=("ariel", 24, "normal"))

    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center", font=("ariel", 24, "normal"))

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40) :
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40) :
        ball.setx(-340)
        ball.dx *= -1

    

import turtle

# windos
wind = turtle.Screen()
wind.title('Dinosaur game')
wind.bgcolor('white')
wind.tracer(0)
wind.setup(width=1000, height=600)

# score
scor = 0
score = turtle.Turtle()
score.color('black')
score.penup()
score.hideturtle()
score.goto(0, 260)

# height score
height = 0
h_score = turtle.Turtle()
h_score.color('black')
h_score.penup()
h_score.hideturtle()
h_score.goto(200, 260)

# dinosaur
dino = turtle.Turtle()
dino.color('red')
dino.shape('square')
dino.shapesize(stretch_wid=3, stretch_len=1)
dino.speed(0)
dino.penup()
dino.goto(-400, -50)
dino.dy = 0.5

# flour
fl = turtle.Turtle()
fl.color('grey')
fl.shape('square')
fl.shapesize(stretch_wid=0.25, stretch_len=1000)
fl.penup()
fl.goto(0, -80)

# block
blo = turtle.Turtle()
blo.color('blue')
blo.shape('square')
blo.shapesize(stretch_wid=2.5, stretch_len=1)
blo.speed(0)
blo.penup()
blo.goto(500, -50)
blo.dx = 2

# birds
bird = turtle.Turtle()
bird.color('blue')
bird.shape('square')
bird.shapesize(stretch_wid=1, stretch_len=2)
bird.speed(0)
bird.penup()
bird.goto(1901, -30)
bird.dx = 1

# quit or restaret
by = turtle.Turtle()
by.color('black')
by.penup()
by.hideturtle()
by.goto(0, 0)

#functions
def dino_jemp():
    y = dino.ycor()
    y += 150
    dino.sety(y)
    dino.shapesize(stretch_wid=3, stretch_len=1)
def dino_down():
    dino.shapesize(stretch_wid=1.5, stretch_len=1)
    dino.goto(-400, -65)
def quit():
    wind.bye()
def restaret():
    blo.goto(500, -50)
    bird.goto(1901, -30)
    by.clear()
    blo.dx = 2
    bird.dx = 1
    dino.dy = 0.5

#Keybord bindings
wind.listen()
wind.onkeypress(dino_jemp, 'Up')
wind.onkeypress(dino_jemp, 'w')
wind.onkeypress(dino_jemp, ' ')
wind.onkeypress(dino_down, 's')
wind.onkeypress(dino_down, 'Down')
wind.onkeypress(quit, 'q')
wind.onkeypress(restaret, 'r')

# game loop
while True:
    wind.update()
    if blo.xcor() == -500:
        blo.setx(500)
    if bird.xcor() == -500:
        bird.setx(1500)
    if dino.ycor() > -50:
        dino.sety(dino.ycor() - dino.dy)
    if dino.ycor() > 100:
        dino.goto(-400, -50)
    
    # score
    scor += 1
    score.clear()
    score.write(('Score:', scor), align='center', font=('Courier',24,'normal'))

    # move
    blo.setx(blo.xcor() - blo.dx)
    bird.setx(bird.xcor() - bird.dx)

    # when dinosaur hit the block or the bird
    if ((dino.xcor() == blo.xcor()) and (dino.ycor() <= blo.ycor())) or ((dino.xcor() == bird.xcor()) and (dino.ycor() >= -50)):
        score.goto(-200, 260)
        # height score
        if scor > height:
            height = scor
            h_score.clear()
            h_score.write(('Height score:', height), align='center', font=('Courier',24,'normal'))

        by.write("click 'r' to restaret  or click 'q' to quit", align='center', font=('courier', 25, 'normal'))
        scor = -1
        blo.dx = 0
        bird.dx = 0
        dino.dy = 0

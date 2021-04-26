#pythman

import turtle
import random
import time


# creating the lives and score 
lives = 3 
score = 0 #starting score

#create the window 
window = turtle.Screen()
window.tracer(0)
window.bgcolor('black')
window.setup(550,600)

#create the pacman turtle
pythman = turtle.Turtle()
pythman.speed(0)
pythman.penup() #so the line on the screen is not seen
pythman.color('yellow')
pythman.shape('circle')
pythman.direction = 'stop'

#pen for moving
pen = turtle.Turtle()
pen.speed(0)
pen.color('white smoke')
pen.penup()
pen.goto(0,245)
pen.pendown()
pen.write('Score: {} Lives: {}'.format(score,lives), align='center',font = ('Impact',36))
pen.hideturtle()

#pacman will continually move 
def movement():
    if pythman.direction == 'up':
        y = pythman.ycor()
        y+= 1.5
        pythman.sety(y)

    if pythman.direction == 'down':
        y = pythman.ycor()
        y-= 1.5
        pythman.sety(y)
    
    if pythman.direction == 'left':
        x = pythman.xcor()
        x-= 1.5
        pythman.setx(x)
        
    if pythman.direction == 'right':
        x = pythman.xcor()
        x+= 1.5
        pythman.setx(x)
    
def moveUp():
    pythman.direction = 'up'

def moveDown():
    pythman.direction = 'down'

def moveLeft():
    pythman.direction = 'left'

def moveRight():
    pythman.direction = 'right'


window.listen()
window.onkeypress(moveUp, 'Up')
window.onkeypress(moveDown, 'Down')
window.onkeypress(moveLeft, 'Left')
window.onkeypress(moveRight, 'Right')

# making the food for pacman
foods = []
for _ in range(90):
    food = turtle.Turtle()
    food.speed(0)
    food.penup()
    food.color('dark orange')
    food.shape('circle')
    food.shapesize(stretch_wid=0.4, stretch_len=0.4)
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    food.setposition(x,y)
    foods.append(food)


#enemies

enemies = []
for x in range(15):
    enemy = turtle.Turtle()
    enemy.penup()
    enemy.color('hot pink')
    enemy.shape('turtle')
    enemy.speed = 0.5
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    enemy.setposition(x,y)
    enemies.append(enemy)


def enemyMovement():
    for enemy in enemies:
        y = enemy.ycor()
        x = enemy.xcor()
        y += enemy.speed
        x += enemy.speed
        enemy.sety(y)
        enemy.setx(x)


while True:
    window.update()

    #lives
    if lives == 0:
        score=0
        lives=3
        pen.clear()
        pen.write('Score:{} Lives:{}'.format(score,lives),align = 'center', font = ('Impact',36))
        time.sleep(1)
        pythman.goto(0,0)

        
    #collisions on border
    if pythman.xcor()>300 or pythman.xcor()<-300 or pythman.ycor()>300 or pythman.ycor()<-300:
        lives-= 1
        pen.clear()
        pen.write('Score: {} Lives: {}'.format(score,lives), align='center',font = ('Impact',36))
        time.sleep(1)
        pythman.goto(0,0)


    #food collision
    for food in foods:
        if pythman.distance(food) < 10:
            score+=1
            pen.clear()
            pen.write('Score:{} Lives:{}'.format(score,lives),align = 'center', font = ('Impact',36))
            x = random.randint(-300,300)
            y = random.randint(-300,300)
            food.goto(x,y)

    #enemies with border
    for enemy in enemies:
        if enemy.xcor()>300 or enemy.xcor()<-300 or enemy.ycor()>300 or enemy.ycor()<-300:
            x = random.randint(-300,300)
            y = random.randint(-300,300)
            enemy.goto(x,y)
            enemyMovement()

    #enemy collision
    for enemy in enemies:
        if pythman.distance(enemy) < 10:
            lives -= 1
            pen.clear()
            pen.write('Score:{} Lives:{}'.format(score,lives),align = 'center', font = ('Impact',36))
            time.sleep(1)
            pythman.goto(0,0)
            
            
    movement()
    enemyMovement()


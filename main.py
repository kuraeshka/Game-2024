import turtle
import os
import math
import random
import time

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Space monster")
wn.bgpic("background.gif")
wn.tracer(0)
# Добавление текстур-------------
wn.register_shape("enemy.1.gif")
wn.register_shape("boss.gif")
wn.register_shape("background.gif")
wn.register_shape("sea.gif")
# Рамка--------------------------
borden_pen = turtle.Turtle()
borden_pen.speed(0)
borden_pen.color("black")
borden_pen.penup()
borden_pen.setposition(-300,-300)
borden_pen.pendown()
borden_pen.pensize(3)
for side in range(4):
    borden_pen.fd(600)
    borden_pen.lt(90)
    borden_pen.hideturtle()
# Враги---------------------------
score = 8
score_pen = turtle.Turtle()
score_pen.color("yellow")
score_pen.penup()
score_pen.setposition(225, 300)
scorestrig = "Врагов: {}".format(score)
score_pen.write(scorestrig, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
# Таймер-------------------------
timesec = 300
mins, secs = divmod(timesec, 60)
timeformat = 'Время {}:{}'.format(mins,secs)
time_pen = turtle.Turtle()
time_pen.color("white")
time_pen.penup()
time_pen.setposition(-40,300)
time_pen.write(timeformat, False, align="Left", font=("Arial", 14, "normal"))
time_pen.hideturtle()
# Таймер обеъкт------------------
time_enemy = turtle.Turtle()
time_enemy.shape("circle")
time_enemy.color("red")
time_enemy.penup()
time_enemy.speed(0)
time_enemyspeed = 2
time_enemy.setposition(0,0)
timestate = "ready"
time_enemy.hideturtle()
# Победа-------------------------
win_pen = turtle.Turtle()
win_pen.penup()
win_pen.setposition(0, 3000)
win_pen.color("white")
win_pen.hideturtle()
# Щиты---------------------------

# Щит противника-----------------
numbers_shield_enemys = 5
shield_enemies = []
for i in range(numbers_shield_enemys):
    shield_enemies.append(turtle.Turtle())

shield_enemy_x = -225
shield_enemy_y = -50
shield_enemy_number = 0

for shield_enemy in shield_enemies:
    shield_enemy.shape("square")
    shield_enemy.shapesize(1,2)
    shield_enemy.color("white")
    shield_enemy.penup()
    shield_enemy.speed(0)
    x = shield_enemy_x+(100*shield_enemy_number)
    y = shield_enemy_y
    shield_enemy.setposition(x,y)
    shield_enemyspeed = 0.2
    shield_enemy_number +=1

shield_enemy_life = 10

# Щиты игрока--------------------
numbers_shield_players = 2
shield_players = []
for i in range(numbers_shield_players):
    shield_players.append(turtle.Turtle())

shield_player_x = -200
shield_player_y = -100
shield_player_number = 0
shield_player_distant = 40

for shield_player in shield_players:
    shield_player.shape("square")
    shield_player.shapesize(2,6)
    shield_player.color("yellow")
    shield_player.penup()
    shield_player.speed(0)
    x = shield_player_x +(400*shield_player_number)
    shield_player.setposition(x, -150)
    shield_player_number +=1

shield_player_life = 10

# Босс---------------------------
boss = turtle.Turtle()
boss.shape("boss.gif")
boss.penup()
boss.speed(0)
boss.setposition(0,5000)
bossspeed = 0.3
boss.hideturtle()
bosslife = 4
bossstate = "stand"

# Игрок--------------------------
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0

# Робот---------------------------
number = 8
enemies = []
for i in range(number):
    enemies.append(turtle.Turtle())
    # Робот-----------------------
enemy_set_x = -225
enemy_set_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.shape("enemy.1.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_set_x + (70*enemy_number)
    y = enemy_set_y
    enemy.setposition(x, y)
    enemyspeed = 0.2
    enemy_number += 1
    if enemy_number == 10:
        enemy_set_y -= 50
        enemy_number = 0

#Оружие--------------------------
booleat = turtle.Turtle()
booleat.color("green")
booleat.shape("classic")
booleat.penup()
booleat.speed(0)
booleat.setposition(0,5000)
booleat.lt(90)
booleatspeed = 4
booleat.hideturtle()
booleatstate = "ready"
#Оружие чит мод-------------------
booleat_sea = turtle.Turtle()
booleat_sea.color("red")
booleat_sea.shape("sea.gif")
booleat_sea.shapesize(100,100)
booleat_sea.penup()
booleat_sea.speed(0)
booleat_sea.setposition(0,5000)
booleat_seaspeed = 8
booleat_sea.hideturtle()
booleat_sea_state = "ready"
# Передвижение игрока-------------
def move_left():
    player.speed = -1.5
def move_right():
    player.speed = 1.5
def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)


#Огонь из оружия-------------------
def fire_booleat():
    global booleatstate
    if booleatstate == "ready":
        booleatstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        booleat.setposition(x,y)
        booleat.showturtle()
#Огонь из оржуия читы--------------
def fire_booleat_sea():
    global booleat_sea_state
    if booleat_sea_state == "ready":
        booleat_sea_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        booleat_sea.setposition(x,y)
        booleat_sea.showturtle()
#Колизия----------------------------
def collision(t1,t2):
    distanes = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distanes < 15:
        return True
    else:
        return False

#Клавиатура-------------------------
wn.listen()
wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")
wn.onkeypress(fire_booleat,"w")
wn.onkeypress(fire_booleat_sea, "e")

#Игра геймплей----------------------
while True:
    # Передвижение игроков----------
    wn.update()
    move_player()
    # Передвижение роботов----------
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 15
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 15
                e.sety(y)
            enemyspeed *= -1

        # Колизия попадания по роботу
        if collision(booleat, enemy):
            booleat.hideturtle()
            booleatstate = "ready"
            booleat.setposition(0, -400)
            enemy.setposition(enemy.xcor(), 5000)
            score -= 1
            scorestrig = "Врагов: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestrig, False, align="left", font=("Arial", 14, "normal"))
        # Колизия попандания по роботу волной
        if collision(booleat_sea, enemy):
            booleat_sea.hideturtle()
            booleat_sea_state = "ready"
            enemy.setposition(enemy.xcor(), 5000)
            score -= 1
            scorestrig = "Врагов: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestrig, False, align="left", font=("Arial", 14, "normal"))
        # Колизия стокновения игрока
        if collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Поражение")
            exit()
        if enemy.ycor() < 0:
            for shield_enemy in shield_enemies:
                shield_enemy.sety(5000)
    # Передвижение щитов--------------
    for shield_enemy in shield_enemies:
        x = shield_enemy.xcor()
        x +=shield_enemyspeed
        shield_enemy.setx(x)

        if shield_enemy.xcor() > 280:
            for e in shield_enemies:
                shield_enemyspeed *= -1
        if shield_enemy.xcor() < -280:
            for e in shield_enemies:
                shield_enemyspeed *= -1
        # Колизия столкновения с щитом --
        if collision(shield_enemy,booleat):
            shield_enemy_life -=1
            booleat.hideturtle()
            booleatstate = "ready"
            booleat.setposition(0, -400)
            if shield_enemy_life == 0:
                shield_enemy.sety(5000)
                shield_enemy_life = 5
    # Таймер--------------------------
    if timestate == "ready":
        x = time_enemy.xcor()
        x += time_enemyspeed
        time_enemy.setx(x)
    if time_enemy.xcor()>50:
        time_enemyspeed *=-1
        timesec -=1
        time_pen.clear()
        mins, secs = divmod(timesec, 60)
        timeformat = 'Время {}:{}'.format(mins, secs)
        time_pen.write(timeformat, False, align="Left", font=("Arial", 14, "normal"))
    if time_enemy.xcor() < -50:
        time_enemyspeed *=-1
        timesec -=1
        time_pen.clear()
        mins, secs = divmod(timesec, 60)
        timeformat = 'Время {}:{}'.format(mins, secs)
        time_pen.write(timeformat, False, align="Left", font=("Arial", 14, "normal"))
    if timesec == 0:
        exit()
    # Появление босса-----------------
    if score == 0:
        bossstate = "ready"
        score = 8
        scorestrig = "Врагов: {}".format(score)
        for shield_enemy in shield_enemies:
            shield_enemy.sety(5000)
    if bossstate == "ready":
        boss.sety(0)
        boss.showturtle()
        x = boss.xcor()
        x += bossspeed
        boss.setx(x)
        if boss.xcor() > 280:
            bossspeed *= -1
        if boss.xcor() < -280:
            bossspeed *= -1

    # Колизия босса-------------------
    if collision(booleat, boss):
        bosslife -= 1
        booleat.hideturtle()
        booleatstate = "ready"
        booleat.setposition(0, -400)
        if bosslife == 0:
            bossstate = "death"

    #Конец матча-----------------------
    if bossstate == "death":
        boss.hideturtle()
        boss.setposition(0,5000)
        time_pen.setposition(-40, -60)
        time_enemy.setposition(0, 0)
        time_pen.write(timeformat, False, align="Left", font=("Arial", 14, "normal"))
        win_pen.setposition(52, 0)
        win_pen.write("Победа", False, align="right", font=("Arial", 20, "normal"))
        win_pen.setposition(0,0)
        score_pen.clear()
        timestate = "over"
        player.speed = 0
        player.setposition(0, -250)
        bosslife = 4
    # Колизия столкновения с щитом игрока
    #for shield_player in shield_players:
       # if collision(booleat,shield_player):
          #  booleat.hideturtle()
          #  booleatstate = "ready"
          #  booleat.setposition(0, -400)
    # Начало новой игры-----------------
    if collision(booleat,win_pen):
        booleat.hideturtle()
        booleatstate = "ready"
        booleat.setposition(0, -400)
        bossstate = 'stand'
        timesec = 300
        timestate = "ready"
        time_pen.clear()
        time_pen.setposition(-40, 300)
        mins, secs = divmod(timesec, 60)
        timeformat = 'Время {}:{}'.format(mins, secs)
        time_pen.write(timeformat, False, align="Left", font=("Arial", 14, "normal"))
        win_pen.clear()
        win_pen.setposition(0, 3000)
        score_pen.write(scorestrig, False, align="left", font=("Arial", 14, "normal"))
        for enemy in enemies:
            enemy.sety(250)
        for shield_enemy in shield_enemies:
            shield_enemy.sety(-50)
    # Пуля------------------------------
    if booleatstate == "fire":
        y = booleat.ycor()
        y += booleatspeed
        booleat.sety(y)
    if booleat.ycor() > 280:
        booleat.hideturtle()
        booleatstate = "ready"
    # Волна------------------------------
    if booleat_sea_state == "fire":
        y = booleat_sea.ycor()
        y += booleat_seaspeed
        booleat_sea.sety(y)
    if booleat_sea.ycor() > 280:
        booleat_sea.hideturtle()
        booleat_sea_state = "ready"
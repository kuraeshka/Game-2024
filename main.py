import turtle
import os
import math
import random
import time

wn = turtle.Screen()
wn.setup(650,650)
wn.title("Space monster")
wn.bgpic("background.gif")
wn.tracer(0)
# Добавление текстур-------------
wn.register_shape("Player.death.gif")
wn.register_shape("player.1.gif")
wn.register_shape("Pobeda.gif")
wn.register_shape("start.gif")
wn.register_shape("EnemyBooleat.gif")
wn.register_shape("player.gif")
wn.register_shape("enemy.1.gif")
wn.register_shape("boss.gif")
wn.register_shape("background.gif")
wn.register_shape("gunenemy.gif")
wn.register_shape("booleat.gif")
wn.register_shape("blocks.gif")
wn.register_shape("shield.gif")
# Музыка-------------------------
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
score_pen.setposition(225, 302)
scorestrig = "Врагов: {}".format(score)
score_pen.write(scorestrig, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
# Таймер-------------------------
timesec = 240
mins, secs = divmod(timesec, 60)
timeformat = 'Время {}:{}'.format(mins,secs)
time_pen = turtle.Turtle()
time_pen.color("white")
time_pen.penup()
time_pen.setposition(-40,302)
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
win_pen.shape("Pobeda.gif")
win_pen.hideturtle()
# Старт--------------------------
start_pen = turtle.Turtle()
start_pen.penup()
start_pen.setposition(50,0)
start_pen.color("white")
start_pen.shape("start.gif")
startstate = "start"
start_pen.setposition(0,0)

# Щиты---------------------------
# Щит противника-----------------
numbers_shield_enemys = 5
shield_enemies = []
for i in range(numbers_shield_enemys):
    shield_enemies.append(turtle.Turtle())

shield_enemy_x = -225
shield_enemy_y = 5000
shield_enemy_number = 0

for shield_enemy in shield_enemies:
    shield_enemy.shape("shield.gif")
    shield_enemy.penup()
    shield_enemy.speed(0)
    x = shield_enemy_x+(100*shield_enemy_number)
    y = shield_enemy_y
    shield_enemy.setposition(x,y)
    shield_enemyspeed = 0.2
    shield_enemy_number +=1

shield_enemy_life = 5

# Щиты игрока--------------------
numbers_shield_players = 2
shield_players = []
for i in range(numbers_shield_players):
    shield_players.append(turtle.Turtle())

shield_player_x = -200
shield_player_y = 5000
shield_player_number = 0
shield_player_distant = 40

for shield_player in shield_players:
    shield_player.shape("blocks.gif")
    shield_player.penup()
    shield_player.speed(0)
    x = shield_player_x +(400*shield_player_number)
    shield_player.setposition(x, shield_player_y)
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
bosslife = 3
bossstate = "stand"
# Хп бар босса-------------------
#1
Boss_bar1 = turtle.Turtle()
Boss_bar1.shape("square")
Boss_bar1.shapesize(1,4)
Boss_bar1.color("red")
Boss_bar1.penup()
Boss_bar1.setposition(-80,250)
Boss_bar1.speed = 0
Boss_bar1.hideturtle()
#2
Boss_bar2 = turtle.Turtle()
Boss_bar2.shape("square")
Boss_bar2.shapesize(1,4)
Boss_bar2.color("red")
Boss_bar2.penup()
Boss_bar2.setposition(0,250)
Boss_bar2.speed = 0
Boss_bar2.hideturtle()
#3
Boss_bar3 = turtle.Turtle()
Boss_bar3.shape("square")
Boss_bar3.shapesize(1,4)
Boss_bar3.color("red")
Boss_bar3.penup()
Boss_bar3.setposition(80,250)
Boss_bar3.speed = 0
Boss_bar3.hideturtle()

# Игрок--------------------------
player = turtle.Turtle()
player.shape("player.1.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0
player_x = 0
playerlife_state = "korable"

# Пули робота--------------------
booleat_robot = turtle.Turtle()
booleat_robot.shape("EnemyBooleat.gif")
booleat_robot.penup()
booleat_robot.speed(0)
booleat_robot.setposition(0,280)
booleat_robot.setheading(270)
booleat_robot.speed = 0
booleat_robot_speed = -1
booleat_robotstate = "ready"
Booleat_robor_time = 0
booleat_robot.hideturtle()

# Оружие робота-------------------
gun_number = 8
guns = []
for i in range(gun_number):
    guns.append(turtle.Turtle())
# Оружие робота-------------------
enemy_gun_set_x = -225
enemy_gun_set_y = 5000
enemy_gun_number = 0
gun_booleat_life = 8
for gun in guns:
        gun.shape("gunenemy.gif")
        gun.penup()
        gun.speed(0)
        x = enemy_gun_set_x + (70*enemy_gun_number)
        y = enemy_gun_set_y
        gun.setposition(x, y)
        enemy_gun_speed = 0.2
        enemy_gun_number += 1
        if enemy_gun_number == 8:
            enemy_gun_set_y -= 50
            enemy_gun_number = 0

# Робот---------------------------
number = 8
enemies = []
for i in range(number):
    enemies.append(turtle.Turtle())
# Робот-----------------------
enemy_set_x = -225
enemy_set_y = 5000
enemy_number = 0
for enemy in enemies:
        enemy.shape("player.gif")
        enemy.penup()
        enemy.speed(0)
        x = enemy_set_x + (70*enemy_number)
        y = enemy_set_y
        enemy.setposition(x, y)
        enemyspeed = 0.2
        enemy_number += 1
        if enemy_number == 8:
            enemy_set_y -= 50
            enemy_number = 0

#Оружие--------------------------
booleat = turtle.Turtle()
booleat.shape("booleat.gif")
booleat.penup()
booleat.speed(0)
booleat.setposition(0,5000)
booleat.lt(90)
booleatspeed = 4
booleat.hideturtle()
booleatstate = "ready"

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
def fire_booleat_robot():
    global booleat_robotstate
    if booleat_robotstate == "ready":
        booleat_robotstate = "fire"
        x = player.xcor()
        y = 280
        booleat_robot.setposition(x,y)
        booleat_robot.showturtle()
#Колизия----------------------------
def collision(t1,t2):
    distanes = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distanes < 20:
        return True
    else:
        return False
def collision1(t1,t2):
    distanes = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distanes < 50:
        return True
    else:
        return False
#Клавиатура-------------------------
wn.listen()
wn.onkeypress(fire_booleat,"w")
#Игра геймплей----------------------
while True:
    if startstate == "start":
        player.setposition(0,-250)
    if collision(start_pen,booleat):
        start_pen.clear()
        startstate = "Game"
        booleat.hideturtle()
        booleatstate = "ready"
        booleat.setposition(0, -400)
        for enemy in enemies:
            enemy.sety(250)
        for shield_enemy in shield_enemies:
            shield_enemy.sety(-50)
        for gun in guns:
            gun.sety(215)
        for shield_player in shield_players:
            shield_player.sety(-150)
        start_pen.setposition(5000,0)
# Передвижение игрока и доп команды ----------
    wn.update()
    move_player()
# Передвижение роботов----------
    if startstate == "Game":
        wn.onkeypress(move_left, "a")
        wn.onkeypress(move_right, "d")
        for enemy in enemies:
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            if enemy.xcor() > 275:
                for e in enemies:
                    y = e.ycor()
                    y -= 15
                    e.sety(y)
                enemyspeed *= -1
            if enemy.xcor() < -275:
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
# Колизия стокновения игрока
            if collision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Поражение")
                exit()
            if enemy.ycor() < 25:
                for shield_enemy in shield_enemies:
                    shield_enemy.sety(1000)
# Оружие роботов-----------------------
        for gun in guns:
            x = gun.xcor()
            x += enemy_gun_speed
            gun.setx(x)

            if gun.xcor() > 275:
                for gun in guns:
                    y = gun.ycor()
                    y -= 15
                    gun.sety(y)
                enemy_gun_speed *= -1
            if gun.xcor() < -275:
                for gun in guns:
                    y = gun.ycor()
                    y -= 15
                    gun.sety(y)
                enemy_gun_speed *= -1
# Колизия попадания по оружию
            if collision(booleat, gun):
                booleat.hideturtle()
                booleatstate = "ready"
                booleat.setposition(0, -400)
                gun.sety(5000)
                gun_booleat_life -=1
# Передвижение щитов--------------
        for shield_enemy in shield_enemies:
            x = shield_enemy.xcor()
            x +=shield_enemyspeed
            shield_enemy.setx(x)

            if shield_enemy.xcor() > 275:
                for e in shield_enemies:
                    shield_enemyspeed *= -1
            if shield_enemy.xcor() < -275:
                for e in shield_enemies:
                    shield_enemyspeed *= -1
# Колизия столкновения с щито---
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
            Booleat_robor_time +=1
            time_pen.clear()
            mins, secs = divmod(timesec, 60)
            timeformat = 'Время {}:{}'.format(mins, secs)
            time_pen.write(timeformat, False, align="Left", font=("Arial", 14, "normal"))
        if time_enemy.xcor() < -50:
            time_enemyspeed *=-1
            timesec -=1
            time_pen.clear()
            Booleat_robor_time +=1
            mins, secs = divmod(timesec, 60)
            timeformat = 'Время {}:{}'.format(mins, secs)
            time_pen.write(timeformat, False, align="Left", font=("Arial", 14, "normal"))
        if timesec == 0:
            exit()
# Пули роботов-------------------
        if gun_booleat_life > 0:
            if Booleat_robor_time == 10:
                fire_booleat_robot()
                Booleat_robor_time = 0
            for shield_player in shield_players:
                if collision1(shield_player, booleat_robot):
                    booleat_robot.hideturtle()
                    booleat_robotstate = "ready"
                    booleat_robot.setposition(0, -280)
# Колизия попадания по игроку-----
        if collision(booleat_robot, player):
            if playerlife_state == "player":
                player.shape("player.1.gif")
                exit()
            if playerlife_state == "korable":
                player.shape("Player.death.gif")
                playerlife_state = "player"
                booleat_robot.hideturtle()
                booleat_robotstate = "ready"
                booleat_robot.setposition(0, -280)
# Колизия востановления жизни-----
        if playerlife_state == "player":
            for shield_player in shield_players:
                if collision1(booleat, shield_player):
                    booleat_robot.hideturtle()
                    booleat_robotstate = "ready"
                    player.shape("player.1.gif")
                    playerlife_state = "korable"
                    shield_player.hideturtle()
                    shield_player.setposition(shield_player.xcor(), 5000)

# Появление босса-----------------
        if score == 0:
            Boss_bar3.showturtle()
            Boss_bar2.showturtle()
            Boss_bar1.showturtle()
            player.shape("player.1.gif")
            playerlife_state = "korable"
            for shield_player in shield_players:
                shield_player.hideturtle()
                shield_player.setposition(shield_player.xcor(), 5000)
            bossstate = "ready"
            score = 8
            scorestrig = "Врагов: {}".format(score)
            for shield_enemy in shield_enemies:
                shield_enemy.sety(5000)
            for gun in guns:
                gun.sety(5000)
        if bossstate == "ready":
            boss.sety(0)
            boss.showturtle()
            x = boss.xcor()
            x += bossspeed
            boss.setx(x)
            if boss.xcor() > 200:
                bossspeed *= -1
            if boss.xcor() < -200:
                bossspeed *= -1
#Колизия босса-------------------
        if collision(booleat, boss):
            if bosslife == 3:
                Boss_bar3.hideturtle()
            if bosslife == 2:
                Boss_bar2.hideturtle()
            if bosslife == 1:
                Boss_bar1.hideturtle()
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
            win_pen.showturtle()
            win_pen.setposition(0, 0)
            score_pen.clear()
            timestate = "over"
            player.speed = 0
            player.setposition(0, -250)
            bosslife = 3
            booleat_robot.hideturtle()
            booleat_robotstate = "ready"
            gun_booleat_life = 8
# Начало новой игры-----------------
        if collision(booleat,win_pen):
            booleat.hideturtle()
            booleatstate = "ready"
            booleat.setposition(0, -400)
            Booleat_robor_time = 0
            bossstate = 'stand'
            timesec = 180
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
            for gun in guns:
                gun.sety(215)
            for shield_player in shield_players:
                shield_player.sety(-150)
                shield_player.showturtle()
# Пуля------------------------------
    if booleatstate == "fire":
        y = booleat.ycor()
        y += booleatspeed
        booleat.sety(y)
    if booleat.ycor() > 280:
        booleat.hideturtle()
        booleatstate = "ready"
# Пуля робота------------------------
    if booleat_robotstate == "fire":
        y = booleat_robot.ycor()
        y += booleat_robot_speed
        x = player.xcor()
        booleat_robot.sety(y)
        booleat_robot.setx(x)
    if booleat_robot.ycor() < -280:
        booleat_robot.hideturtle()
        booleat_robotstate = "ready"
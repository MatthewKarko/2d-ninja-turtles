####################################
#Author: Mr.Karko
#Date: 8/4/18
#TASK 1
#Game: Ninja turtles fight
#
#
#
####################################
from random import randint
import time
import turtle
turtle.bgcolor('grey')
m = turtle.Turtle()
r = turtle.Turtle()
l = turtle.Turtle()
s = turtle.Turtle()
d = turtle.Turtle()




class Dice:    
    def die(num):
        die=randint(1,num)
        return die
class Character:
    def __init__(self,name,hp,thaco,ac,exp):
        self.name=name
        self.hp=hp
        self.thaco=thaco
        self.ac=ac
        self.exp=exp



class Ralph(Character):
    def __init__(self):
        super().__init__(name='Raphael',thaco=20,ac=15,
                         hp=20,exp=8)
    prof = "Fighter"
    maxhp=10
    level=1
    hd=8
    level2=15

class Mike(Character):
    def __init__(self):
        super().__init__(name='Michael Angelo',thaco=20,ac=15,
                         hp=14,exp=8)
    prof= "Jokester"
    maxhp=10
    level=1
    hd=8
    level2=15
class Don(Character):
    def __init__(self):
        super().__init__(name='Donatello',thaco=20,ac=15,
                         hp=16,exp=8)
    prof= "Genius"
    maxhp=10
    level=1
    hd=8
    level2=15

class Leo(Character):
    def __init__(self):
        super().__init__(name='Leonardo',thaco=20,ac=15,
                         hp=20,exp=8)
    prof= "Leader"
    maxhp=8
    level=1
    hd=8
    level2=15

class Shredder(Character):
    def __init__(self):
        super().__init__(name="Shredder",
                         hp=28,thaco=20,
                         ac=6,
                         exp=10)


class TheFootClan(Character):
    def __init__(self):
        super().__init__(name="The Foot Clan",
                         hp=9,thaco=18,
                         ac=6,
                         exp=8)

def profession():
    print("What ninja turtle do you want to play?",'\n',
          " press r for Raphael",'\n',
          " press m for Michael Angelo",'\n',
          " press d for Donatello",'\n',
          " press l for Leonardo")
    pclass=input("Enter choice: ")
    if pclass =="r":
        Prof = Ralph()
    elif pclass=="m":
        Prof = Mike()
    elif pclass == "l":
        Prof = Leo()
    elif pclass == "d":
        Prof = Don()
    else:
        print('That is an invalid choice, I will assign you Raphael')
        Prof = Ralph()
        #profession()
    return Prof
def ranmob():
    mob = Shredder() if Dice.die(2)<2 else TheFootClan()
    return mob


def playerAttack():
    roll=Dice.die(20)   
    if roll>=hero.thaco-mob.ac:
        print("You hit")
        if hero.prof=="Fighter":
            rollD=Dice.die(10)
            Rattack()

        if hero.prof=="Genius":
            rollD=Dice.die(6)
            Dattack()

        if hero.prof=="Leader":
            rollD=Dice.die(8)
            Lattack()

        if hero.prof=="Jokester":
            rollD=Dice.die(6)
            Mattack()
            
        print("for",rollD,"damage")
        mob.hp-=rollD
        print("the",mob.name,"has",mob.hp,"hp left")
    else:
        print("You miss")

def monsterAttack():
    roll=Dice.die(20)   
    if roll>=mob.thaco-hero.ac:
        print("Enemy hit")
        if mob.name=="Shredder":                    
            rollD=Dice.die(12)
            Sattack()
        elif mob.name=="The Foot Clan":
            rollD=Dice.die(8)
        print("for",rollD,"damage")
        hero.hp-=rollD
        print(hero.name,"has",hero.hp,"hp left")
    else:
        print("Enemy misses")

def levelUp():


    while hero.exp>=hero.level2:
        levelGain=False
        hero.level+=1
        levelGain=True
        hero.level2=hero.level2*2
        if levelGain==True:
            hero.maxhp+=Dice.die(hero.hd)
            hero.hp=hero.maxhp


            print("You Gained a level","\n",'hp:',hero.hp,"\n",'level:',hero.level)
            levelGain=False
    while hero.level>=3:
        hero.level-=3
        hero.thaco-=1
        print("thaco:",hero.thaco)


def commands():

    while True:
        if hero.prof=="Fighter" or "Genius" or "Leader" or "Jokester":
            print (" press f to fight",'\n',
               "press enter to pass")
            command=input("~~~~~~~~~Press a key to Continue.~~~~~~~")
            if command=="f":
                playerAttack()
                break
            elif command=="":
                pass
                break

            else:
                print('That is not a choice try again,')

####################################################################################################################
def TurtleMike():
    
    #m = turtle.Turtle()

    m.shape("turtle")
    m.resizemode("user")
    m.shapesize(3, 3, 9)
    m.shapesize(outline=10)
    m.speed(6)
    m.color('Orange')
    m.penup()
    m.setx(-300)
    m.sety(-200)

    

def Mattack():
    time.sleep(2)

    m.pd()
    m.setx(100)
    m.sety(-50)

    m.penup()
    m.setx(-300)
    m.sety(-200)

def TurtleRalph():
    
   # r = turtle.Turtle()

    r.shape("turtle")
    r.resizemode("user")
    r.shapesize(3, 3, 9)
    r.shapesize(outline=10)
    r.speed(6)
    r.color('Red')
    r.penup()
    r.setx(-300)
    r.sety(-100)

def Rattack():
    time.sleep(2)

    r.pd()
    r.setx(100)
    r.sety(-50)

    r.penup()
    r.setx(-300)
    r.sety(-100)

def TurtleLeo():
    
    #l = turtle.Turtle()

    l.shape("turtle")
    l.resizemode("user")
    l.shapesize(3, 3, 9)
    l.shapesize(outline=10)
    l.speed(6)
    l.color('Blue')
    l.penup()
    l.setx(-300)
    l.sety(0)

def Lattack():
    time.sleep(2)

    l.pd()
    l.setx(100)
    l.sety(-50)

    l.penup()
    l.setx(-300)
    l.sety(0)
    

       

def TurtleDon():
    
    #d = turtle.Turtle()

    d.shape("turtle")
    d.resizemode("user")
    d.shapesize(3, 3, 9)
    d.shapesize(outline=10)
    d.speed(6)
    d.color('Purple')
    d.penup()
    d.setx(-300)
    d.sety(100)

def Dattack():
    time.sleep(2)

    d.pd()
    d.setx(100)
    d.sety(-50)

    d.penup()
    d.setx(-300)
    d.sety(100)
    

       


def TurtleShred():
    
    #s = turtle.Turtle()

    s.shape("turtle")
    s.resizemode("user")
    s.shapesize(5, 5, 9)
    s.shapesize(outline=6)
    s.speed(6)
    s.color('white', 'black')
    s.penup()
    s.setx(100)
    s.sety(-50)
    s.right(180)

def Sattack():
    time.sleep(2)

    s.pd()
    s.setx(-300)
    s.sety(100)

    s.setx(-300)
    s.sety(-200)

    s.penup()
    s.setx(100)
    s.sety(-50)


####################################################################################################################
TurtleShred()
TurtleMike()
TurtleRalph()
TurtleLeo()
TurtleDon()



mob=ranmob()
hero=profession()
print("Your turtles stats: hp thaco ac xp",'\n',
      hero.hp,hero.thaco,hero.ac,hero.exp)
print('It was just another nomal day for the 4 turtles, until..... BOOM. a loud explosion had been set off in a building. As you rush out and into the building. You dont see anyone until......You see', mob.name,'.')
while True:

    if mob.hp<=0:
        print(mob.name,'is dead!',
              'Congratulations you have successfully beat your enemy')        
        hero.exp+=mob.exp        
        print('Hero xp',hero.exp)
        mob=ranmob()
    if hero.hp<=0:
        mob.exp+=hero.exp
        print("Enemy xp",mob.exp)
        print(hero.name,'died!  '
              'Better luck next time!')
        

        time.sleep(5)
                        
        hero=profession()
        print("name hp thaco ac xp",'\n',
              hero.name,hero.hp,hero.thaco,hero.ac,hero.exp)

    levelUp()
    time.sleep(2)
    
    
    print(mob.name,"has",mob.hp,"hp.")
    if hero.hp>0:
        commands()
    if mob.hp>0:                
        monsterAttack()

    

#imports&vars
import turtle
import math, time
import random
import sys

varibal1 = 5

from threading import Timer

screen = turtle.Screen()


#the preloaded drawings
def eye(col, rad):
    turtle.down()
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
    turtle.up()


preset = 0


def pre1():
    global preset
    if preset == 0:
        preset = 1
        turtle.clear()
        red.clear()
        orange.clear()
        yellow.clear()
        green.clear()
        blue.clear()
        purple.clear()
        pink.clear()
        white.clear()
        black.clear()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.color("black")
        turtle.pendown()
        # draw face
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.up()

        # draw eyes
        turtle.goto(-40, 120)
        eye('white', 15)
        turtle.goto(-37, 125)
        eye('black', 5)
        turtle.goto(40, 120)
        eye('white', 15)
        turtle.goto(40, 125)
        eye('black', 5)

        # draw nose
        turtle.goto(0, 75)
        eye('black', 8)

        # draw mouth
        turtle.goto(-40, 85)
        turtle.down()
        turtle.right(90)
        turtle.circle(40, 180)
        turtle.up()

        # draw tongue
        turtle.goto(-10, 45)
        turtle.down()
        turtle.right(180)
        turtle.fillcolor('red')
        turtle.begin_fill()
        turtle.circle(10, 180)
        turtle.end_fill()

    else:
        print("You cannot use 2 presets in one go.")


def pre2():
    global preset
    if preset == 0:
        preset += 1
        turtle.clear()
        red.clear()
        orange.clear()
        yellow.clear()
        green.clear()
        blue.clear()
        purple.clear()
        pink.clear()
        white.clear()
        black.clear()

        turtle.penup()
        turtle.goto(0, 0)
        turtle.pensize(5)
        turtle.color("black")
        turtle.pendown()
        # draw face
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.up()

        # draw eyes
        turtle.goto(-40, 120)
        eye('white', 15)
        turtle.goto(-37, 125)
        eye('black', 5)
        turtle.goto(40, 120)
        eye('white', 15)
        turtle.goto(40, 125)
        eye('black', 5)

        # draw nose
        turtle.goto(0, 75)
        eye('black', 8)

        # draw mouth
        turtle.goto(-40, 85)
        turtle.down()
        turtle.right(90)
        turtle.circle(40, 180)
        turtle.up()

        # draw tongue
        turtle.goto(-10, 45)
        turtle.down()
        turtle.right(180)
        turtle.fillcolor('red')
        turtle.begin_fill()
        turtle.circle(10, 180)
        turtle.end_fill()

    else:
        print("You cannot use 2 presets in one go.")


def draw():

    for i in range(4):
        turtle.forward(30)
        turtle.left(90)

    turtle.forward(30)


screen.setup(600, 600)


# Driver Code
def pre3():
    global preset
    if preset == 0:
        preset += 1
        turtle.clear()
        red.clear()
        orange.clear()
        yellow.clear()
        green.clear()
        blue.clear()
        purple.clear()
        pink.clear()
        white.clear()
        black.clear()
        if __name__ == "__main__":

            # set turtle object speed
            turtle.speed(100)
            # loops for board
            for i in range(8):
                # not ready to draw
                turtle.penup()
                # set position for every row
                turtle.setpos(-120, 30 * i - 120)
                # ready to draw
                turtle.pendown()
                # row
                for j in range(8):
                    # conditions for alternative color
                    if (i + j) % 2 == 0:
                        col = 'black'
                    else:
                        col = 'white'
                    # fill with given color
                    turtle.fillcolor(col)

                    # start filling with colour
                    turtle.begin_fill()

                    # call method
                    draw()
                    # stop filling
                    turtle.end_fill()

            # hide the turtle
        # turtle.hideturtle()
    else:
        print("You cannot use 2 presets in one go.")


def pre4():
    turtle.clear()
    red.clear()
    orange.clear()
    yellow.clear()
    green.clear()
    blue.clear()
    purple.clear()
    pink.clear()
    white.clear()
    black.clear()

    turtle.goto(0, 50)
    colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
    turtle.speed(10)
    turtle.bgcolor("black")

    for x in range(200):
        turtle.pencolor(colors[x % 6])
        turtle.width(x / 100 + 1)
        turtle.forward(x)
        turtle.left(59)

    turtle.done()
    turtle.speed(10)
    turtle.bgcolor("black")

    for x in range(200):
        turtle.pencolor(colors[x % 6])
        turtle.width(x / 100 + 1)
        turtle.forward(x)
        turtle.left(59)


def pre5():
    turtle.clear()
    print("this preset is empty right now.")


def pre6():
    turtle.clear()
    print("this preset is empty right now.")


def pre7():
    turtle.clear()
    print("this preset is empty right now.")


def pre8():
    turtle.clear()
    print("this preset is empty right now.")


def pre9():
    turtle.clear()
    print("this preset is empty right now.")


#for drawing


def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 90)


def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drag(x, y):
    turtle.goto(x, y)


def incr():
    global varibal1
    varibal1 += 3
    sise = varibal1
    turtle.pensize(sise)


def decr():
    global varibal1
    varibal1 -= 3
    sise = varibal1
    turtle.pensize(sise)


sprint("Hello player :>")

check = 0
eraseconfermation = 0


def erase():
    global eraseconfermation
    if eraseconfermation == 2:
        #   global eraseconfermation
        turtle.clear()
        eraseconfermation = 0
    else:
        eraseconfermation = 2


filesav = 0

save_names = []

Sav = [
    "Evie.eps", "Dominique.eps", "BrysonHamilton.eps", "Kairo.eps",
    "TackettQuincy.eps", "Alexus.eps", "HurstEmilia.eps", "Maelyn.eps",
    "PatrickLennon.eps", "Alma.eps", "CassidyAmirah.eps", "Jazmyn.eps",
    "HawkSylis.eps", "Theron.eps", "SnowJudah.eps", "Dominik.eps",
    "OsborneGunnar.eps", "Kolten.eps", "HamiltonBryan.eps", ".eps",
    "CrandallRayyan.eps", "Micaiah.eps", "SanchezKarmyn.eps", "Lorena.eps",
    "ChinJacklyn.eps", "Adalee.eps", "WesleyMaritza.eps", "Raelyn.eps",
    "BroussardAngeline.eps", "River.eps", "DuarteJalynn.eps", "Annabella.eps",
    "KennedyTessa.eps", "Keyla.eps", "TilleyCillian.eps", "Morgan.eps",
    "DeleonAnalise.eps", "Nichole.eps", "CorleyEsme.eps", "Estefany.eps",
    "WarnerJulius.eps", "Tyron.eps", "MoraAva.eps", "Marin.eps",
    "JamesKalia.eps", "Tyler.eps", "TillyJanie.eps", "Rayna.eps",
    "MckinneySaylor.eps", "Alba.eps", "Crosby.eps"
]
ran = random.choice(Sav)


def sav():
    global filesav
    screen.getcanvas().postscript(file=ran, colormode='color')
    print(("Your file is called ") + (ran))
    filesav += 1

    print("Open SavingInstructions.md to accsess your photo.")


def qui():
    print("quitting now.")
    print(".")
    print(".")
    turtle.clearscreen()
    quit()


#for changeing the pencolor

turtle.Screen().bgcolor("lightblue")


def red1():
    global check
    turtle.color("red")
    print("Changed color to RED")
    check += 1


def orange1():
    global check
    turtle.color("orange")
    print("Changed color to ORANGE")
    check += 1


def yellow1():
    global check
    turtle.color("yellow")
    print("Changed color to YELLOW")
    check += 1


def green1():
    global check
    turtle.color("green")
    print("Changed color to GREEN")
    check += 1


def blue1():
    global check
    turtle.color("blue")
    print("Changed color to BLUE")
    check += 1
    print(check)


def purple1():
    global check
    turtle.color("purple")
    print("Changed color to PURPLE")
    check += 1


def pink1():
    global check
    turtle.color("pink")
    print("Changed color to PINK")
    check += 1


def black1():
    global check
    turtle.color("black")
    print("Changed color to BLACK")
    check += 1


def white1():
    global check
    turtle.color("white")
    print("Changed color to WHITE")
    check += 1


#for changeing the bagrounds
def red2():

    turtle.Screen().bgcolor("red")
    print(" Changed background color to RED")
    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


def orange2():

    turtle.Screen().bgcolor("orange")
    print(" Changed background color to ORANGE")
    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


def yellow2():

    turtle.Screen().bgcolor("yellow")
    print(" Changed background color to YELLOW")
    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


def green2():

    turtle.Screen().bgcolor("green")
    print(" Changed background color to GREEN")

    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


def blue2():

    turtle.Screen().bgcolor("blue")
    print(" Changed background color to BLUE")
    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))
    print(check)


def purple2():

    turtle.Screen().bgcolor("purple")
    print(" Changed background color to PURPLE")
    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


def pink2():

    turtle.Screen().bgcolor("pink")
    print(" Changed background color to PINK")

    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


def black2():

    turtle.Screen().bgcolor("black")
    print(" Changed background color to BLACK")
    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


def white2():

    turtle.Screen().bgcolor("white")
    print(" Changed background color to WHITE")
    green.clear()
    green.goto(-50, -100)
    green.write("g", font=("Pacifico", 24, "normal"))


#--------------------------

green = turtle.Turtle()
green.hideturtle()
green.penup()
green.goto(-275, 150)
green.pencolor("gray")
green.write("Please open the console and instructions.md to figure out the controlls. This message will go away soon")

green.goto(0, 0)
green.pendown()
green.speed(5)

#green.color("green")
#green.showturtle()
#blue = turtle.Turtle()
#blue.color("blue")
#purple = turtle.Turtle()

green.color("green")
green.showturtle()
blue = turtle.Turtle()
blue.color("blue")
purple = turtle.Turtle()
purple.color("purple")
red = turtle.Turtle()
red.color("red")
yellow = turtle.Turtle()
yellow.color("yellow")
orange = turtle.Turtle()
orange.color("orange")
black = turtle.Turtle()
black.color("black")
white = turtle.Turtle()
white.color("white")
pink = turtle.Turtle()
pink.color("pink")

red.penup()
orange.penup()
yellow.penup()
green.penup()
blue.penup()
purple.penup()
pink.penup()
white.penup()
black.penup()

screen.onclick(goto)

red.onclick(red1)
orange.onclick(orange1)
yellow.onclick(yellow1)
green.onclick(green1)
blue.onclick(blue1)
pink.onclick(pink1)
white.onclick(white1)

black.onclick(black1)

#red.speed(6)
#orange.speed(6)
#yellow.speed(6)
#green.speed(6)
#blue.speed(6)
#purple.speed(6)
#pink.speed(6)
#white.speed(6)
#black.speed(6)

turtle.shape("circle")

red.shape("circle")
orange.shape("circle")
yellow.shape("circle")
green.shape("circle")
blue.shape("circle")
purple.shape("circle")
pink.shape("circle")
white.shape("circle")
black.shape("circle")

red.goto(-200, -100)
orange.goto(-150, -100)
yellow.goto(-100, -100)
green.goto(-50, -100)
blue.goto(0, -100)
purple.goto(50, -100)
pink.goto(100, -100)
white.goto(150, -100)
black.goto(200, -100)

red.write("r", font=("Pacifico", 24, "normal"))
orange.write("o", font=("Pacifico", 24, "normal"))
yellow.write("y", font=("Pacifico", 24, "normal"))
green.write("g", font=("Pacifico", 24, "normal"))
blue.write("b", font=("Pacifico", 24, "normal"))
purple.write("p", font=("Pacifico", 24, "normal"))
pink.write("k", font=("Pacifico", 24, "normal"))
white.write("w", font=("Pacifico", 24, "normal"))
black.write("l", font=("Pacifico", 24, "normal"))

red.hideturtle()
orange.hideturtle()
yellow.hideturtle()
green.hideturtle()
blue.hideturtle()
purple.hideturtle()
pink.hideturtle()
white.hideturtle()
black.hideturtle()

#print("Your Decidion has been recorded.")

#to change colors
turtle.ondrag(drag)
screen.onkey(red1, "r")
screen.onkey(yellow1, "y")
screen.onkey(orange1, "o")
screen.onkey(green1, "g")
screen.onkey(blue1, "b")
screen.onkey(purple1, "p")
screen.onkey(pink1, "k")

screen.onkey(black1, "l")
screen.onkey(white1, "w")

#to change bagrounds

screen.onkey(red2, "R")
screen.onkey(yellow2, "Y")
screen.onkey(orange2, "O")
screen.onkey(green2, "G")
screen.onkey(blue2, "B")
screen.onkey(purple2, "P")
screen.onkey(pink2, "K")
screen.onkey(black2, "L")
screen.onkey(white2, "W")

# to change pensise
screen.onkey(incr, "Up")
screen.onkey(decr, "Down")

#to see the presets
screen.onkey(pre1, "1")
screen.onkey(pre2, "2")
screen.onkey(pre3, "3")
screen.onkey(pre4, "4")
screen.onkey(pre5, "5")
screen.onkey(pre6, "6")
screen.onkey(pre7, "7")
screen.onkey(pre8, "8")
screen.onkey(pre9, "9")

screen.onkey(sav, "S")
screen.onkey(erase, "E")
screen.onkey(qui, "Q")
screen.listen()

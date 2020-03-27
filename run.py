import turtle
import random
import tkinter

### Class for each player object
class Player:
    
    ## Starting y coordinate
    y = -250
    
    ## Initialing variables
    def __init__(self, vMin, vMax, color):
        self.player = turtle.Turtle()
        self.player.shape('turtle')
        self.color = color 
        self.player.color(self.color)
        self.velocity = random.randint(vMin, vMax)
        self.player.penup()
        self.player.setheading(90)
        self.player.sety(self.y)
    
    ## Function that starts moving the turtle 
    def start(self):
        self.player.pendown()
        self.player.forward(self.velocity)

## Class that holds all of the player objects
class Race:
    turtle.Screen().bgcolor('#498000')
    ## Array that holds all of the player objects
    turtles = []
    
    ## Color for each turtle
    colors = ['blue', 'red', 'orange', 'pink', 'black', 'purple', 'cyan', 'yellow']
    
    ## Function that adds turtles to the array
    def addTurtle(self, amount):
        ## Initializes players for each turtle given in the parameters
        for x in range(0, amount + 1):
            ## Creates a player with a given velocity
            t = Player(0, 10, self.colors[x])
            ## Appends the turtle to the array
            self.turtles.append(t)
        
    
    ## Sets up the race
    def setup(self):
        currentX = -350
        maxX = 350
        ## Spacing between each of the turtles
        spacing = 700 / (len(self.turtles) - 1)
        ## Each turtle gets their x coordinate set to the current x position and the spacing
        for t in self.turtles:
            t.player.setx(currentX)
            currentX = currentX + spacing
        
    def start(self):
        won = False
        while won != True:
            for t in self.turtles:
                t.start()
                if t.player.ycor() >= 250:
                    won = True
                    print(t.color + ' turtle won!')
            


    
race = Race()
race.addTurtle(7)
race.setup()
race.start()





#print(turtle.screensize())

turtle.Screen().exitonclick()
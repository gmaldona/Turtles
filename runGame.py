import turtle
import random
from tkinter import *
import time

### Class for each player object
class Player:
    
    ## Starting y coordinate
    y = -250
    
    ## Initialing variables
    def __init__(self, vMin, vMax, color):
        self.player = turtle.Turtle()
        self.player.showturtle()
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
        for x in range(0, amount):
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
    
    ## Function that starts the race 
    def start(self):
        ## Variable that is responsible for stopping the race
        won = False
        ## color of the turtle that won
        color = ''
        ## Moves the turtle until a color won
        while won != True:
            ## Loops through each turtle
            for t in self.turtles:
                ## Moves the turtle
                t.start()
                 ## If a turtle crossed the finish line
                if t.player.ycor() >= 250:
                    ## There is a winnter
                    won = True
                    color = t.color
                    time.sleep(2)
                


def run(numberOfTurtles):
    race = Race()
    race.addTurtle(numberOfTurtles)
    race.setup()
    race.start()


run(8)
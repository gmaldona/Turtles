import os

def run():
    
    count = input("How many rounds?: ")
    
    for x in range(0, int(count)): 
        os.system('cd Desktop/Turtles/')
        os.system('python runGame.py')
    
run()
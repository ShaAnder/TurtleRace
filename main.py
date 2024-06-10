#!usr/bin/env/python

### --- IMPORTS --- ###

#we want our turtle imports
from turtle import Turtle as T
from turtle import Screen as S
#and random to ensure our bois can move randomly
import random

### --- SETUP --- ###

#we want to setup our screen first
s= S()

#give the screen some definite properties to prevent confusion to people reading
s.setup(width=500,height=744)

#we're gonna add a tad of flair to the race too by adding a bg
background = "racetrack.png"
s.bgpic(background)

#color, starting position and all turtles lists for our loops later
colors = ["red","orange","yellow","green","blue","purple"]
y_pos = [-325, -200, -72, 56, 190, 325]
all_turtles = []

#now we loop to create our turtles, makes turtle, assigns color, assigns start 
#and appends to a list for easier manipulation later down the code

#for the turtles in a range of 6 (aka make 6)
for t_list in range(0, 6):
    #create turtle
    t = T(shape="turtle")
    t.color(colors[t_list])
    t.shapesize(stretch_len=2,stretch_wid=2)
    #so we don't draw all over the sceen as it moves
    t.penup()
    #go to your starting pos, loop through y list index
    t.goto(x=-230, y=y_pos[t_list])
    #append turtle to list
    all_turtles.append(t)

### --- MAIN --- ###

#now we want to create a text input for user to bet
usr_bet = s.textinput(title="Make your bet", prompt="Who will win? Enter a color: ").lower()

#two checks here for our whiles, one loop does the main thing, the other to check correct bet
checking = True
is_race_on = False
while checking:
    #if the bets not in colors,
    if usr_bet not in colors:
        #ask for a valid choice
        print("Sorry this is not a valid choice please try again")
        usr_bet = s.textinput(title="Make a VALID bet", prompt="Who will win? Enter a color: ").lower()
    #if it's a valid choice 
    else:
        #do race, kill check loop, activate race loop
        is_race_on = True
        checking = False
        #while the race is happening
        while is_race_on:
            #loop through our turtles
            for t in all_turtles:
                #if any of them are at the end
                if t.xcor() >230:
                    #kill the loop
                    is_race_on = False
                    #get the winner
                    winning_color = t.pencolor()
                    #user feedback
                    if winning_color == usr_bet:
                        print("AYYY your turtle won!")
                    else:
                        print(f"Sorry should have bet on {winning_color}")
                #we want our turtles to move a random distance
                distance = random.randint(0,10)
                #each turtle moves x Distance
                t.forward(distance)














### --- EXIT --- ###
s.exitonclick()
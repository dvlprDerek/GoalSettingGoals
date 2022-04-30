import turtle
import numpy
import csv
import functions

file=open("nhl-stats.csv")
uneeded_header=file.readline()
uneeded_header2=file.readline()

print("Welcome to NHL Goal Setting Goals Mountain!")


# peak: leading goal scorer at flag (-18,195)
flag = turtle.Turtle()
flag.hideturtle()
flag.penup()
flag.goto(-18,195)

# start point (-280,-220)
skater = turtle.Turtle()
skater.hideturtle()
skater.penup()
skater.goto(-280,-220)


wn = turtle.Screen()
wn.bgpic("mountain.gif")
#wn.mainloop() //stops code here

player = turtle.Turtle()

print("- - - - - - - - - - MENU - - - - - - - - - -")
                     
ticker = True
playerdic = {}
i = 1
functions.addaplayer(playerdic,input("Please input the first player (e.g: 'daniel sedin'): "))

while ticker == True and i<5:
  yorno = input("Would you like to add another player? (y/n): ")
  
  if yorno == "y":
    playeri = input("Please type in player name: ")


    # call function to check # of occurance before adding player to dict
    #functions.maxoccurance(playerdic)
    functions.addaplayer(playerdic,playeri) #add player to dict 
    i=i+1
  else:
    print("stopping ...")
    ticker = False
print(playerdic)
#print(functions.max(playerdic))

functions.place(playerdic, skater)







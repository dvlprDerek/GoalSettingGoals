import numpy
import csv
file=open("nhl-stats.csv")
uneeded_header1=file.readline()
uneeded_header2=file.readline()

def addaplayer(dict,n):
  if(playerchecker(dict,n) == False):
    print("Player is not in the list")
  if(alreadyinfinder(dict,n) == True):
    print("Player can't be added more than once.")
  ticker = 0
  file.seek(0)
  for line in file:
    data=line.strip().split(",")
    name = data[0]
    goal = data[4]
    if(n.lower()==name.lower()):
      if(maxoccurance(dict,n) == True):
        dict[name] = goal
        ticker = ticker + 1

 

 
    
  

    
def max(dict):
  arr = dict.values()
  lead = 0
  for g in arr:
    if int(g) > lead:
      lead = int(g)
      
  return lead

def place(dict, skater):
  arr = []
  scale = 415/max(dict)
  
  for x,y in dict.items():
    goal = int(y)
    arr.append(goal)
    count = 0
    for i in arr:
      if i == goal:
        count = count + 1

    if count == 1:
      skater.goto(-50,-220+goal*scale)
      skater.write(x)
    elif count == 2:
      skater.goto(-200,-220+goal*scale)
      skater.write(x)
    elif count == 3:
      skater.goto(100,-220+goal*scale)
      skater.write(x)
    
  skater.goto(-280,-220)
  
  
#def maxoccurance(playerdic,n)
def maxoccurance(playerdic,n):
  maxocr = 0
  file.seek(0)
  for line in file:
    data=line.strip().split(",")
    name = data[0]
    goal = data[4]
    if(n.lower() == name.lower()):
      playergoal = goal
  
  for x,y in playerdic.items():
    if y == playergoal:
      maxocr = maxocr + 1

  
  if (maxocr >2):
    return False
  else:
    return True



#def namefinder(playerdic,n)
def alreadyinfinder(dic,n):
  found = 0
  for x,y in dic.items():
    if (x.lower() == n.lower()):
      found = found + 1
  if(found > 0):
    return True
  else: 
    return False

#checks if players are in the list 
def playerchecker(dic,n):
  found = 0
  file.seek(0)
  for line in file:
    data=line.strip().split(",")
    name = data[0]
    if(n.lower() == name.lower()):
      found = found + 1
  if (found > 0):
    return True
  else:
    return False
#compares players
#def compare(player1,player2):
  #if (player1>player2):
    #diff = player1
    #print(player1 " is ahead of " player2 "by" player1-player2 )
    
  
  

#def maxgoals(player):
  #after finding player goals, compare goals to find player with most goals. Return player with most goals in selected players list


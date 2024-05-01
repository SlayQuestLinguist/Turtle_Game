class Turtle:
    def __init__(self, iName):
      self.distanceToSea = 14
      self.turtleId = iName
    def getDistance(self):
      return self.distanceToSea
    def getIsTurtleInSea(self):
      return self.distanceToSea <= 0
    def advance(self, iSteps):
      print("advance(" + str(iSteps) + ") of current " + str(self))
      self.distanceToSea = self.distanceToSea - iSteps
      print ("after advance(), " + str(self))
    def __str__(self):
      return "Turtle " + str(self.turtleId) + ": " + str(self.distanceToSea)

class TurtleGroup:
  def __init__(self):
    self.turtlelist = [Turtle(1), Turtle(2), Turtle(3)]
    print(self.turtlelist)
    for lTurtle in self.turtlelist:
      print(lTurtle)

  def getIsAllInSea(self):
    turtleInSeaList = []
    for lTurtle in self.turtlelist:
      turtleInSeaList.append(lTurtle.getIsTurtleInSea())
    return all(turtleInSeaList)
#    print("initiating turtles:")
  
  def advanceTurtles(self, iSteps):
    for lTurtle in self.turtlelist:
      print("advanceTurtles(" + str(iSteps) + "), current status " + str(lTurtle))
    turtleToAdvance = None
    ttlDistanceList = []
    for lTurtle in self.turtlelist:
      ttlDistanceList.append(lTurtle.getDistance())
    print("self.ttlDistanceList")
    distanceMax = max(ttlDistanceList)
    index = ttlDistanceList.index(distanceMax)
    turtleToAdvance = self.turtlelist[index]
    turtleToAdvance.advance(iSteps)

  def allAdvance(self):
    for lTurtle in self.turtlelist:
      print("allAvance() current group = " + str(lTurtle))
      lTurtle.advance(1)
      print("after allAvance() group = " + str(lTurtle))

  def __str__(self):
    return "TurtleGroup: 1:" + str(self.turtle1) +  ", 2:" + str(self.turtle2) + ", 3:" + str(self.turtle3)

class Dice:
  def __init__(self):
    pass
  @staticmethod
  def roll():
    import random
    upSide = random.randint(1, 6)
    return upSide

class Sun:
    def __init__(self):
      self.brightness = 0
    def incrementBrightness(self):
      self.brightness = self.brightness + 1
    def getIsSunUp(self):
      return self.brightness == 7
    def __str__(self):
      return "Sun: " + str(self.brightness)

class GameBoard:
  def __init__(self):
    self.sun = Sun()
    self.turtleGroup = TurtleGroup()
    
  def playOnce(self, iRoundNum):
    print("playOnce(" + str(iRoundNum) + ")")
    ### Play
    rollResult = Dice.roll()
    print("dice = " + str(rollResult))
    if rollResult == 6:
      self.sun.incrementBrightness()
      print(self.sun, iRoundNum)
    elif rollResult in [4,5]:
      self.turtleGroup.allAdvance()
    else:
      self.turtleGroup.advanceTurtles(rollResult)
    ### Check results
    if self.turtleGroup.getIsAllInSea():# and self.sun.getIsSunUp() == False:
      print("Yay, you won! All turtles are in the sea: " + str(self.turtleGroup.getIsAllInSea()))
      return(1)
    elif self.sun.getIsSunUp():# and self.turtleGroup.getIsAllInSea() == False:
      print("Oh no, you lost! Sun is up:" + str(self.sun.getIsSunUp()))
      return(0)
    elif iRoundNum > 200:
      print("Infinite loop detected")
      return("bad game")
    else:
      print("launching another round... ")
      return(self.playOnce(iRoundNum + 1))
      
    return("default")

class GameRepeator:

  def execute():
    print("GameRepeator::execute()")
    lRound = 0
    winTimes = 0
    while lRound < 1000:
      print(">>> calling new GameBoard() for l = " + str(lRound))
      game = GameBoard()
      endResult = game.playOnce(0)
      print(">>> GameBoard() for l = " + str(lRound) + " returned " + str(endResult))

      if endResult == 1:
        winTimes += 1
      lRound += 1
    winRate = winTimes/1000
    print(winRate)


GameRepeator.execute()

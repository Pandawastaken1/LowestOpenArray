class bus:

  #Constructor
  def __init__(self,colorInput,numberOfSeats,engineHP,isbus):
    self.bodyColor=colorInput
    self.seats=numberOfSeats
    self.engineSize=engineHP
    self.bus=isbus

  def driveoffintothesunset(self):
    print("and this is just like a movie")


    #0 100,22,44,33
    #2.5,
    #"Hello George, how are you today? Just Fine?"
    #True/False


mybus=bus("black",40,3050.1,True)

print(mybus.bodyColor)
print(mybus.seats)
mybus
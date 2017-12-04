
class Santa:

  def __init__(self, name):
    self.hasSanta = False
    self.hasGiftee = False
    self.confirmedSanta = ''
    self.confirmedGiftee = ''
    self.potentialSantas = []
    self.potentialGiftees = []
    self.name = name

  def __str__(self):
    string = ''
    if self.hasSanta:
      string = 'The person "{0}" has "{1}" as a Santa \n'.format(self.name, self.confirmedSanta.name)
    else: 
      string = 'The person "{0}" has the following potential Santas: \n'.format(self.name)
      for s in self.potentialSantas:
        string += " - {} \n".format(s.name)
    if self.hasGiftee:
      string += 'And has "{}" as a Giftee \n'.format(self.confirmedGiftee.name)
    else: 
      string += "And the following potential Giftees \n"
      for g in self.potentialGiftees:
        string += " - {} \n".format(g.name)
    return string

  # starting functions
  def setPotentialSantas(self, santas):
    self.potentialSantas = santas

  def setPotentialGiftees(self, giftees):
    self.potentialGiftees = giftees
  
  def setHasSanta(self, hasSanta):
    self.hasSanta = hasSanta

  def setHasGiftee(self, hasGiftee):
    self.hasGiftee = hasGiftee

  def setSanta(self, Santa):
    self.confirmedSanta = Santa

  def setGiftee(self, Giftee):
    self.confirmedGiftee = Giftee

  def addToPotentialGiftees(self, Giftee):
    if Giftee not in self.potentialGiftees:
      self.potentialGiftees.append(Giftee)

  def addToPotentialSantas(self, Santa):
    if Santa not in self.potentialSantas:
      self.potentialSantas.append(Santa)

  # other functions
  def isGiftee(self, giftee):
    self.confirmedGiftee = giftee
    self.hasGiftee = True
    self.potentialGiftees = []

  def isSanta(self, santa):
    self.confirmedSanta = santa
    self.hasSanta = True
    self.potentialSantas = []

  def removeGiftee(self, giftee):
    self.potentialGiftees.remove(giftee)
    if len(self.potentialGiftees) == 1:
      self.hasGiftee = True
      self.confirmedGiftee = self.potentialGiftees[0]
      self.potentialGiftees = []
      return self.confirmedGiftee, self
    return None, None

  def removeSanta(self, santa):
    self.potentialSantas.remove(santa)
    if len(self.potentialSantas) == 1:
      self.hasSanta = True
      self.confirmedSanta = self.potentialSantas[0]
      self.potentialSantas = []
      return self.confirmedSanta, self
    return None, None
    
      


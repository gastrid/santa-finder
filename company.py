from santa import Santa

class Company:

  def __init__(self):
    self.people = {}
    self.found = 0 # Number of people whose santa has been found

  def companyToMatrix(self):
    companyMatrix = {}
    for n, p in self.people.items():
      pRow = {}
      if p.confirmedSanta != '':
        pRow['confirmedSanta'] = p.confirmedSanta.name
      else:
        pRow['confirmedSanta'] = ''

      if p.confirmedGiftee != '':
        pRow['confirmedGiftee'] = p.confirmedGiftee.name
      else:
        pRow['confirmedGiftee'] = ''

      companyMatrix[p.name] = pRow
    return companyMatrix

  def matrixToCompany(self, matrix):
    for n, p in matrix.items():
      pers = Santa(n)
      self.people[n] = pers

    # loop again to add the actual people
    for n, p in self.people.items():
      cs = matrix[n]['confirmedSanta']
      if cs != '':
        p.hasSanta = True
        p.confirmedSanta = self.people[cs]
      else: 
        for nn, pp, in self.people.items():
          if (pp.name != p.name) & (pp.name != cs):
            p.addToPotentialSantas(pp)

      cg = matrix[n]['confirmedGiftee']
      if cg != '':
        p.hasGiftee = True
        p.confirmedGiftee = self.people[cg]
      else: 
        for nn, pp, in self.people.items():
          if (pp.name != p.name) & (pp.name != cg):
            p.addToPotentialGiftees(pp)

  def show(self, person):
    if (person == 'company'):
      string = 'Here are the people in this company: \n'
      for n, _ in self.people.items():
        string += '- {}, \n'.format(n)
      print(string)
      return
    for n, p in self.people.items():
      if p.name == person:
        print(p)

  def makeLink(self, santa, giftee, gives):
    for n, p in self.people.items():
      if n == santa:
        santa = p
      if n == giftee:
        giftee = p
    if (type(santa) is str) | (type(giftee) is str):
      print("Oops, the names you've entered are not in our list of people...")
      return
    if gives == True:
      santa.isGiftee(giftee)
      self.removeGiftee(giftee, santa)

      giftee.isSanta(santa)
      self.removeSanta(santa, giftee)
    else:
      result, newSanta = santa.removeGiftee(giftee)
      if result is not None:
          self.removeGiftee(result, newSanta)
      result, newGiftee = giftee.removeSanta(santa)
      if result is not None:
        self.removeSanta(result, newGiftee)
      
   
  def removeGiftee(self, giftee, isNot):
    for n, p in self.people.items():
      if (n != giftee.name) & (n != isNot.name) & (p.hasGiftee == False):
        result, santa = p.removeGiftee(giftee)
        if result is not None:
          self.removeGiftee(result, santa)

  def removeSanta(self, santa, isNot):
    for n, p in self.people.items():  
      if (n != santa.name) & (n != isNot.name) & (p.hasSanta == False):
        result, giftee = p.removeSanta(santa)
        if result is not None:
          self.removeSanta(result, giftee)
        
  def addPeople(self, people):
    for pName in people:
      pers = Santa(pName)
      for n, p in self.people.items():
        p.addToPotentialSantas(pers)
        p.addToPotentialGiftees(pers)
        pers.addToPotentialSantas(p)
        pers.addToPotentialGiftees(p)     
      self.people[pName] = pers
    








       
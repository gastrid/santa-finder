
import pickle
from company import Company

def returnInput(string, comp):
  if string == "help":
    print(helpString)
    return None
  elif string == "exit":
    return string
  else:
    analyseInput(string, comp)

def analyseInput(string, comp):
  cmds = string.split(" ")
  gives = False
  if cmds[0] == "enter":
    comp.addPeople(cmds[1:])
    return
  elif cmds[0] == "show":
    comp.show(cmds[1])
    return
  elif cmds[1] == "->":
    gives = True
  elif cmds[1] == "!->":
    gives = False
  else:
    print("you've entered the wrong command, you should enter something like 'Santa -> Giftee'")
    return
  if cmds[0] == cmds[2]:
    print("You cannot be your own Santa")
    return
  comp.makeLink(cmds[0], cmds[2], gives)
  return

exit = ""
matrix = None
try:
  with open( "company.p", "r" ) as f:
    matrix = pickle.load(f)
except EOFError:
  print("matrix empty")

comp = Company()
if matrix is not None:
  comp.matrixToCompany(matrix)

while exit != "exit":
  string = raw_input("What do you want to do? > ")
  exit = returnInput(string, comp)
  matrix = comp.companyToMatrix()
  with open('company.p', 'wb') as f:
    pickle.dump(matrix, f)

  


  




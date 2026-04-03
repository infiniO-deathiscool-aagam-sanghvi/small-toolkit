import os
import random
import time
inputq = "start"
q = 0
definitions = []
while inputq != "stop":
  try:
    if q == 0:
      inputq = input("Enter your command! : ")
      inputa = inputq.split(" ")
    if inputa[0] == "timer":
      inputb = int(inputa[1])
      while inputb != 0:
        time.sleep(1)
        os.system('clear')
        print(inputb)
        inputb -= 1
    elif inputa[0] == "coin":
      print(random.choice(["Heads!","Tails!"]))
    elif inputa[0] == "help":
      print("Hi! I'm small-toolkit and I can do lots of things!\nWe can flip a coin (type \"coin\") or set a timer! (type \"timer 30\")")
    elif inputa[0] == "random":
      print(random.randint(int(inputa[1]),int(inputa[2])))
    elif inputa[0] == "dice":
      print(random.randint(1,6))
    elif inputa[0] == "run":
      del inputa[0]
      print(eval(" ".join(inputa)))
    elif inputa[0] == "def":
      del inputa[0]
      definitions.append([inputa.pop(1)," ".join(inputa)])
    elif any(row[0] == inputa[0] for row in definitions):
      inputa = inputa.slice(1)
      q = 1
      break
    else:
      print("ERROR.INVALID: Retry")
    q = 0         
  except:
    print("Are you sure you typed enough parameters? Restart the program to continue using it.")
      

import time
inputq = "start"
while inputq.lower() != "stop":
  inputq = input("Enter your command! : ")
  inputa = inputq.split(" ")
  if inputa[0] == "timer":
    inputq = int(inputa[1])
    while inputq != 0:
      time.sleep(1)
      print(inputq)
      inputq -= 1
    
  

'''
snake=1
water=-1
gun=0
'''

import random
computer=random.choice([-1,1,0])
youstr=input("enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={
  1:"Snake",-1:"Water",0:"Gun"
}
you=youDict[youstr]
print(f"You chose {reverseDict[you]}\nComputer chose{reverseDict[computer]}")
if(computer==you):
  print("It's draw")
else:
  if(computer==-1 and you==1):
    print("YOu Won!")
  elif(computer==-1 and you==0):
    print("YOu Lose!")
  elif(computer==-1 and you==-1):
    print("YOu Lose!")

    

import random
from playsound import playsound

mylist=[]

for x in range(1,6):
    mynumber = random.randint(1,60)
    mylist.append(mynumber)
    print(mylist)
    if x==3:
        playsound("aaliyah.mp3")




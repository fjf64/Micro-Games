import random 
import string
N = 10

word = input("enter only lowercase letters")

def halt():
    print("[ending]")
    pass
apple = True
while apple == True:
    god = ''.join(random.choices(string.ascii_lowercase, k=N))
    print(god)
    if word in god:
        halt()
        apple = False
print("word found")
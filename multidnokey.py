import time
import threading
import random
import sys
print("a = easy(2L) | b = medium(2L) | c = hard(3L) | d = impossible(4L) | e = gives aneurysms(5L)")
ms = (input())
dismode = {
    "a" : 20,
    "b" : 20,
    "c" : 20,
    "d" : 20,
    "e" : 20
}
timemode = {
    "a" : 3,
    "b" : 2,
    "c" : 2,
    "d" : 2,
    "e" : 2
}
donkeymode = {
    "a" : 3,
    "b" : 3,
    "c" : 4,
    "d" : 5,
    "e" : 6
}
blanemode = {
    "a" : 2,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5
}
lanemode = {
    "a" : 1,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4
}
tm = int(timemode[ms])
bdd = int(dismode[ms])
da = int(donkeymode[ms])
bm = int(blanemode[ms])
lm = int(lanemode[ms])
d = 1
death = 0
deadzone = 10
dnokeydead = 20
timeout = tm
dd = bdd
s = 0
pp = 0
dp = random.sample(range(1,da),lm)
live = 0
def dnokey():
    print("ded")
    print("score of "+str(s)+" donkeys passed, 1 donkey killed")
    exit()
while True:
    try:
        t = threading.Timer(timeout, dnokey)
        if d == 0:
            d = 1
            dd = bdd
            dp = random.sample(range(1,da),lm)
            s += 1
        dd -= 10
        timeout = tm
        if not t.is_alive():
            t.start()
        print("donkey is "+str(dd)+" feet away in lane "+str(dp)+" ...\n")
        pp = int(input())
        if pp < 1:
            print("stop cheating you churlish clay-brained bugbear")
            exit()
        if pp > bm:
            print("stop cheating you frothy elf-skinned haggard")
            exit()
        if dp.count(pp) >= 1 and dd <= deadzone:
            dnokey()
            death += 1
        if dd < dnokeydead:
            d = 0
        if t.is_alive:
            t.cancel()
    except ValueError:
        print("Ran Out Of Time :|")
        dnokey()
        death += 1
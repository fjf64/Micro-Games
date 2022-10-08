import threading as th
import time as t
import random as r
from threading import Timer
ans = 0
"""
todo - green-wargs, upgrades, ranch, temperry, duckberry, dice, finish slots
plant creation: shop, sell, timer, buy, crop, crops, stuffs
"""
def ask(type, failsafe, try_again = True):
    """[1] - int [2] - str [3] - any, fail output, try_again vs enter fail output (True by default), returns ans value"""
    global ans
    try:
        if type == 1:
            ans = input()
            ans = int(ans)
        elif type == 2:
            ans = str(input())
        else:
            ans = input()
    except:
        if try_again == True:
            print("[Wrong Input - Please try again]")
            ask(type, failsafe, try_again)
        if try_again == False:
            print("[Wrong Input]")
            ans = failsafe
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
def carootbuy():
    if stuffs["Radollar"] >= 3:
        if crops["caroots"] == 0:
            caroot_timer.start()
            crops["caroots"] += 1
            stuffs["Radollar"] -= 3
        elif crops["caroots"] != 0:
            crops["caroots"] += 1
            stuffs["Radollar"] -= 3
def toxishbuy():
    if stuffs["Radollar"] >= 10:
        if crops["toxishes"] == 0:
            toxish_timer.start()
            crops["toxishes"] += 1
            stuffs["Radollar"] -= 10
        elif crops["toxishes"] != 0:
            crops["toxishes"] += 1
            stuffs["Radollar"] -= 10
def noxcressbuy():
    if stuffs["Radollar"] >= 100:
        if crops["noxcresses"] == 0:
            noxcress_timer.start()
            crops["noxcresses"] += 1
            stuffs["Radollar"] -= 100
        elif crops["noxcresses"] != 0:
            crops["noxcresses"] += 1
            stuffs["Radollar"] -= 100
def wettucebuy():
    if stuffs["Radollar"] >= 500:
        if crops["wettuces"] == 0:
            wettuce_timer.start()
            crops["wettuces"] += 1
            stuffs["Radollar"] -= 500
        elif crops["wettuces"] != 0:
            crops["wettuces"] += 1
            stuffs["Radollar"] -= 500
def wargbudbuy():
    if stuffs["Radollar"] >= 2500:
        if crops["wargbuds"] == 0:
            wargbud_timer.start()
            crops["wargbuds"] += 1
            stuffs["Radollar"] -= 2500
        elif crops["wargbuds"] != 0:
            crops["wargbuds"] += 1
            stuffs["Radollar"] -= 2500
def caroot():
    stuffs["caroot"] += crops["caroots"]
def toxish():
    stuffs["toxish"] += crops["toxishes"]
def noxcress():
    stuffs["noxcress"] += crops["noxcresses"]
def wettuce():
    stuffs["wettuce"] += crops["wettuces"]
def wargbud():
    stuffs["wargbud"] += crops["wargbuds"]
caroot_timer = RepeatTimer(3, caroot)
#sell = 1
toxish_timer = RepeatTimer(5, toxish)
#sell = 4
noxcress_timer = RepeatTimer(.1, noxcress)
#sell = 1
wettuce_timer = RepeatTimer(5, wettuce)
#sell = 100
wargbud_timer = RepeatTimer(10, wargbud)
#sell = 1000
def loop():
    global ans
    print("Hello, please choose an option")
    print(choices)
    ask(3, 0)
    if ans == "shop" or ans == "s":
        print(str(stuffs["Radollar"]) + "-Rads")
        for key in shop:
            print(str(key) +"-"+ shop[key][0])
        print("What would you like to buy?")
        ask(2, 0)
        
        try:
            shop[ans][1]()
        except:
            print("error: skipping input\n")
            loop()
        """
        shop[ans][1]()
        """
    #cheat-os
    if ans == "rad":
        print("Radollars given")
        stuffs["Radollar"] += 10000
    if ans == "inv" or ans == "i":
        print(stuffs)
    if ans == "crops" or ans == "c":
        print(crops)
    if ans == "sell" or ans == "se":
        stuffs["Radollar"] += stuffs["caroot"]
        stuffs["caroot"] = 0
        stuffs["Radollar"] += stuffs["toxish"] * 4
        stuffs["toxish"] = 0
        stuffs["Radollar"] += stuffs["noxcress"] * 1
        stuffs["noxcress"] = 0
        stuffs["Radollar"] += stuffs["wettuce"] * 100
        stuffs["wettuce"] = 0
        stuffs["Radollar"] += stuffs["wargbud"] * 1000
        stuffs["wargbud"] = 0
    if ans == "game" or ans == "g":
        if stuffs["Radollar"] >= 1:
            stuffs["Radollar"] -= 1
            print("Would you like to play? [1] - rock,paper,scissors [2] - slots")
            ask(1, 0)
            if ans == 1:
                print("[1] - rock, [2] - paper, [3] - scissors")
                ask(1, 1)
                opponentmove = r.randint(1,3)
                if opponentmove == 1:
                    print("The oppenent chose rock")
                if opponentmove == 2:
                    print("The oppenent chose paper")
                if opponentmove == 3:
                    print("The oppenent chose scissors")
                if int(ans) == opponentmove:
                    print("Tie: 1.25 Radollars")
                    stuffs["Radollar"] = round(stuffs["Radollar"] * 1.25)
                    loop()
                if int(ans) + 1 == opponentmove:
                    print("you lost: -1 radollar")
                    loop()
                if int(ans) + 1 == opponentmove or ans == 3 and opponentmove == 1:
                    print("you lost: -1 Radollars")
                    loop()
                if int(ans) - 1 == opponentmove or ans == 1 and opponentmove == 3:
                    print("you won!: x2 Radollars")
                    stuffs["Radollar"] *= 2
                    loop()
                loop()
            if ans == 2:
                print("")
                slot1 = r.randint(1, 3)
                print(slot1)
                t.sleep(.1)
                slot2 = r.randint(1,3)
                print(slot2)
                if slot1 == slot2:
                    print("...")
                    t.sleep(1)
                else:
                    t.sleep(.1)
                slot3 = r.randint(1,3)
                print(slot3)
                if slot1 == slot2 and slot2 == slot3:
                    print("Payday! money multiplied")
                    stuffs["Radollar"] *= (slot1 * slot2 * slot3)
                    if slot1 == 3:
                        print("Lucky threes, multiplying Radollars")
                        stuffs["Radollar"] * 3
        else:
            print("Not enough Radollars")
        loop()
    loop()
stuffs = {
    "Radollar" : 5,
    "caroot" : 0,
    "toxish" : 0,
    "noxcress" : 0,
    "wettuce" : 0,
    "wargbud" : 0,
}
crops = {
    "caroots" : 0,
    "toxishes" : 0,
    "noxcresses" : 0,
    "wettuces" : 0,
    "wargbuds" : 0,
}
shop = {
    "1" : ["caroots = 3-Rads", carootbuy],
    "2" : ["Toxish = 10-Rads", toxishbuy],
    "3" : ["Noxcress = 100-Rads", noxcressbuy],
    "4" : ["wettuce = 500-Rads", wettucebuy],
    "5" : ["Wargbud = 2500-Rads", wargbudbuy],
}
choices = ["shop", "inv", "crops", "sell", "game <1-Rad> "]
loop()

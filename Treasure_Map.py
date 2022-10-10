import random as r
# to-do :: 
areamap = {}
oldpp = [4,5]
newpp = [4,5]
mapsize = [5, 10]
randevent = {
}
mapassite = {
}
camploc = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1)]
treasurelist = {
    1:"old bones",
    2:"fossilized pizza",
    3:"old cheese",
    4:"used rod",
}
shop_upgrades = {
    1:["golems", 5],
    2:["archeology tools", 25],
    3:["site-kits", 100],
}
upgrades = {
    "golems" : 0,
    "archeology tools" : 1,
    "site-kits" : 0,
}
backpack = {
    "t-coins" : 0,
    "golems": 0,
    "site-kits" : 0,
}
backlen = len(backpack)
blank = "\u25A1"
digging_spot = "0"
player = "\u0D9E"
campsy = "C"
site = "\u4DEF"
snake = "\u1F33"
eventchance = 1
if eventchance == 1: #digging spot
    randevent["snake"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), snake]
    if randevent["snake"] == camploc:
        randevent["snake"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), snake]
eventchance = 2
if eventchance == 2: #snake
    randevent["digging_spot"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), digging_spot]
    if randevent["digging_spot"] == camploc:
        randevent["digging_spot"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), digging_spot]
def bpreset():
    global backpack
    backpack = {
    "t-coins" : backpack["t-coins"],
    "golems": backpack["golems"],
    "site-kits" : backpack["site-kits"],
}
def makemap(x, y, item):
    for i in range(x):
        areamap[i] = item * y
def printmap():
    for key in areamap:
        print(areamap[key])
    print("")
def editmap(height, length, insert, playermovement = True):
    global oldpp
    global newpp
    if playermovement == True:
        oldpp = [height, length]
    length -= 1
    height -= 1
    editmap = list(areamap[height])
    editmap[length] = insert
    editmap = "".join(editmap)
    areamap[height] = editmap
    newpp = [height, length]
def ppmovemap():
    global fixcamp
    global newpp
    direinput = input("enter direction - (wasd):")
    if direinput == "w":
        editmap(oldpp[0], oldpp[1], blank)
        newpp = oldpp
        oldmapp = oldpp
        if newpp[0] > 1:
            newpp[0] -= 1
        else:
            print("Out of Bounds")
        editmap(newpp[0], newpp[1], player)
        printmap()
    if direinput == "a":
        editmap(oldpp[0], oldpp[1], blank)
        newpp = oldpp
        oldmapp = oldpp
        if newpp[1] > 1:
            newpp[1] -= 1
        else:
            print("Out of Bounds")
        editmap(newpp[0], newpp[1], player)
        printmap()
    if direinput == "s":
        editmap(oldpp[0], oldpp[1], blank)
        newpp = oldpp
        oldmapp = oldpp
        if newpp[0] < mapsize[0]:
            newpp[0] += 1
        else:
            print("Out of Bounds")
        editmap(newpp[0], newpp[1], player)
        printmap()
    if direinput == "d":
        editmap(oldpp[0], oldpp[1], blank)
        newpp = oldpp
        oldmapp = oldpp
        if newpp[1] < mapsize[1]:
            newpp[1] += 1
        else:
            print("Out of Bounds")
        editmap(newpp[0], newpp[1], player)
        printmap()
    if direinput == "bag" or direinput == "inv":
        print(backpack)
    if direinput == "motherlode":
        backpack["t-coins"] += 10000
    if direinput == "mother":
        backpack["t-coins"] += 100
    if direinput == "upgrades":
        print(upgrades)
    if direinput == "kit" and backpack["site-kits"] >= 1:
        mapassite[len(mapassite) + 1] = [oldpp[0], oldpp[1], "site", site, 0]
        backpack["site-kits"] -= 1
        print("kit placed")
def camp():
    global backpack
    print("Welcome to the survival camp, press [enter] to leave, input [1] to sell treasures, [2] to enter shop")
    campchoice = input()
    if campchoice == "":
        print("exiting camp")
    if campchoice == "1":
        for i in range(len(backpack) - backlen):
            backpack["t-coins"] += r.randint(upgrades["archeology tools"], upgrades["archeology tools"] * 10)
            bpreset()
    if campchoice == "2":
        for key in shop_upgrades:
            print(str(key) +" - "+ str(shop_upgrades[key][0]) +" - "+ str(shop_upgrades[key][1]))
        upgradechoice = input()
        try:
            upgradechoice = int(upgradechoice)
            if upgradechoice == 1 and backpack["t-coins"] >= shop_upgrades[1][1]:
                backpack["t-coins"] -= shop_upgrades[1][1]
                upgrades["golems"] += 1
                shop_upgrades[1][1] += 5
                print("Golem bought")
            if upgradechoice == 2 and backpack["t-coins"] >= shop_upgrades[2][1]:
                backpack["t-coins"] -= shop_upgrades[2][1]
                upgrades["archeology tools"] += 1
                shop_upgrades[2][1] += 25
                print("Tools bought")
            if upgradechoice == 3 and backpack["t-coins"] >= shop_upgrades[3][1]:
                backpack["t-coins"] -= shop_upgrades[3][1]
                if upgrades["site-kits"] <= 3:
                    backpack["site-kits"] += 1
                    upgrades["site-kits"] += 1
                else:
                    upgrades["site-kits"] += 1
                shop_upgrades[3][1] += 100
                print("archeology Site Kit bought - enter [kit] while on map to place - max = 3")
        except:
            print("Nothing bought")
    print(str(backpack["t-coins"]) + " Treasure Coins")
def accessite(sitenum):
    print(str(mapassite[sitenum][4])+" t-coins gained")
    backpack["t-coins"] += mapassite[sitenum][4]
    mapassite[sitenum][4] = -1
makemap(mapsize[0], mapsize[1], blank)
editmap(5, 5, player)
editmap(camploc[0], camploc[1], campsy, False)
while True:
    editmap(camploc[0], camploc[1], campsy, False)
    for key in randevent:
        editmap(randevent[key][0], randevent[key][1], randevent[key][2], False)
    for key in mapassite:
        editmap(mapassite[key][0], mapassite[key][1], mapassite[key][3], False)
    ppmovemap()
    if oldpp == [camploc[0], camploc[1]]:
        camp()
        backpack["golems"] = upgrades["golems"]
    if oldpp[0] == randevent["snake"][0] and oldpp[1] == randevent["snake"][1]:
        if backpack["golems"] == 0:
            print("You hit a snake! It stole your treasures and half your coins. ")
            bpreset()
            backpack["t-coins"] = round(backpack["t-coins"] / 2)
        else:
            backpack["golems"] -= 1
            print("A golem has protected you from the snake.")
        randevent["snake"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), snake]
        if randevent["snake"] == camploc:
            randevent["snake"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), snake]
    if oldpp[0] == randevent["digging_spot"][0] and oldpp[1] == randevent["digging_spot"][1]:
        foundtreasure = r.randint(1, len(treasurelist)) 
        print("digging_spot located. "+treasurelist[foundtreasure]+" found!")
        if treasurelist[foundtreasure] in backpack:
            backpack[treasurelist[foundtreasure]] += 1
        else:
            backpack[treasurelist[foundtreasure]] = 1
        randevent["digging_spot"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), digging_spot]
        if randevent["digging_spot"] == camploc:
            randevent["digging_spot"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), digging_spot]
    for key in mapassite:
        if oldpp[0] == mapassite[key][0] and oldpp[1] == mapassite[key][1]:
            accessite(key)
    for key in mapassite:
        mapassite[key][4] += upgrades["site-kits"]
    eventchance = r.randint(1,25)
    if eventchance == 1: #digging spot
        randevent["snake"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), snake]
        if randevent["snake"] == camploc:
            del randevent["snake"]
    if eventchance == 2: #snake
        randevent["digging_spot"] = [r.randint(1, mapsize[0] - 1), r.randint(1, mapsize[1] - 1), digging_spot]
        if randevent["digging_spot"] == camploc:
            del randevent["digging_spot"]

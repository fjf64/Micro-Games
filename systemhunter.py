#!!! NOT FINISHED !!!#
import time as t
import random as r
"""todo: finish forest, finish enemy attacks, add quest system, power shards, loot,"""
"""codes: [qb] - quest builder, """
#hidden functions
#variables
savecode = 0000
cheatcode = 1019999999900
#1,01,99,99,9999,00
enemy_stats = {0}
quest =["",]
qbfcom = {}
target_magic_attack = 0
target_attack = 0
target_defense = 0
target_magic_defense = 0
target_magic_pool = 0
target_physical_pool = 0
current_magic_pool = 0
current_physical_pool = 0
temp_physical_defense = 0
temp_magic_defense = 0
current_ap = 0
current_mp = 0
past_sword_strike_form = 1
sword_strike_form = 1
low_level = 0
high_level = 0
bload = 0
classpick = 0
qb = 0
qbfl = 1
physical_damage_done = 0
magic_damage_done = 0
target_selection = 0
current_location = 1
passive_count = 1
#real functions
def ask(type, failsafe, try_again = True):
    """[1] - int [2] - str [3] - any, fail output, try_again vs enter fail output (True by default), returns ans value"""
    global ans
    try:
        if type == 1:
            ans = int(input())
        if type == 2:
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
#Functions
def qbf():
    global quest
    global qbfl
    qbff()
    print("[welcome to the quest builder!")
    while qbfl == 1:
        print("[?] to get options]")
        ask(3,0)
        """
        try:
            qbfcom[ans][0]()
        except:
            print("something went wrong.")
            pass
        """
        qbfcom[ans][0]()
        
def qbff():
    global quest
    global qbfcom
    def hell():
        for key in qbfcom:
            print(str(key)+" - "+qbfcom[key][1])
    def manual():
        manuals = {
            1 : ["quest name", "slot 0 is dedicated to the quest name"],
        }
        print("Welcome to the manual, options are listed below.")
        print("type esc to escape.")
        for key in manuals:
            print(str(key) +" - "+ manuals[key][0])
        ask(3,0)
        if ans != "esc":
            try:
                print(manuals[int(ans)][1])
            except:
                print("Wrong input, returning to menu.")
                pass
    def text():
        global quest
        print("text position?:")
        for x in range(len(quest)):
            print(str(x) +" - "+ str(quest[x]))
        ask(1,0)
        spot = ans
        print("text?")
        ask(3,0)
        try:
            quest.insert(int(spot), str(ans))
        except:
            try:
                print("error, your text is: "+ str(ans))
            except:
                print("you did something very wrong.")
        for x in range(len(quest)):
            print(str(x) +" - "+ str(quest[x]))
    def questcheck():
        global quest
        for x in range(len(quest)):
            print(str(x)+" - "+quest[x])
    qbfcom = {
        "?" : [hell, "lists commands"],
        "m" : [manual, "manual, lists important info for building quests. "],
        "q" : [questcheck, "view quest"],
        "t" : [text, "add text to the quest"],
    }
    print("[functions ready!]")
def nothing():
    print("[nothing happened]\n")
    pass
def attack_nothing():
    print("[nothing happened]\n")
    attack_you()
def loadsave():
    global current_location
    global bload
    global clear_check
    global qb
    code = savecode
    bload = 1
    if int(str(code)[1-3]) >= 1:
        current_location = int(str(code)[1:3])
    if int(str(code)[3-5]) >= 1:
        for x in range(int(str(code)[3:5])):
            swordsman()
    if int(str(code)[5-7]) >= 1:
        for x in range(int(str(code)[5:7])):
            mage()
    if int(str(code)[7-11]) >= 1:
        stats["combat-Experience"] = (int(str(code)[7:11]))
        print("[Current combat experience: "+str(stats["combat-Experience"])+"]")
    if (int(str(code)[11-12]) * 10) + int(str(code)[12-13]) >= 1:
        for x in range(int(str(code)[11:13])):
            clear_check["dark_forest"] += 1
    print(clear_check["dark_forest"])
    for key in classes:
        print("[" + key + "]")
    print("[Curent Location - "+alt_locations[current_location]+"]\n")
    bload = 0
    print(clear_check["dark_forest"])
def savesave():
    pass
#player default ablilities
def player_stat_check():
    print("Stats:")
    print(stats, sep=",  ")
    print("Passives:")
    print(alt_passives, sep=", ")
    print("Buffs:")
    for key in buffs:
        print(buffs[key][3] +", "+ str(buffs[key][2]))
    print("Debuffs:")
    for key in debuffs:
        print(debuffs[key][3] +", "+ str(debuffs[key][2]))
    attack_you()
def list_attack_commands():
    comcalling = alt_attack_commands
    for key in alt_attack_commands:
        print("["+key+" - "+alt_attack_commands[key]+"]")
    attack_you()
def attack_you():
    #"""
    try:
        print("[choose your attack - [?] for options - "+str(stats["ap"])+" ap | mp "+str(stats["mp"])+"]")
        selection = input()
        attack_commands[selection]()
    except:
        print("[Error: Incorrect Response - Choosing to do nothing.]\n")
        selection = ""
        attack_commands[selection]()

    #debug code
    """
    print("[choose your attack - [?] for options - "+str(stats["ap"])+" ap | mp "+str(stats["mp"])+"]")
    selection = input()
    attack_commands[selection]()
    """
def Lizzie():
    global target_magic_pool
    target_magic_pool += 7.5
def Rafe():
    global target_physical_pool
    global temp_physical_defense
    target_physical_pool += 7.5
    temp_physical_defense += 2
def target_stat_check():
    coc = 1
    print(""+str(enemy_stats[target_selection][5])+" Stats:}")
    for x in enemy_stats[target_selection]:
        if coc == 1:
            print(str(x) + " hp, ")
        if coc == 2:
            print(str(x) + " attack, ")
        if coc == 3:
            print(str(x) + " magic attack, ")
        if coc == 4:
            print(str(x) + " defense, ")
        if coc == 5:
            print(str(x) + " magic defense\n")
        coc += 1
    attack_you()
#player classes
def swordsman():
    global classes
    global stats
    if classes["swordsman"] == 0:
        print("[Class Added: Swordsman]")
        print("\n[The Swordsman is a class that specializes in close combat and physical prowess regarding swords. Sword Strike has the ability to switch between a two-handed striking form and a parrying shield form. \n[s1] / [s2] are shortcuts for swordstrike form.]\n")
        print("[you have gained strength, attack points(ap) and extra defense.]\n")
        classes["swordsman"] += 1
        stats["strength"] = 1
        stats["hp"] += 10
        stats["defense"] += 1
        stats["ap"] = 3
        attack_commands["s"] = sword_strike
        alt_attack_commands["s"] = "sword_strike"
        attack_commands["s1"] = sword_strike_1
        attack_commands["s2"] = sword_strike_2
        passives[passive_count] = parry
        alt_passives.append("parry")
    else:
        if bload == 0:
            print("[swordsman already acquired: Awarding Statpoints]\n")
        classes["swordsman"] += 1
        stats["strength"] += 1
        stats["defense"] += 1
        stats["ap"] += 1
        stats["hp"] += 5
def sword_strike():
    global target_physical_pool
    global current_ap
    global temp_physical_defense
    global temp_magic_defense
    global past_sword_strike_form
    global sword_strike_form
    past_sword_strike_form = sword_strike_form
    try:
        sword_strike_form = int(input("[ [1] - Striking Form ,[2] - Shield Form ]\n"))
    except:
        sword_strike_form = 1
    if sword_strike_form == 1:
        if current_ap >= 0:
            print("[Striking Form Chosen]\n")
            target_physical_pool += (stats["strength"] + 1) * 5 + stats["combat-Experience"]
            current_ap -= 0
    if sword_strike_form == 2:
        if current_ap >= 0:
            print("[Shield Form Chosen]\n")
            target_physical_pool += stats["strength"] * 5 + stats["combat-Experience"]
            temp_physical_defense += round(stats["defense"] / 2)
            current_ap -= 0
def sword_strike_1():
    global target_physical_pool
    global current_ap
    global temp_physical_defense
    global temp_magic_defense
    global past_sword_strike_form
    global sword_strike_form
    past_sword_strike_form = sword_strike_form
    sword_strike_form = 1
    if sword_strike_form == 1:
        if current_ap >= 0:
            print("[Striking Form Chosen]\n")
            target_physical_pool += (stats["strength"] + 1) * 5 + stats["combat-Experience"]
            current_ap -= 0
    if sword_strike_form == 2:
        if current_ap >= 0:
            print("[Shield Form Chosen]\n")
            target_physical_pool += stats["strength"] * 5 + stats["combat-Experience"]
            temp_physical_defense += round(stats["defense"] / 2)
            current_ap -= 0
def sword_strike_2():
    global target_physical_pool
    global current_ap
    global temp_physical_defense
    global temp_magic_defense
    global past_sword_strike_form
    global sword_strike_form
    past_sword_strike_form = sword_strike_form
    sword_strike_form = 2
    if sword_strike_form == 1:
        if current_ap >= 0:
            print("[Striking Form Chosen]\n")
            target_physical_pool += (stats["strength"] + 1) * 5 + stats["combat-Experience"]
            current_ap -= 0
    if sword_strike_form == 2:
        if current_ap >= 0:
            print("[Shield Form Chosen]\n")
            target_physical_pool += stats["strength"] * 5 + stats["combat-Experience"]
            temp_physical_defense += round(stats["defense"] / 2)
            current_ap -= 0
def parry():
    global target_physical_pool
    if past_sword_strike_form == 2 and sword_strike_form == 1:
        target_physical_pool += physical_damage_done * round(stats["defense"] / 2)
        print("[Parry! - "+str(physical_damage_done * round(stats["defense"] /2))+" - Extra Damage.]\n")

def mage():
    global classes
    global stats
    global passive_count
    if classes["mage"] == 0:
        print("[Class Added: Mage]")
        print("\n[The Mage excels in the use of pure magic, and specializes in magical attacks. Mana_strike has the ability to attack with both physical and magical damage. mages possess the passive of area-attacking spells.]\n")
        print("[you have gained willpower, mana points(mp) and extra magic defense.]\n")
        classes["mage"] += 1
        stats["willpower"] = 2
        stats["magic-defense"] += 1
        stats["mp"] = 3
        stats["hp"] += 5
        attack_commands["m"] = magic_strike
        alt_attack_commands["m"] = "magic_strike"
        passives[passive_count] = area_spells
        alt_passives.append("area spells")
        passive_count += 1

    else:
        if bload == 0:
            print("[mage already acquired: Awarding Statpoints]\n")
        classes["mage"] += 1
        stats["willpower"] += 1
        stats["magic-defense"] += 1
        stats["mp"] += 1
        stats["hp"] += 5
def magic_strike():
    global target_magic_pool
    global target_physical_pool
    global current_mp
    if current_mp >= 0:
        target_magic_pool += stats["willpower"] * 3 + stats["combat-Experience"]
        target_physical_pool += stats["willpower"] * 3 + stats["combat-Experience"]
        current_mp -= 0
# enemy attacks
def area_spells():
    global target_magic_pool
    for key in enemy_stats.keys():
        if key != target_selection and len(enemy_stats) > 1:
            loop_enemy = enemy_stats[key]
            if not (loop_enemy[0] - round(target_magic_pool / len(enemy_stats))) <= 0:
                loop_enemy[0] -= round((round((target_magic_pool + stats["combat-Experience"]) / len(enemy_stats)) / loop_enemy[4]) + .4)
            else:
                loop_enemy[0] = 0
#monster attacks
def goop():
    global current_magic_pool
    global current_physical_pool
    global temp_physical_defense
    global temp_magic_defense
    print("You have been gooped!\n")
    current_magic_pool += enemy_stats[target_selection][2]
    current_physical_pool += target_attack
    debuffs[len(buffs)] = [gooped, low_level, high_level, "gooped!"]
def gooped(power, length):
    global temp_physical_defense
    if (stats["defense"] - power) != 0:
        temp_physical_defense -= power
def goblin_mode():
    global current_magic_pool
    global current_physical_pool
    global temp_physical_defense
    global temp_magic_defense
    print("You have been hit!\n")
    current_physical_pool += round(1.5 * enemy_stats[target_selection][1] + len(enemy_stats))
def aggressive_sniff():
    global current_magic_pool
    global current_physical_pool
    global temp_physical_defense
    global temp_magic_defense
    print("You have been sniffed!\n")
    current_physical_pool += round(1.5 * enemy_stats[target_selection][1])
def bite():
    global current_magic_pool
    global current_physical_pool
    global temp_physical_defense
    global temp_magic_defense
    print("You have been bitten!\n")
    current_physical_pool += round(5 * enemy_stats[target_selection][1])
def startup():
    global savecode
    global classpick
    print("[Hello!]\n[I am the System, here to be your eyes and ears on this journey. but first, if you have a save code, please enter it. if not, hit enter to skip it.] ")

    savecode = input()
    if savecode == "qb":
        qbf()
    try:
        savecode = int(savecode)
    except:
        if savecode == "":
            pass
        else:
            print("[Error: Incorrect Response]")
            savecode = ""
    if savecode != "":
        loadsave()
    print("[Loading Successful: Entering Tutorial\n]")
    print("[Please select a class.]")
    print("[1] - swordsman, [2] - mage")
    try:
        classpick = int(input())
    except:
        print("Error: Incorrect Response - Class chosen\n")
        classpick = 1
    if classpick != 1 and classpick != 2:
        print("Error: Incorrect Response - Class chosen\n")
        classpick = 1
    if classpick == 1:
        swordsman()
    if classpick == 2:
        mage()
    print("[Transferring you to "+alt_locations[current_location]+"...]")
    locations[current_location]()
def dark_forest():
    print("[You have entered the dark forest.]")
    if clear_check["dark_forest"] == 0:
        print("[Huge trees surround you and the sound of wild beasts draws louder.]\n[The Best course of action is to escape the forest before you become prey to a beast out of your league.] \n[Numerous monster are hunting you while you try to escape the forest.]\n")
    print("[enter [?] to see your abilities during a battle.]\n")
    if clear_check["dark_forest"] == 0:
        for x in range(3):
            fight(1, 3, 1, 3, 1, 1, 3, True)
        clear_check["dark_forest"] = 1
    if clear_check["dark_forest"] == 1:
        print("[In the distance you see a swordsman and a mage fighting a pack of wolves - press enter to continue]\n")
        next = input()
        for x in range(3):
            x = x+1
            fight(x, x*2, 1, 1, 1, 4, 4, False)
        print("[The wolves have been defeated. The mage and swordsman approach to talk to you.]\n")
        next = input()
        print("W.I.P.")

def fight(low, high, enemy_min_count, enemy_max_count, location_number, low_enemy_type, high_enemy_type, desperation):
    global target_physical_pool
    global target_magic_pool
    global target_attack
    global target_magic_attack
    global target_defense
    global target_magic_defense
    global current_physical_pool
    global current_magic_pool
    global temp_magic_defense
    global temp_physical_defense
    global stats
    global enemy_stats
    global target_selection
    global low_level
    global high_level
    global physical_damage_done
    global magic_damage_done
    low_level = low
    high_level = high
    target_magic_pool = 0
    target_physical_pool = 0
    dot_pyhisical = 0
    dot_magic = 0
    dot_physical_time = 0
    dot_magic_time = 0

    #pos : health, attack, magic attack, defense, magic defense
    enemy_stats = {
    }
    count_counter = 1
    enemy_count = r.randint(enemy_min_count, enemy_max_count)
    while enemy_count > 0:
        chosen_enemy = r.randint(low_enemy_type, high_enemy_type)
        enemy_stats[count_counter] = [r.randint(low * 5,high * 5), r.randint(low ,high), r.randint(low,high), r.randint(low,high), r.randint(low,high), enemies[chosen_enemy]]
        count_counter += 1
        enemy_count -= 1
    print("[You have encountered " + str(len(enemy_stats)) + " enemy/'s]\n")
    current_ap = stats["ap"]
    current_mp = stats["mp"]
    while len(enemy_stats) > 0:
        for key in enemy_stats:
            print(str(key)+" - "+str(enemy_stats[key]))
        try:
            target_selection = int(input("[select your target:]\n"))
            if len(enemy_stats) >= 1 and len(enemy_stats) <= 2 and len(party) >= len(
                    enemy_stats) and desperation == True:
                target_stat_spice = round((((len(enemy_stats) ** 2) * 3.7) - .6 * len(enemy_stats)) - .1)
                stat_counter = 1
                while stat_counter < 3:
                    # do stat multi
                    enemy_stats[target_selection][stat_counter] *= target_stat_spice
                    stat_counter += 1
                while stat_counter >= 3 and stat_counter < 5:
                    # do stat multi
                    enemy_stats[target_selection][stat_counter] /= enemy_stats[target_selection][stat_counter]
                    stat_counter += 1
                print("[You have evenly matched or outnumbered the enemy: They have gotten reckless in desperation]\n")
            current_hp = stats["hp"]

        except:
            print("[Error: Incorrect Response - targeting enemy]\n")
            target_selection = next(iter(enemy_stats))
            if len(enemy_stats) >= 1 and len(enemy_stats) <= 2 and len(party) >= len(enemy_stats):
                target_stat_spice = round((((len(enemy_stats) ** 2) * 3.7) - .6 * len(enemy_stats)) - .1)
                stat_counter = 1
                while stat_counter < 3:
                    # do stat multi
                    enemy_stats[target_selection][stat_counter] *= target_stat_spice
                    stat_counter += 1
                while stat_counter >= 3 and stat_counter < 5:
                    # do stat multi
                    enemy_stats[target_selection][stat_counter] /= enemy_stats[target_selection][stat_counter]
                    stat_counter += 1
                print("[You have evenly matched or outnumbered the enemy: They have gotten reckless in desperation]\n")
            current_hp = stats["hp"]
        while enemy_stats[target_selection][0] > 0:
            #friendly turn
            for key in party:
                party[key]()
            target_magic_pool += dot_magic
            target_physical_pool += dot_pyhisical
            if dot_magic_time > 0 or dot_physical_time > 0:
                dot_physical_time -= 1
                dot_magic_time -= 1
            for key in passives:
                passives[key]()
            for key in enemy_stats.copy():
                target_stats_health = enemy_stats[key]
                if target_stats_health[0] <= 0:
                    del enemy_stats[key]
                    records["battles"] += 1
                    print("[Combat Experience gained]\n")
                    print("[Coins gained]\n")
                    stats["coins"] += r.randint(low, high)
                    stats["combat-Experience"] += r.randint(low, high)
            enemy_attacks[enemy_stats[target_selection][5]]()
            for key in buffs:
                if buffs[key][2] > 0:
                    buffs[key][0](buffs[key][1], buffs[key][2])
                    buffs[key][2] -= 1
                else:
                    del buffs[key]
            for key in debuffs.copy():
                if debuffs[key][2] > 0:
                    debuffs[key][0](debuffs[key][1], debuffs[key][2])
                    debuffs[key][2] -= 1
                else:
                    del debuffs[key]
            enemy_stats[target_selection][0] -= round((target_physical_pool / enemy_stats[target_selection][3]) + .4)
            physical_damage_done = round((target_physical_pool / enemy_stats[target_selection][3]) + .4)
            enemy_stats[target_selection][0] -= round((target_magic_pool / enemy_stats[target_selection][4]) + .4)
            magic_damage_done = round((target_magic_pool / enemy_stats[target_selection][4]) + .4)
            print("{Target Hp State:}")
            print(str(physical_damage_done+magic_damage_done) + " damage done | health left " + str(enemy_stats[target_selection][0]) + "\n")
            #enemy turn
            current_hp -= round((current_physical_pool / (stats["defense"] + temp_physical_defense)) + .4)
            current_physical_damage_done = round((current_physical_pool / (stats["defense"] + temp_physical_defense)) + .4)
            current_hp -= round((current_magic_pool / (stats["magic-defense"] + temp_magic_defense) + .4))
            current_magic_damage_done = round((current_magic_pool / (stats["magic-defense"] + temp_magic_defense)) + .4)
            print("{Player Hp State:}")
            print(str(current_physical_damage_done+current_magic_damage_done) + " damage taken | Hp " + str(current_hp) + "\n")
            target_magic_pool = 0
            target_physical_pool = 0
            current_physical_pool = 0
            current_magic_pool = 0
            temp_magic_defense = 0
            temp_physical_defense = 0
            if current_hp <= 0:
                print("You have died and dropped your coins. Resurrecting at last location. \n")
                locations[location_number]()
        else:
            del enemy_stats[target_selection]
            records["battles"] += 1
            print("[Combat Experience gained]\n")
            print("[Coins gained]\n")
            stats["coins"] += r.randint(low, high)
            stats["combat-Experience"] += r.randint(low, high)

#lists
classes ={
    "swordsman": 0,
    "mage": 0
}
stats = {
    "coins" : 5,
    "hp" : 10,
    "magic-defense" : 1,
    "defense" : 1,
    "combat-Experience" : 0,
    "ap" : 0,
    "mp" : 0,
}
passives = {

}
alt_passives = [

]
# num - name, power, length
buffs = {

}
debuffs = {

}
#attack commands
attack_commands = {
    "?" : list_attack_commands,
    "help" : list_attack_commands,
    "pl" : player_stat_check,
    "" : attack_nothing,
    "l" : target_stat_check,
}
alt_attack_commands = {
    "?" : "list attack commands",
    "pl" : "player stats",
    "l" : "target stats",
}
enemies =  {
    #dark forest
    1:"Slime",
    2:"Goblin",
    3:"Large Shrew",
    4:"Wolf"
}
enemy_attacks =  {
    #dark forest
    "Slime":goop,
    "Goblin":goblin_mode,
    "Large Shrew":aggressive_sniff,
    "Wolf":bite,
}
#locations
locations = {
    1 : dark_forest,
}
alt_locations = {
    1 : "dark forest",
}
clear_check = {
    "dark_forest" : 0,
}
party = {
    1 : attack_you,
}
records = {
    "battles" : 0,
}
#startup
startup()

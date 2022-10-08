import random as r
def most_frequent(List):
    return max(set(List), key = List.count)
movechances = {"a":r.randint(20, 40), "d":r.randint(20, 40), "p":r.randint(20, 40)}
lastmove_a = ""
lastmove_b = ""
lastmove_c = ""
falseparry = 0
aiwincount = 0
playerwincount = 0
ai_falseparry = 0
allmoves = []
movechancesadder = {"a":0, "d":0, "p":0}
gamemoves = []
moves = ["a", "d", "p"]
while True:
    print("player wins - "+str(playerwincount)+"\nAI wins - " +str(aiwincount))
    gamemoves = []
    player_health = 100
    aihealth = 100
    while player_health > 0 and aihealth > 0:
        print("player health - "+str(player_health)+ "\nAI health - "+str(aihealth))
        pastaihealth = aihealth
        if falseparry == 0:
            move = input("[a] - attack [d] - defend [p]")
            if move not in moves:
                move = "d"
        if falseparry == 1:
            move = "v"
            falseparry = 0
        lastmove_a = move
        allmoves.append(move)
        gamemoves.append(move)
        lastmove_b = lastmove_a
        lastmove_c = lastmove_b
        if ai_falseparry == 0:
            aimove = max(movechances, key=movechances.get)
        if move == "v":
            aimove = "a"
        if ai_falseparry == 1:
            aimove = "v"
            ai_falseparry = 0
        #insert ai move chance
        #attack
        if move == "a" and aimove == "a":
            print("AI attacked, both health -20")
            player_health -= 20
            aihealth -= 15
        if move == "a" and aimove == "d":
            print("AI defended, AI health -15")
            aihealth -= 15
        if move == "a" and aimove == "p":
            print("AI parried, player health -30")
            player_health -= 30
        
        #defend
        if move == "d" and aimove == "a":
            print("AI attacked, player health -15")
            player_health -= 15
        if move == "d" and aimove == "d":
            print("AI defended, no change")
        if move == "d" and aimove == "p":
            print("AI parried, AI vulnerable")
            ai_falseparry = 1
            movechances["p"] -= 5
            
        #parry
        if move == "p" and aimove == "a":
            aihealth -= 30
            print("AI attacked, AI vulnerable")
            movechances["a"] -= 5
            ai_falseparry = 1
        if move == "p" and aimove == "d":
            print("AI defended, you are vulnerable")
            falseparry = 1
        if move == "p" and aimove == "p":
            print("AI parried, nothing happens")
            ai_falseparry = 1
        
        #vulnerable
        if move == "a" and aimove == "v":
            aihealth -= 20
            print("AI vulnerable, -20 AI health")
        if move == "d" and aimove == "v":
            print("nothing happened")
        if move == "p" and aimove == "v":
            print("nothing happened")
        if move == "v" and aimove == "a":
            print("AI attacked while you were vulnerable -20 health")
            player_health -= 20
            
        #AI parameters
        if lastmove_a == "a" and lastmove_b == "p":
            movechances["d"] += 25
        if pastaihealth > aihealth and aimove != "v":
            movechances[aimove] -= 25
        if pastaihealth > aihealth and aimove == "v":
            movechances["p"] -= 25
        if aimove == move:
            movechances[r.choice(list(movechances.keys()))] += 5
            
    #death
    if player_health <= 0:
        print("You died. re-entering battle")
        aiwincount += 1
    if aihealth <= 0:
        print("You killed the AI. re-entering battle")
        playerwincount += 1
        if most_frequent(gamemoves) == "a":
            movechances["p"] += 25
            if movechances["p"] > 100 or movechances["p"] < 0:
                movechances["p"] = 100
        if most_frequent(gamemoves) == "d" :
            movechances["a"] += 25
            if movechances["a"] > 100 or movechances["a"] < 0:
                movechances["a"] = 100
        if most_frequent(gamemoves) == "p":
            movechances["d"] += 25
            if movechances["d"] > 100 or movechances["d"] < 0:
                movechances["d"] = 100
    if aihealth <= 0 or player_health <= 0:
        print("WIP")
        movechancesadder["p"] += allmoves.count("a")
        movechancesadder["d"] += allmoves.count("p")
        movechancesadder["a"] += allmoves.count("d")
        for key in movechancesadder:
            if movechancesadder[key] > 50:
                movechancesadder = 25
        movechances["a"] += movechancesadder["a"]
        movechances["d"] += movechancesadder["d"]
        movechances["p"] += movechancesadder["p"]
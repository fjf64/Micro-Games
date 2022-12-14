import random as r
if True:
    # A small package + a starter line or two, that is used for making maps and visuals.
    #To-Do :: 
    """ map coords
        #ABCD
        1####
        2####
        3####
        4####
    """
    areamap = {} # if a custom map was made, insert here
    walker_pos_list = []
    mapsize = [5, 100] #!!! IMPORTANT !!!#
    mapmid = [round(mapsize[0] / 2), round(mapsize[1] / 2)]
    oldpp = [3, 50] # INITIAL PLAYER POSITION
    origin = oldpp
    newpp = oldpp
    player = "X"
    blank = "#"
    walkable = " "
    def makemap(x, y, item):
        """use walkable as item if you want the whole map to be transversal"""
        for i in range(x):
            areamap[i] = item * y
    def printmap():
        for key in areamap:
            print(areamap[key])
        print("")
    def readmap(length, height, returnfalse = True):
        "returns icon at location, tends to be wrong"
        global areamap
        try:
            length -= 1
            height -= 1
            expandedmap = list(areamap[height])
            readoutput = expandedmap[length]
            print(readoutput)
            return readoutput
        except KeyError:
            if returnfalse == True:
                return blank
    def editmap(height, length, insert, playermovement = False):
        """making changes in map, insert is the text added and playermovement can be ignored unless it changes the player position. """
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
        """basic player movement built in to the package. """
        global fixcamp
        global newpp
        direinput = input("enter direction - (wasd):")
        if direinput == "w":
            editmap(oldpp[0], oldpp[1], walkable, True)
            newpp = oldpp
            oldmapp = oldpp
            if newpp[0] > 1 and [newpp[0] - 1, newpp[1]] in walker_pos_list:
                newpp[0] -= 1
            else:
                print("Out of Bounds")
            editmap(newpp[0], newpp[1], player, True)
            printmap()
        if direinput == "a":
            editmap(oldpp[0], oldpp[1], walkable, True)
            newpp = oldpp
            oldmapp = oldpp
            if newpp[1] > 1 and [newpp[0], newpp[1] - 1] in walker_pos_list:
                newpp[1] -= 1
            else:
                print("Out of Bounds")
            editmap(newpp[0], newpp[1], player, True)
            printmap()
        if direinput == "s":
            editmap(oldpp[0], oldpp[1], walkable, True)
            newpp = oldpp
            oldmapp = oldpp
            if newpp[0] < mapsize[0] and [newpp[0] + 1, newpp[1]] in walker_pos_list:
                newpp[0] += 1
            else:
                print("Out of Bounds")
            editmap(newpp[0], newpp[1], player, True)
            printmap()
        if direinput == "d":
            editmap(oldpp[0], oldpp[1], walkable, True)
            newpp = oldpp
            oldmapp = oldpp
            if newpp[1] < mapsize[1] and [newpp[0], newpp[1] + 1] in walker_pos_list:
                newpp[1] += 1
            else:
                print("Out of Bounds")
            editmap(newpp[0], newpp[1], player, True)
            printmap() # Map Package - minimize
    def pathgen(path_length,path_stretch = 1, path_bias_x = 0, path_bias_y = 0):
        global walker_pos_list
        """creates randomized paths using [walkable] variable as the path, and path stretch is the linear distance covered before changing direction.  path bias is if the path leans towards verticality or horizontal movement, with a higher or lower ratio changing the amount of times it re-rolls the direction"""
        oldpp = origin
        random_walkers = [oldpp[0], oldpp[1]]
        walker_pos_list = [[oldpp[0], oldpp[1]]]
        while path_length > 0:
            cwbiasx = path_bias_x
            cwbiasy = path_bias_y
            walker_direction = r.randint(1,2)
            while walker_direction != 2 and cwbiasx > 0:
                walker_direction = r.randint(1,2)
                cwbiasx -= 1
            while walker_direction != 1 and cwbiasy > 0:
                walker_direction = r.randint(1,2)
                cwbiasy -= 1
            walker_speed = r.choice([-1, 1])
            for x in range(path_stretch):
                if walker_direction == 1:
                    random_walkers[0] += walker_speed
                if walker_direction == 2:
                    random_walkers[1] += walker_speed
                if random_walkers[0] <= mapsize[0] and random_walkers[1] <= mapsize[1] and random_walkers[0] >= 1 and random_walkers[1] >= 1:
                    if not random_walkers in walker_pos_list:
                        walker_pos_list.append([random_walkers[0], random_walkers[1]])
                        path_length -= 1
                else:
                    random_walkers[0] = walker_pos_list[0][0]
                    random_walkers[1] = walker_pos_list[0][1]
            for x in range(len(walker_pos_list)):
                editmap(walker_pos_list[x][0], walker_pos_list[x][1], walkable)
makemap(mapsize[0],mapsize[1], blank)
pathgen(100, 2, 3)
editmap(oldpp[0], oldpp[1], player, True)
printmap()
while True:
    ppmovemap()

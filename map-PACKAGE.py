import random as r
if True:
    # A small package + a starter line or two, that is used for making maps and visuals.
    """ map coords
        #ABCD
        1####
        2####
        3####
        4####
    """
    areamap = {}
    pathgen_parameters = 50
    walker_pos_list = []
    mapsize = [5, 10] #!!! IMPORTANT !!!#
    mapmid = [round(mapsize[0] / 2), round(mapsize[1] / 2)]
    oldpp = [3, 5] # INITIAL PLAYER POSITION
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
    def pathgen(path_length):
        global walker_pos_list
        """creates randomized paths using [walkable] variable as the path icon"""
        oldpp = origin
        random_walkers = [oldpp[0], oldpp[1]]
        walker_pos_list = [[oldpp[0], oldpp[1]]]
        while path_length > 0:
            walker_direction = r.randint(1,2)
            if walker_direction == 1:
                random_walkers[0] += r.choice([-1, 1])
            if walker_direction == 2:
                random_walkers[1] += r.choice([-1, 1])
            if random_walkers[0] <= mapsize[0] and random_walkers[1] <= mapsize[1] and random_walkers[0] >= 1 and random_walkers[1] >= 1:
                walker_pos_list.append([random_walkers[0], random_walkers[1]])
                path_length -= 1
            else:
                random_walkers[0] = walker_pos_list[0][0]
                random_walkers[1] = walker_pos_list[0][1]
        for x in range(len(walker_pos_list)):
            editmap(walker_pos_list[x][0], walker_pos_list[x][1], walkable)
makemap(mapsize[0],mapsize[1], blank)
pathgen(pathgen_parameters)
editmap(oldpp[0], oldpp[1], player, True)
printmap()
while True:
    ppmovemap()

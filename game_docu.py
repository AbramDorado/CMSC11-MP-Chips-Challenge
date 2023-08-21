import End_Art

'''
    Description:    The read_file function reads the content of the text files
                    which are the 3 Maps
    Arguments:
        Map_number  The name of the text file to be read

    Returns:
        data        Return type is a string and it will be used as the Map of
                    the game
'''
#read file
def read_file(Map_number):
    text_file = open("%s"%(Map_number), "r")
    data = text_file.read()
    text_file.close()
    return data

'''
    Description:        The switch_place auxiliary function is to move the player '@'
                        across the map, it switches place with the tile next to it
                        whether it is up, down, left, right
    Arguments:
        line_as_list    Makes the Map string as a list, it used to get the value of the index of the 
                        positions of the player and the surounding tiles
        new_pos         The new position of the player according to the direction that
                        was chosen, and the symbol will be changed to '@'
        pos             The index of the location of the player, new_pos will be stored
                        in it so that the index will be updated for the next move of
                        the player

    Returns:
      None
'''
#Auxiliary Function to update the map
def switch_place(line_as_list, new_pos, pos):
    save_this = line_as_list[new_pos]
    line_as_list[new_pos] = '@'
    line_as_list[pos] = save_this

'''
    Description:        The eat auxiliary function is to acquire the keys, chips, or immunity items
                        and replaces it's place with a passable tile
    Arguments:
        line_as_list    Makes the Map string as a list, it used to get the value of the index of the 
                        positions of the player and the surounding tiles
        remove_index    The index of the variable to be remove such as keys,
                        chips or immunity items, it is then replaced with a passable tile
        pos             The index of the location of the player ('@')
                        and replaces with the index of new location

    Returns:
      None
'''
#Auxiliary Function to acquire the Keys and Chips
def eat(line_as_list, remove_index, pos):
    line_as_list[pos] = line_as_list[remove_index]
    line_as_list[remove_index] = ' '
    line_as_list[pos] = line_as_list[remove_index]

'''
    Description:        The keep auxiliary function is to put back the symbols 'W','F','<','>'
                        after the player have passed through it
    Arguments:
        line_as_list    Makes the Map string as a list, it used to get the value of the index of the 
                        positions of the player and the surounding tiles
        stay_index      The index of the variable to be stay which are the element
                        tiles and the slide tiles
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        symbol          The symbols 'W','F','<','>' that will be placed back

    Returns:
      None
'''
#Auxiliary Function to keep the symbols (W, F, <, >)
def keep(line_as_list, stay_index, pos, symbol):
    line_as_list[stay_index] = symbol
    line_as_list[pos] = line_as_list[stay_index]

'''
    Description:        The passable_tile function let the player walks throughout the
                        Map and also check if the next tile needs some variables before
                        passing through
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        water_count     The variable that keeps the 'W' when the value is 1 and sets it back to 0
        fire_count      The variable that keeps the 'F' when the value is 1 and sets it back to 0
        W_symbol        (used to define the auxiliary function)The water element tile to passed by if water immunity element
                        is acquired
        F_symbol        (used to define the auxiliary function)The fire element tile to passed by if fire immunity element
                        is acquired

    Returns:
        water_count     Return type is integer and return value is 0 to reset the water_count in the next move
        fire_count      Return type is integer and return value is 0 to reset the fire_count in the next move
                        that the next tile is not fire element tile anymore
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for ' ' passable tile
def passable_tile(direction_index, back_direction, line_as_list, pos, water_count, fire_count, W_symbol, F_symbol):
    new_pos = direction_index
    switch_place(line_as_list, new_pos, pos)
    if water_count >= 1:
        stay_index = back_direction
        keep(line_as_list, stay_index, pos, W_symbol)
        water_count = 0
    if fire_count >= 1:
        stay_index = back_direction
        keep(line_as_list, stay_index, pos, F_symbol)
        fire_count = 0
    Map = line_as_list
    return water_count, fire_count, Map

'''
    Description:        The impassable_tile function is the wall '|', it prevents the
                        player from passing throughout, which maintains the players position
    Arguments:
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location

    Returns:
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for '|' impassable tile
def impassable_tile(line_as_list, pos):
    new_pos = pos
    switch_place(line_as_list, new_pos, pos)
    Map = line_as_list
    return Map

'''
    Description:        The the_chips function adds a value to the number of chips
                        acquired by the player and remove it in the Map
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        chips           The number of chips ('*') acquired by the player incremented for ever eaten chips

    Returns:
        chips           Return type is an integer, it will add a number every time
                        a chip is acquired and will be used to exit and proceeding to
                        next Map.
        Map             Return type is a string, it will update the map with new
                        position of the player and removed chip
'''
#Function for "*" Chips
def the_chips(direction_index, back_direction, line_as_list, pos, chips):
    new_pos = direction_index
    chips += 1
    switch_place(line_as_list, new_pos, pos)
    remove_index = back_direction
    eat(line_as_list, remove_index, pos)
    Map = line_as_list
    return chips, Map

'''
    Description:        The keys function adds the keys ['g','y','b'] in the inventory
                        list acquired by the player and removes it in the Map
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        inventory       The list of which the keys will be stored by the player

    Returns:
        inventory       Return type is a string, it will add the keys acquired
                        and will be used to unlock the doors
        Map             Return type is a string, it will update the map with new
                        position of the player and removed door
'''
#Function for ['g','y','b'] keys
def keys(direction_index, back_direction, direction, line_as_list, pos, inventory):
    if direction == 'g':
        inventory.append('g')
    elif direction == 'y':
        inventory.append('y')
    elif direction == 'b':
        inventory.append('b')
    new_pos = direction_index
    switch_place(line_as_list, new_pos, pos)
    remove_index = back_direction
    eat(line_as_list, remove_index, pos)
    Map = line_as_list
    return inventory, Map

'''
    Description:        The door function let the player walk through the door 'G','Y','B'
                        if they acquired the proper key to open those if they don't have
                        those in the inventory they can't walk through it.
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        inventory       The list of which the keys will be stored by the player
        key             The proper key to open the specific door (i.e. 'y' key for 'Y' door)

    Returns:
        Map             Return type is a string, it will update the map with new
                        position of the player and removed chip
'''
#Function for ('G' or 'Y' or 'B') door
def door(direction_index, back_direction, line_as_list, pos, inventory, key):
    if key in inventory:
        inventory.remove(key)
        new_pos = direction_index
        switch_place(line_as_list, new_pos, pos)
        remove_index = back_direction
        eat(line_as_list, remove_index, pos)
    Map = line_as_list
    return Map

'''
    Description:        The the_immunity function gives immunity of fire or water
                        that was acquired by the player and removes it in the Map
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        power           The specific immunity either water or fire will be stored in
                        the immunty variable

    Returns:
        immunity        Return type is a string, it will change the immunity status
                        of the player, and will be used to walk on element tile
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#function for 'w' and 'f' (water & fire) immunity
def the_immunity(direction_index, back_direction, line_as_list, pos, power):
    new_pos = direction_index
    switch_place(line_as_list, new_pos, pos)
    immunity = power
    remove_index = back_direction
    eat(line_as_list, remove_index, pos)
    Map = line_as_list
    return immunity, Map


'''
    Description:        The element1 function is the Water & Fire element that the player should
                        not step into without the proper immunity or else the player will die
                        note:(the functionality of game over is in the "game" funtion)
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        immunity        The specific immunity, in this case "water"
        water_count     The variable that will determine if the symbol W will be removed or
                        stay after the player has passed through it
        W_symbol        The water element tile to passed by if water immunity element
                        is acquired, it's the one being removed and beeing keep

    Returns:
        water_count     Return type is integer and return value is >= 1, it is used in decision
                        making for telling whether to removed W or to keep it,
                        if water_count = 1 ... remove if water_count > 1 ... keep it
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for 'W' water element
def element1(direction_index, back_direction, line_as_list, pos, immunity, water_count, W_symbol):
    if immunity == 'water':
        new_pos = direction_index
        switch_place(line_as_list, new_pos, pos)
        water_count += 1
        if water_count == 1:
            remove_index = back_direction
            eat(line_as_list, remove_index, pos)
        else:
            stay_index = back_direction
            keep(line_as_list, stay_index, pos, W_symbol)
        Map = line_as_list
        return water_count, Map

'''
    Description:        The element2 function is the Fire element that the player should
                        not step into without the proper immunity or else the player will die
                        note:(the functionality of game over is in the "game" funtion)
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        immunity        The specific immunity, in this case "fire"
        fire_count      The variable that will determine if the symbol F will be removed or
                        stay after the player has passed through it
        F_symbol        The fire element tile to passed by if fire immunity element
                        is acquired, it's the one being removed and beeing keep

    Returns:
        fire_count      Return type is integer and return value is >= 1, it is used in decision
                        making for telling whether to removed F or to keep it,
                        if fire_count = 1 ... remove if fire_count > 1 ... keep it
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for 'F' fire element
def element2(direction_index, back_direction, line_as_list, pos, immunity, fire_count, F_symbol):
    if immunity == 'fire':
        new_pos = direction_index
        switch_place(line_as_list, new_pos, pos)
        fire_count += 1
        if fire_count == 1:
            remove_index = back_direction
            eat(line_as_list, remove_index, pos)
        else:
            stay_index = back_direction
            keep(line_as_list, stay_index, pos, F_symbol)
        Map = line_as_list
        return fire_count, Map

'''
    Description:        The slide_left function involuntarily moves the player to the
                        left when the direction of the move of the player is either
                        left or right. At the last arrow, the player will detec if it is a passable tile
                        if it is, it will move again one last time.
    Arguments:
        left            The index of the new location of the player or their move
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        arrow_count     The variable that will determine if the symbol ('<') will be removed or
                        stay after the player has passed through it and after the player moves
                        in the passable tile, it is set to zero.
        A1_symbol       The A1_symbol ('<') that will be placed back to the past location
                        of the player as the player moves automatically

    Returns:
        arrow_count     Return type is integer and return value is  arrow_count >= 1, it is
                        used in decision making for telling whether to removed > or to keep it,
                        if arrow_count = 1 ... remove if arrow_count > 1 ... keep it
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for '<' slide left
def slide_left(left, line_as_list, pos, arrow_count, A1_symbol):
    while left == '<':
        new_pos = pos - 1
        switch_place(line_as_list, new_pos, pos)
        arrow_count += 1
        if arrow_count == 1:
            remove_index = new_pos + 1
            eat(line_as_list, remove_index, pos)
        else:
            stay_index = new_pos + 1
            keep(line_as_list, stay_index, pos, A1_symbol)
        Map = line_as_list
        pos = Map.index('@')
        left = Map[pos - 1]
    if left == ' ':
        new_pos = pos - 1
        switch_place(line_as_list, new_pos, pos)
        arrow_count = 0
        stay_index = new_pos + 1
        keep(line_as_list, stay_index, pos, A1_symbol)
        Map = line_as_list
    return arrow_count, Map

'''
    Description:        The slide_right function involuntarily moves the player to the
                        right when the direction of the move of the player is either
                        left or right. At the last arrow, the player will detec if it is a passable tile
                        if it is, it will move again one last time.
    Arguments:
        right           The index of the new location of the player or their move
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        arrow_count     The variable that will determine if the symbol ('>') will be removed or
                        stay after the player has passed through it and after the player moves
                        in the passable tile, it is set to zero
        A2_symbol       The A2_symbol ('>') that will be placed back to the past location
                        of the player as the player moves automatically

    Returns:
        arrow_count     Return type is integer and return value is  arrow_count >= 1, it is
                        used in decision making for telling whether to removed > or to keep it,
                        if arrow_count = 1 ... remove if arrow_count > 1 ... keep it
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for '>' slide right
def slide_right(right, line_as_list, pos, arrow_count, A2_symbol):
    while right == '>':
        new_pos = pos + 1
        switch_place(line_as_list, new_pos, pos)
        arrow_count += 1
        if arrow_count == 1:
            remove_index = new_pos - 1
            eat(line_as_list, remove_index, pos)
        else:
            stay_index = new_pos - 1
            keep(line_as_list, stay_index, pos, A2_symbol)
        Map = line_as_list
        pos = Map.index('@')
        right = Map[pos + 1]
    if right == ' ':
        new_pos = pos + 1
        switch_place(line_as_list, new_pos, pos)
        arrow_count = 0
        stay_index = new_pos - 1
        keep(line_as_list, stay_index, pos, A2_symbol)
        Map = line_as_list
    return arrow_count, Map

'''
    Description:        The slide_left_updown function involuntarily moves the player to the
                        left when the direction of the move of the player is either
                        up or down (The slide_left function is used)
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        arrow_count     The variable that will determine if the symbol ('<') will be removed or
                        stay after the player has passed through it and after the player moves
                        in the passable tile, it is set to zero
        A1_symbol       The A1_symbol ('<') that will be placed back to the past location
                        of the player as the player moves automatically

    Returns:
        arrow_count     Return type is integer and return value is  arrow_count >= 1, it is
                        used in decision making for telling whether to removed > or to keep it,
                        if arrow_count = 1 ... remove if arrow_count > 1 ... keep it
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for slide left from up & down direction
def slide_left_updown(direction_index, back_direction, line_as_list, pos, arrow_count, A1_symbol):
    new_pos = direction_index
    switch_place(line_as_list, new_pos, pos)
    arrow_count += 1
    if arrow_count == 1:
        remove_index = back_direction
        eat(line_as_list, remove_index, pos)
    Map = line_as_list
    pos = Map.index('@')
    left = Map[pos - 1]
    slide_left(left, line_as_list, pos, arrow_count, A1_symbol)
    arrow_count = 0
    Map = line_as_list
    return arrow_count, Map

'''
    Description:        The slide_right_updown function involuntarily moves the player to the
                        left when the direction of the move of the player is either
                        up or down (The slide_right function is used)
    Arguments:
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        arrow_count     The variable that will determine if the symbol ('>') will be removed or
                        stay after the player has passed through it and after the player moves
                        in the passable tile, it is set to zero
        A2_symbol       The A2_symbol ('>') that will be placed back to the past location
                        of the player as the player moves automatically

    Returns:
        arrow_count     Return type is integer and return value is  arrow_count >= 1, it is
                        used in decision making for telling whether to removed > or to keep it,
                        if arrow_count = 1 ... remove if arrow_count > 1 ... keep it
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for slide right from up & down direction
def slide_right_updown(direction_index, back_direction, line_as_list, pos, arrow_count, A2_symbol):
    new_pos = direction_index
    switch_place(line_as_list, new_pos, pos)
    arrow_count += 1
    if arrow_count == 1:
        remove_index = back_direction
        eat(line_as_list, remove_index, pos)
    Map = line_as_list
    pos = Map.index('@')
    right = Map[pos + 1]
    slide_right(right, line_as_list, pos, arrow_count, A2_symbol)
    arrow_count = 0
    Map = line_as_list
    return arrow_count, Map

'''
    Description:        The thief function restart the game to the specific map. All items
                        will be discarded and the player starts again in Starting Tile
    Arguments:
        chips           The number of chips ('*') acquired by the player
        inventory       The list of which the keys will be stored by the player
        immunity        The specific immunity that the player acquired such as water ('w')
                        or fire ('f')
        level           The level of the game which tells the Map to be used

    Returns:
        chips           Return type is an integer, return value is 0, it will restart the
                        number of chips
        inventory       Return type is a string, it will remove all the keys in the inventory
        immunity        Return type is a string, return value is None, it will remove the
                        acquired immunity item of the player
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for '$' thief tile
def thief(chips, inventory, immunity, level):
    chips = 0
    inventory = []
    immunity = 'None'
    if level == 1:
        Map_number = 'Map1.txt'
        Map = read_file(Map_number)
    if level == 2:
        Map_number = 'Map2.txt'
        Map = read_file(Map_number)
    if level == 3:
        Map_number = 'Map3.txt'
        Map = read_file(Map_number)
    return chips, inventory, immunity, Map

'''
    Description:        The exit_door function is the door need to pass through in order to proceed
                        to the next level, all the chips should be collected in order to unlock it
    Arguments:
        level           The level of the game used for conditional statement to based on the map
        direction_index The index of the new location of the player or their move
        back_direction  The index of the past location of the player
        line_as_list    Used only to defne the auxiliary function and Makes the Map string as a list
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location
        chips           The number of chips ('*') acquired by the player if it matched
                        the chips_collect

    Returns:
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for '#' exit door
def exit_door(level,direction_index,back_direction,line_as_list,pos,chips):
    if level == 1:
        chips_collect = 9
        if chips == chips_collect:
            new_pos = direction_index
            switch_place(line_as_list, new_pos, pos)
            remove_index = back_direction
            eat(line_as_list, remove_index, pos)
    if level == 2:
        chips_collect = 10
        if chips == chips_collect:
            new_pos = direction_index
            switch_place(line_as_list, new_pos, pos)
            remove_index = back_direction
            eat(line_as_list, remove_index, pos)
    if level == 3:
        chips_collect = 11
        if chips == chips_collect:
            new_pos = direction_index
            switch_place(line_as_list, new_pos, pos)
            remove_index = back_direction
            eat(line_as_list, remove_index, pos)
    Map = line_as_list
    return Map

'''
    Description:        The done function proceeds the game to the next level and to
                        the next map, it uses the read_file function to load the map
    Arguments:
        chips           The number of chips ('*') acquired by the player
        inventory       The list of which the keys will be stored by the player
        immunity        The specific immunity that the player acquired such as water ('w')
                        or fire ('f')
        level           The level of the game which tells the Map to be used

    Returns:
        chips           Return type is an integer, return value is 0, it will restart the
                        number of chips
        inventory       Return type is a string, it will remove all the keys in the inventory
        immunity        Return type is a string, return value is None, it will remove the
                        acquired immunity item of the player
        level           Return type is an integer, return value is level + 1, it will proceed
                        the level to the next map
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for 'E' done proceed to new map
def done(chips, inventory, immunity, level):
    chips = 0
    inventory = []
    immunity = 'None'
    if level == 1:
        Map_number = 'Map2.txt'
        Map = read_file(Map_number)
        level += 1
        return chips, inventory, immunity, level, Map
    elif level == 2:
        Map_number = 'Map3.txt'
        Map = read_file(Map_number)
        level += 1
        return chips, inventory, immunity, level, Map

'''
    Description:        The position function is the move of the player across the entire map
                        it assign the move w,a,s,d to a specific variable that will be utilized 
                        in the "game" function
    Arguments:
        Map             The Map of the game that is a list, that will be used for the entire program
        pos             The index of former location of the player ('@')
                        and replaces with the index of new location

    Returns:
        move            Return type is a string that is w,a,s,d that tells which direction
                        the player wants to go
        line_as_list    Return type is a list, it updates the list based on the player's move
        direction       Return type is a string which tells the value of index surrounding
                        the player's position
        direction_index Return type is an integer, it is the index around the player
        back_direction  Return type is an integer it is the index at the previous postion of the player
        Map             Return type is a string, it will update the map with new
                        position of the player
'''
#Function for move of player
def position(Map,pos):

    left_index = pos - 1
    right_index = pos + 1
    up_index = pos - 41
    down_index = pos + 41

    left = Map[left_index]
    right = Map[right_index]
    up = Map[up_index]
    down = Map[down_index]

    back_left = left_index + 1
    back_right = right_index - 1
    back_up = up_index + 41
    back_down = down_index - 41

    move = input('Choose move, w,a,s,d: ').lower()

    if move == 'a':
        line_as_list = list(Map)
        direction = left
        direction_index = left_index
        back_direction = back_left

    elif move == 'd':
        line_as_list = list(Map)
        direction = right
        direction_index = right_index
        back_direction = back_right

    elif move == 'w':
        line_as_list = list(Map)
        direction = up
        direction_index = up_index
        back_direction = back_up

    elif move == 's':
        line_as_list = list(Map)
        direction = down
        direction_index = down_index
        back_direction = back_down

    else:
        line_as_list = list(Map)
        print('Invalid \n')
        direction = Map[pos]
        direction_index = pos
        back_direction = pos

    return move,line_as_list,direction,direction_index,back_direction

'''
    Description:        The game function is the game proper in where the game starts,
                        proceeds, and ends. It is where the other functions combine
                        together and used depend on the tile that will walk through
                        by the player

    Arguments:
        Map             The string to be printed and used as Map throughout the game
        level           The level to be checked and to know what Map to be used
        End             The string to be printed when the game finished after completing
                        the last level or Map
        Over            The string to be printed when the game is over or the player lose

    Returns:
        None
'''
#Function for the game proper
def game(Map, level, End, Over):

    print(Map)
    chips = 0
    inventory = []
    immunity = 'None'

    water_count = 0
    fire_count = 0
    arrow_count = 0

    green_key = 'g'
    yellow_key = 'y'
    blue_key = 'b'

    water = 'water'
    fire = 'fire'

    W_symbol = 'W'
    F_symbol = 'F'
    A1_symbol = '<'
    A2_symbol = '>'

    while True:

        if level == 1:
                print("\nTotal no. of Chips to collect is 9\n" )
        elif level == 2:
                print("\nTotal no. of Chips to collect is 10\n")
        elif level == 3:
                print("\nTotal no. of Chips to collect is 11\n")

        print("Chips: %s" %(chips))
        print("Inventory: %s" %(inventory))
        print("Immunity: %s" %(immunity))

        pos = Map.index('@')

        move,line_as_list,direction,direction_index,back_direction = position(Map,pos)

        if direction == ' ':
            water_count, fire_count, Map = passable_tile(direction_index, back_direction, line_as_list, pos, water_count, fire_count, W_symbol, F_symbol)

        elif direction == '|':
             Map = impassable_tile(line_as_list, pos)

        elif direction == '*':
            chips, Map = the_chips(direction_index, back_direction, line_as_list, pos, chips)

        elif direction in ['g','y','b']:
            inventory, Map = keys(direction_index, back_direction, direction, line_as_list, pos, inventory)

        elif direction == 'G':
            Map = door(direction_index, back_direction, line_as_list, pos, inventory, green_key)
        elif direction == 'Y':
            Map = door(direction_index, back_direction, line_as_list, pos, inventory, yellow_key)
        elif direction == 'B':
            Map = door(direction_index, back_direction, line_as_list, pos, inventory, blue_key)

        elif direction == 'w':
            immunity, Map = the_immunity(direction_index, back_direction, line_as_list, pos, water)
        elif direction == 'f':
            immunity, Map = the_immunity(direction_index, back_direction, line_as_list, pos, fire)

        elif direction == 'W':
            if immunity == water:
                water_count, Map = element1(direction_index, back_direction, line_as_list, pos, immunity, water_count, W_symbol)
                Map = Map
            else:
                print(Over)
                return False
        elif direction == 'F':
            if immunity == fire:
                fire_count, Map = element2(direction_index, back_direction, line_as_list, pos, immunity, fire_count, F_symbol)
                Map = Map
            else:
                print(Over)
                return False

        elif direction == '$':
            chips, inventory, immunity, Map = thief(chips, inventory, immunity, level)

        elif direction == '<':
            if move == 'a':
                arrow_count, Map = slide_left(direction, line_as_list, pos, arrow_count, A1_symbol)
            elif move == 'w':
                arrow_count, Map = slide_left_updown(direction_index, back_direction, line_as_list, pos, arrow_count, A1_symbol)
            elif move == 's':
                arrow_count, Map = slide_left_updown(direction_index, back_direction, line_as_list, pos, arrow_count, A1_symbol)

        elif direction == '>':
            if move == 'd':
                arrow_count, Map = slide_right(direction, line_as_list, pos, arrow_count, A2_symbol)
            elif move == 'w':
                arrow_count, Map = slide_right_updown(direction_index, back_direction, line_as_list, pos, arrow_count, A2_symbol)
            elif move == 's':
                arrow_count, Map = slide_right_updown(direction_index, back_direction, line_as_list, pos, arrow_count, A2_symbol)

        elif direction == '#':
            Map = exit_door(level,direction_index,back_direction,line_as_list,pos,chips)

        elif direction == 'E':
            if level in [1,2]:
                chips, inventory, immunity, level, Map = done(chips, inventory, immunity, level)
            elif level == 3:
                print(End)
                return False

        print("".join(Map))

'''
    Description:        The main function is the one responsible for setting up the game,
                        such as the introduction, map 1, level 1, the imports
                        and the game function
    Arguments:
        None

    Returns:
        None
'''
#Main Function
def main():

    print('\n       Welcome to Chips Challenge!\n')
    Map_number = 'Map1.txt'
    Map = read_file(Map_number)
    End = End_Art.Finish
    Over = End_Art.Sad
    level = 1
    game(Map, level, End, Over)

#Run
if __name__ == "__main__":

    main()
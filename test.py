import End_Art

#read file
def read_file(Map_number):
    text_file = open("%s"%(Map_number), "r")
    data = text_file.read()
    text_file.close()
    return data

#Auxiliary Function to update the map
def switch_place(line_as_list, new_pos, pos):
    save_this = line_as_list[new_pos]
    line_as_list[new_pos] = '@'
    line_as_list[pos] = save_this

#Auxiliary Function to acquire the Keys and Chips
def eat(line_as_list, remove_index, pos):
    line_as_list[pos] = line_as_list[remove_index]
    line_as_list[remove_index] = ' '
    line_as_list[pos] = line_as_list[remove_index]

#Auxiliary Function to keep the symbols (W, F, <, >)
def keep(line_as_list, stay_index, pos, symbol):
    line_as_list[stay_index] = symbol
    line_as_list[pos] = line_as_list[stay_index]

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

#Function for '|' impassable tile
def impassable_tile(line_as_list, pos):
    new_pos = pos
    switch_place(line_as_list, new_pos, pos)
    Map = line_as_list
    return Map

#Function for "*" Chips
def the_chips(direction_index, back_direction, line_as_list, pos, chips):
    new_pos = direction_index
    chips += 1
    switch_place(line_as_list, new_pos, pos)
    remove_index = back_direction
    eat(line_as_list, remove_index, pos)
    Map = line_as_list
    return chips, Map

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

#function for 'w' and 'f' (water & fire) immunity
def the_immunity(direction_index, back_direction, line_as_list, pos, power):
    new_pos = direction_index
    switch_place(line_as_list, new_pos, pos)
    immunity = power
    remove_index = back_direction
    eat(line_as_list, remove_index, pos)
    Map = line_as_list
    return immunity, Map

#Function for 'W' and 'F' (water & Fire) element
def element(direction_index, back_direction, line_as_list, pos, immunity, power, e_count, symbol):
    if immunity == power:
        new_pos = direction_index
        switch_place(line_as_list, new_pos, pos)
        e_count += 1
        if e_count == 1:
            remove_index = back_direction
            eat(line_as_list, remove_index, pos)
        else:
            stay_index = back_direction
            keep(line_as_list, stay_index, pos, symbol)
        Map = line_as_list
        return e_count, Map

#Function for '<' and '>' slide
def slide_leftright(direction_index, back_direction, direction, symbol, line_as_list, pos, arrow_count):
    while direction == symbol:
        new_pos = direction_index
        switch_place(line_as_list, new_pos, pos)
        arrow_count += 1
        if arrow_count == 1:
            remove_index = back_direction
            eat(line_as_list, remove_index, pos)
        else:
            stay_index = new_pos + 1
            keep(line_as_list, stay_index, pos, symbol)
        Map = line_as_list
        pos = Map.index('@')
        direction = Map[direction_index]
    if direction == ' ':
        new_pos = pos - 1
        switch_place(line_as_list, new_pos, pos)
        arrow_count = 0
        stay_index = back_direction
        keep(line_as_list, stay_index, pos, symbol)
        Map = line_as_list
    return arrow_count, Map

#Function for slide left and right from up & down direction
def slide_updown(direction_index, back_direction, direction, symbol, line_as_list, pos, arrow_count):
    new_pos = direction_index
    switch_place(line_as_list, new_pos, pos)
    arrow_count += 1
    if arrow_count == 1:
        remove_index = back_direction
        eat(line_as_list, remove_index, pos)
    Map = line_as_list
    pos = Map.index('@')
    direction = Map[direction_index]
    slide_leftright(direction_index, back_direction, direction, symbol, line_as_list, pos, arrow_count)
    arrow_count = 0
    Map = line_as_list
    return arrow_count, Map

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

#Function for '#' exit door
def exit_door(Map,level,direction_index,back_direction,line_as_list,pos,chips):
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

    move = input('Choose move, w,a,s,d: ')

    if move == 'a':
        line_as_list = list(Map)
        direction = left
        direction_index = left_index
        back_opposite = back_right
        back_direction = back_left

    elif move == 'd':
        line_as_list = list(Map)
        direction = right
        direction_index = right_index
        back_opposite = back_left
        back_direction = back_right

    elif move == 'w':
        line_as_list = list(Map)
        direction = up
        direction_index = up_index
        back_opposite = back_down
        back_direction = back_up

    elif move == 's':
        line_as_list = list(Map)
        direction = down
        direction_index = down_index
        back_opposite = back_up
        back_direction = back_down

    else:
        line_as_list = list(Map)
        print('invalid')
        direction = Map[pos]
        direction_index = pos
        back_opposite = pos
        back_direction = pos

    return move,line_as_list,direction,direction_index,back_opposite,back_direction

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

        move,line_as_list,direction,direction_index,back_opposite,back_direction = position(Map,pos)

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
                e_count, Map = element(direction_index, back_direction, line_as_list, pos, immunity, water, water_count, W_symbol)
                Map = Map
            else:
                print(Over)
                return False
        elif direction == 'F':
            if immunity == fire:
                e_count, Map = element(direction_index, back_direction, line_as_list, pos, immunity, fire, fire_count, F_symbol)
                Map = Map
            else:
                print(Over)
                return False

        elif direction == '$':
            chips, inventory, immunity, Map = thief(chips, inventory, immunity, level)

        elif direction == '<':
            if move == 'a':
                arrow_count, Map = slide_leftright(direction_index, back_direction, direction, A1_symbol, line_as_list, pos, arrow_count)
            elif move == 'w':
                arrow_count, Map = slide_updown(direction_index, back_direction, direction, A1_symbol, line_as_list, pos, arrow_count)
            elif move == 's':
                arrow_count, Map = slide_updown(direction_index, back_direction, direction, A1_symbol, line_as_list, pos, arrow_count)

        elif direction == '>':
            if move == 'd':
                arrow_count, Map = slide_leftright(direction_index, back_direction, direction, A2_symbol, line_as_list, pos, arrow_count)
            elif move == 'w':
                arrow_count, Map = slide_updown(direction_index, back_direction, direction, A2_symbol, line_as_list, pos, arrow_count)
            elif move == 's':
                arrow_count, Map = slide_updown(direction_index, back_direction, direction, A2_symbol, line_as_list, pos, arrow_count)

        elif direction == '#':
            Map = exit_door(Map,level,direction_index,back_direction,line_as_list,pos,chips)

        elif direction == 'E':
            if level in [1,2]:
                chips, inventory, immunity, level, Map = done(chips, inventory, immunity, level)
            elif level == 3:
                print(End)
                return False

        print("".join(Map))

#Main Function
def main():

    print('Welcome to Chips Challenge!')
    Map_number = 'Map1.txt'
    Map = read_file(Map_number)
    End = End_Art.Finish
    Over = End_Art.Sad
    level = 1
    game(Map, level, End, Over)

#Run
if __name__ == "__main__":

    main()
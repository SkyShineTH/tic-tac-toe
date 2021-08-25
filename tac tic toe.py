Table = ['1','2','3',
         '4','5','6',
         '7','8','9']

def table_game():
    print(Table[0]+' | ' + Table[1]+' | ' + Table[2])
    print("---------")
    print(Table[3] + ' | ' + Table[4] + ' | ' + Table[5])
    print("---------")
    print(Table[6] + ' | ' + Table[7] + ' | ' + Table[8])
    print("---------")


def user_insert(player):
    print("if you want quit the game input 'q'")
    in_pos = input(f"Insert position you want {'Player(1)' if player == True else 'Player(2)'}:")
    if in_pos == 'q':
        exit("You quit the game!")
    pos = int(in_pos)
    if pos in range(0,10):
        pos -= 1
        for i in range(3):
            if i == 3:
                print("You have selected 3 times.")
                break
            elif player == True and Table[pos] != 'X' and Table[pos] != 'O':
                Table[pos] = 'X'
                break
            elif player == False and Table[pos] != 'X' and Table[pos] != 'O':
                Table[pos] = 'O'
                break
            else:
                print(f"You have selected {i} times.")
    else:
        print("You insert over number or special characters!!!")

def checkwin(player, table):
    if Table[0] == Table[1] == Table[2]: return True
    elif Table[3] == Table[4] == Table[5]: return True
    elif Table[6] == Table[7] == Table[8]: return True
    elif Table[0] == Table[3] == Table[6]: return True
    elif Table[1] == Table[4] == Table[7]: return True
    elif Table[2] == Table[5] == Table[8]: return True
    elif Table[0] == Table[4] == Table[8]: return True
    elif Table[2] == Table[4] == Table[6]: return True
    else:
        return False

def check_fulltable(table):
    for element in table:
        if isinstance(element, int) or element.isdigit():
            return False
    return True

def game():
    players = True
    while True:
        table_game()
        if checkwin(players, Table):
            print(f"Winner is {'Player1 (X)' if players == False else 'Player2 (O)'}!!!")
            break
        if check_fulltable(Table):
            print("Draw")
            break
        user_insert(players)
        if players == True:
            players = False
        else:
            players = True

game()
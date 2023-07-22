"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Procházka
email: jan.prochazka92@gmail.com
discord: .honzikovacesta
"""

#FUNCTION- checking if player won
def check_winning_combination(winning_positions, selected_positions, grid_size):
    for positions in winning_positions:
        is_inside = 0
        for position in positions:
            if position in selected_positions:
                is_inside += 1
                if is_inside == grid_size:
                    return True
    return False

#FUNCTION- print gaming grid
def print_gaming_grid(gaming_grid):
    grid_size = len(gaming_grid)
    grid_line = "+---" * grid_size + "+"

    print(grid_line)
    for row in gaming_grid:
        print("|" + "|".join(f"{char:^3}" for char in row) + "|")
        print(grid_line)


#gaming grid of chosen size
grid_size = 3 # 3 --> 3x3, 4 --> 4x4, 5 -->5x5 etc
gaming_grid = []
i = 0
for n in range(grid_size):
    gaming_grid.append([j+i for j in range(grid_size)])
    i += grid_size

#define list of winning positions for checking if one or another player has won    
winning_positions = []
#rows and columns
for i in range(grid_size): 
    winning_positions.append(list(gaming_grid[i]))  #create a copy of the row so it wont be changed with gaming_grid list
    winning_positions.append([gaming_grid[j][i] for j in range(grid_size)])
#diagonals
winning_positions.append([gaming_grid[i][i] for i in range(grid_size)]) 
winning_positions.append([gaming_grid[i][grid_size - 1 - i] for i in range(grid_size)])

#welcome player and print game info
line = '========================================'
game_info = f'''   
GAME RULES:
Each player can place one mark (or stone)
per turn on the {grid_size}x{grid_size} grid. The WINNER is
who succeeds in placing {grid_size} of their
marks in a:
            * horizontal,
            * vertical or
            * diagonal row
'''
print('Welcome to Tic Tac Toe!'.center(len(line)))
print(line)
print(game_info)
print(line)
print("Press Enter to start the game...")
input()

#printing gaming grid using function
print_gaming_grid_use = print_gaming_grid(gaming_grid)

#empty lists and variables
placed_x = []
placed_o = []
blocked_positions = []
grid_len = grid_size**2
max_index = grid_len - 1

while True:

    #PLAYER - x -
    while True:
        #player input and handling exceptions
        try:
            mark_x = int(input('Player X turn, choose position with number: '))
            if mark_x in blocked_positions:
                print('blocked position, try again')
            elif mark_x < 0:
                print('negative value, try again')
            elif mark_x > max_index:
                print('number out of interval, try again')
            else:
                blocked_positions.append(mark_x)
                placed_x.append(mark_x)
                for row in gaming_grid:
                    if mark_x in row:
                        index = row.index(mark_x)
                        row[index] = 'x'
                break
        except ValueError:
            print('wrong value, try again')  
    
    #print updated grid
    print_gaming_grid_use = print_gaming_grid(gaming_grid)

    #checks if player have winning combination
    is_winning_combination = check_winning_combination(winning_positions, placed_x, grid_size)
    
    #checks if there is a winner
    if is_winning_combination:
        print('X is the winner!')
        break

    #checks if draw
    if len(blocked_positions) == grid_len:
        print('Draw!')
        break

    #print(f'pos blocked {blocked_positions}')
    #print(f'blocked by player x {placed_x}')
    #print(f'winning pos {winning_positions}')

    #PLAYER - o -
    while True:
        #player input and handling exceptions   
        try:
            mark_o = int(input('Player O turn, choose position with number: '))
            if mark_o in blocked_positions:
                print('blocked position, try again')
            elif mark_o < 0:
                print('negative value, try again')
            elif mark_o > max_index:
                print('number out of interval, try again')
            else:
                blocked_positions.append(mark_o)
                placed_o.append(mark_o)
                for row in gaming_grid:
                    if mark_o in row:
                        index = row.index(mark_o)
                        row[index] = 'o'
                break
        except ValueError:
            print('wrong value, try again')

    #print updated grid
    print_gaming_grid_use = print_gaming_grid(gaming_grid)

    #checks if player have winning combination
    is_winning_combination = check_winning_combination(winning_positions, placed_o, grid_size)

    #checks if there is a winner
    if is_winning_combination:
        print('O is the winner!')
        break

    #checks if draw
    if len(blocked_positions) == grid_len:
        print('Draw!')
        break
    
    #print(f'pos blocked {blocked_positions}')
    #print(f'blocked by player o {placed_o}')
    #print(f'winning pos {winning_positions}')
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Procházka
email: jan.prochazka92@gmail.com
discord: .honzikovacesta
"""

#pozdrav uzivatele

#pravidla hry

#hrací plocha

#tah hrace 1, upozorní pokud táhn
#Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
#Pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní.
#Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené

line = '========================================'
print('Welcome to Tic Tac Toe!')
print(line)
print('''   
            GAME RULES:
            Each player can place one mark (or stone)
            per turn on the 3x3 grid. The WINNER is
            who succeeds in placing three of their
            marks in a:
            * horizontal,
            * vertical or
            * diagonal row      ''')
print(line)
print('Let\'s start the game')


position = [n for n in range(9)]
grid_line = '+---+---+---+'


#3x3 grid napsat ve for cyklu?
print(grid_line)
print(f'|{position[0]:^{3}}|{position[1]:^{3}}|{position[2]:^{3}}|')
print(grid_line)
print(f'|{position[3]:^{3}}|{position[4]:^{3}}|{position[5]:^{3}}|')
print(grid_line)
print(f'|{position[6]:^{3}}|{position[7]:^{3}}|{position[8]:^{3}}|')
print(grid_line)

vyherni_pozice = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
kontrola_x = []
kontrola_o = []
obsazena_pozice = []
n=True
while n:

    #HRAC - x -
    while True:   
        try:
            mark_x = int(input('Player X turn, choose position with number: '))
            if mark_x in obsazena_pozice:
                print('tato pozice je obsazena')
            else:
                obsazena_pozice.append(mark_x)
                kontrola_x.append(mark_x)
                position[mark_x] = 'x'
                break
        except ValueError:
            print('spatna hodnota')
        

    
    

    #grid
    print(grid_line)
    print(f'|{position[0]:^{3}}|{position[1]:^{3}}|{position[2]:^{3}}|')
    print(grid_line)
    print(f'|{position[3]:^{3}}|{position[4]:^{3}}|{position[5]:^{3}}|')
    print(grid_line)
    print(f'|{position[6]:^{3}}|{position[7]:^{3}}|{position[8]:^{3}}|')
    print(grid_line)
    
    #vyherni pozice = 0 1 2, 3 4 5, 6 7 8, 0 3 6, 1 4 7, 2 5 8, 0 4 8, 2 4 6
    if kontrola_x in vyherni_pozice:
        print('X is the winner!')
        n=False
    
    print(obsazena_pozice)
    print(kontrola_x)

    #HRAC - o -
    
    while True:   
        try:
            mark_o = int(input('Player O turn, choose position with number: '))
            if mark_o in obsazena_pozice:
                print('tato pozice je obsazena')
            else:
                obsazena_pozice.append(mark_o)
                kontrola_o.append(mark_o)
                position[mark_o] = 'o'
                break
        except ValueError:
            print('spatna hodnota')
    
    #grid
    print(grid_line)
    print(f'|{position[0]:^{3}}|{position[1]:^{3}}|{position[2]:^{3}}|')
    print(grid_line)
    print(f'|{position[3]:^{3}}|{position[4]:^{3}}|{position[5]:^{3}}|')
    print(grid_line)
    print(f'|{position[6]:^{3}}|{position[7]:^{3}}|{position[8]:^{3}}|')
    print(grid_line)
    
    #vyherni pozice = 0 1 2, 3 4 5, 6 7 8, 0 3 6, 1 4 7, 2 5 8, 0 4 8, 2 4 6   
    if kontrola_o in vyherni_pozice:
        print('O is the winner!')
        n=False
    
    print(obsazena_pozice)
    print(kontrola_o)
# var = 'Welcome to Code Nation'
# def is_even(string):
#     if len(string) %2 ==0:
#         print(f'{string} has length {len(string)} and is even')
#     else:
#         print(f'{string} has length {len(string)} and is not even')
# is_even('helloe')

# alph = [chr(x) for x in range(ord('a'),ord('z')+1) ]
# for x in alph:
#     print(x)

# i = int (input('number 1 to 26:'))
# print(alph[i-1])
import random

def start():
    global player,comp,available,a
    available = ['1','2','3','4','5','6','7','8','9']
    a = [f'\033[2;36m{i}\033[0;0m' for i in  range(10)]
    choice = input('X or O:').lower()
    player,comp = '',''
    board()
    if choice in ['x']:
        player = 'x'
        comp= 'o'
        play()
    if choice == 'o':
        player='o'
        comp ='x'
        comp_play()
    else:
        start()

def play():
    global available, a
    print('choose a sector')
    choice = input('>>').lower()
    if choice in available:
        available.remove(choice)
        a[int(choice)] = player
        board()
    else: 
        play()
    check_win(player)
    comp_play()

def comp_play():
    global available,a
    comp_move(comp)
    x = random.randint(0,len(available)-1)
    a[int(available[x])] = comp
    available.remove(available[x])
    board()
    check_win(comp)
    play()

def comp_move(comp):
    #move to win
    for j in range(3):
        if 2 == sum(a[i] == comp for i in [1+3*j,2+3*j,3+3*j]) and 0 == sum(a[i] == player for i in [1+3*j,2+3*j,3+3*j]):
            for i in [1+3*j,2+3*j,3+3*j]:
                a[i] = comp 
            board()
            check_win(comp)
    for j in range(3):        
        if 2 == sum(a[i] == comp for i in [1+j,4+j,7+j]) and 0 == sum(a[i] == player for i in [1+j,4+j,7+j]):
            for i in [1+j,4+j,7+j]:
                a[i] = comp 
            board()
            check_win(comp)
    if 2 == sum(a[i] == comp for i in [1,5,9]) and 0 == sum(a[i] == player for i in [1,5,9]):
            for i in [1,5,9]:
                a[i] = comp 
            board()
            check_win(comp)
    if 2 == sum(a[i] == comp for i in [3,5,7]) and 0 == sum(a[i] == player for i in [3,5,7]):
            for i in [3,5,7]:
                a[i] = comp 
            board()
            check_win(comp)
    
    #move to defend
    for j in range(3):
        if 2 == sum(a[i] == player for i in [1+3*j,2+3*j,3+3*j]) and 0 == sum(a[i] == comp for i in [1+3*j,2+3*j,3+3*j]):
            for i in [1+3*j,2+3*j,3+3*j]:
                if a[i] != player:
                        available.remove(str(a.index(a[i])))
                        a[i] = comp
                        board()
                        play()           
    for j in range(3):        
        if 2 == sum(a[i] == player for i in [1+j,4+j,7+j]) and 0 == sum(a[i] == comp for i in [1+j,4+j,7+j]):
            for i in [1+j,4+j,7+j]:
                if a[i] != player:
                        available.remove(str(a.index(a[i])))
                        a[i] = comp
                        board()
                        play()       
    if 2 == sum(a[i] == player for i in [3,5,7]) and 0 == sum(a[i] == comp for i in [3,5,7]):
            for i in [3,5,7]:
                if a[i] != player:
                        available.remove(str(a.index(a[i])))
                        a[i] = comp
                        board()
                        play()       
    if 2 == sum(a[i] == player for i in [1,5,9]) and 0 == sum(a[i] == comp for i in [1,5,9]):
            for i in [1,5,9]:
                if a[i] != player:
                        available.remove(str(a.index(a[i])))
                        a[i] = comp
                        board()
                        play()       
    
def check_win(p):
    global a
    for j in range(3):
        if a[1+3*j] == a[2+3*j]== a[3+3*j]==p:
            print(f'{p} wins')
            again()
    for j in range(3):
        if a[1+j] == a[4+j]== a[7+j]==p:
            print(f'{p} wins')
            again()
    if a[1] == a[5]== a[9]==p:
        print(f'{p} wins')
        again()
    elif a[3] == a[5]== a[7]==p:
        print(f'{p} wins')
        again()
    elif available == []:
        print("It's a draw")
        again()
    
def board():
    print('')
    print(f' {a[1]} | {a[2]} | {a[3]} ')
    print('-----------')
    print(f' {a[4]} | {a[5]} | {a[6]} ')
    print('-----------')
    print(f' {a[7]} | {a[8]} | {a[9]} ')

def again():
    choice = input('play again? y/n :').lower()
    if choice == 'y':
        start()
    elif choice == 'n':
        quit()
    else:
        again()

start()
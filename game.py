restart_check = True
og_game_board = ['1','2','3','4','5','6','7','8','9']

def display_game(game_board):
    print(f'     |     |     \n  {game_board[0]}  |  {game_board[1]}  |  {game_board[2]}  \n     |     |     \n-----------------\n     |     |     \n  {game_board[3]}  |  {game_board[4]}  |  {game_board[5]} \n     |     |     \n-----------------\n     |     |     \n  {game_board[6]}  |  {game_board[7]}  |  {game_board[8]} \n     |     |     \n')

def player_input():
    choice = 'WRONG'

    while choice not in game_board:
        choice = input('Please choose a cell to change: ')
        if choice not in game_board and og_game_board:
            print('Please choose one of the numbers on the grid.')
    
    return int(choice) - 1

def turn_check(turn):
    if turn == True:
        return False
    else:
        return True

def replacement_choice(game_board,index_change,turn):
    if turn == True:
        game_board[index_change] = 'X'
    else:
        game_board[index_change] = 'O'

    return game_board

def gameon_check(turn_counter):
    if turn_counter < 9:
        print(turn_counter)
        return True
    else: 
        return False

def restart_checking():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input('Play again? (Y or N) ')
        if choice not in ['Y','N']:
            print("Don't understand? Please choose 'Y' or 'N'")

    if choice == 'Y':
        return True
    else:
        return False



while restart_check == True:
    game_board = ['1','2','3','4','5','6','7','8','9']
    game_on = True
    turn_counter = 1
    turn = True
    
    display_game(og_game_board)

    while game_on:
        index_change = player_input()

        game_board = replacement_choice(game_board,index_change,turn)

        turn =  turn_check(turn)

        display_game(game_board)

        game_on = gameon_check(turn_counter)

        turn_counter += 1

    restart_check = restart_checking()

def start_game():
    #Confirm start
    input("Press Enter to continue...")

    #Initialization
    word = get_word()
    board = initialize(word)
    print(''.join(board))
    lives = 6
    guessed_letters = list("")

    while lives>0:
        #Begin guesses
        print("Guess a letter")
        guess = input()
        if guess in guessed_letters:
            print("You have already guessed this letter")
        else:
            guessed_letters += guess
            if word.find(guess) == -1:
                lives -= 1
                print('You have '+str(lives)+ ' lives remaining.')
            else: 
                board = check_letter(guess, word, board)
                                        
        print(''.join(board))
        print('Guessed letters: '+str(guessed_letters))
        if '_' not in board:
                    lives = 0
                    print('You won! Play again? (y/n)')
                    if input('') == 'y':
                        start_game()



def get_word():
    #get word from database using random number

    return "banana"

def initialize(word):
    board = list("")
    for element in word:
        board += '_ '
        
    return board

def check_letter(guess, word, board):
    locations = [pos for pos, char in enumerate(word) if char == guess]
    for location in locations:
        board[location*2] = guess

    return board
start_game()


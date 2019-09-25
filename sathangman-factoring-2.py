import json
import random

# Functions
def runHangman():
    def createDictionary(paths_list):
        new_dic = []
        for each in paths_list:
            path = each
            json1 = open (path)
            data = json.load(json1)
            new_dic = new_dic + data
        return new_dic

    def makeBoard(word):
        board_build = []
        for char in range(len(word)):
            board_build += "_"
        return board_build

    def showWinStreak():
        print("Winstreak: ", winstreak)

    def showBoard(board):
        print(" ".join(board))

    def showStrikes(strikes):
        print("Strikes: ", strikes)

    def showGuesses(guesses):
        print("Guesses: ", " ".join(guesses))

    def takeGuess(letters, guesses):
        while True:
            guess = input("Go ahead, guess a new letter: ")
            if guess in guesses:
                print ("You already guessed that one.")
            elif guess not in letters:
                print("Doesn't compute. Try lower-case letters or a hyphen.")
            else:
                guesses += guess
                return (guess, guesses)
                break

    def printGoodNews():
        print("Hey! You got one!")

    def printBadNews():
        print("Yikes. Not so much. +1 strike")

    def updateBoard(word_list, board,  guess):
        while guess in word_list:
            index1 = word_list.index(guess)
            board[index1] = guess
            word_list[index1] = "_"
        return (board, word_list)

    def printVictory():
        print ("Well done! You got the word.")

    def printGameOver():
        print ("Sorry, too many wrong guesses. Game over.")

    def printFullDef(word, selection):
        print ("The word was ", w, "- ", selection["type"], " ", selection["definition"])


# Run Code
    print("This ain't baseball, it's SAT Hangman. Six strikes and you're out.")

    d = createDictionary(["sat-words/dictionary.json", "sat-words/dictionary2.json"])
    letters = "abcdefghijklmnopqrstuvwxyz-"
    winstreak = 0
#    selection = getSelection(d)

    # New Game Loop
    while True:
        print ("New round, here we go.")
        showWinStreak()
        strikes = 0
        selection = random.choice(d)
        w = selection["word"].lower()
        w_list = list(w)
        board = makeBoard(w)
        guesses = []

        # Guessing Loop
        while True:
            showBoard(board)
            showStrikes(strikes)
            showGuesses(guesses)
            guess_tup = takeGuess(letters, guesses)
            print(guess_tup)
            g = guess_tup[0]
            guesses = guess_tup[1]
            if g in w:
                printGoodNews()
                board_tup = updateBoard(w_list, board, g)
                board = board_tup[0]
                w_list = board_tup[1]
                if "_" not in board:
                    printVictory()
                    printFullDef(w, selection)
                    winstreak += 1
                    break
            else:
                printBadNews()
                strikes += 1
                if strikes == 6:
                    printGameOver()
                    printFullDef(w, selection)
                    winstreak = 0
                    break

runHangman()






#get dictionary
#get random entry
#Show Player working_word
#Ask player to guess
#Authenticate input
#Check input against word
#Swap index of working_word with index of word for correct Guesses

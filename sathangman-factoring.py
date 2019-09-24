import random
import json

def runHangman():

    def initialize():
        # Initialize by importing/creating a dictionary,
        # defining acceptable input (letters) and winstreak
        dict0 = makeDictionary()
        letters = "abcdefghijklmnopqrstuvwxyz-"
        # Set Win Streak to 0
        winstreak = 0
        # Set the guess list to empty string
    print("This ain't baseball, it's SAT Hangman. Six strikes and you're out.")

    def makeDictionary():
        # Import and Parse JSON word dictionaries into a single dictionary
        json1 = open ("sat-words/dictionary.json")
        dict1 = json.load(json1)
        json2 = open ("sat-words/dictionary2.json")
        dict2 = json.load(json2)
        return dict1 + dict2

    def getNewSelection(dictionary):
        random.choice(dictionary)

    def populateCharBlanks(word, working_word):
        for char in range(len(word)):
            working_word += "_"
            return working_word
    working_word = populateCharBlanks()

    def refreshRoundVars(dictionary):
            selection = getNewSelection(dictionary)
            word = selection["word"].lower()
            pos = selection["type"]
            definition = selection["definition"]
            strikes = ""
            guess_list = []
        # Set a new variable called working_word representing the gameboard, then
        # populate it with as many _'s as the random word has characters.
            working_word = populateCharBlanks(word, working_word)
        # Create separate list variables for the random word, the game board,
            w_list = list(word)
            ww_list = list(working_word)
            return

    def updateBoard(guess, w_list, ww_list, working_word):
        index = w_list.index(guess)
        ww_list[index] = guess
        w_list[index] = "_"
        working_word = "".join(ww_list)
        return [w_list, wW_list, working_word]


    # Grab a random selection from dictionary along with part of speech and definition
initialize()
dict 0 = makeDictionary()
while game is active:
    selection = getNewSelection(dict0)
    strikes = ""
    guess_list = []
    while round is active:
        Getguess()
    if guess is unqualified
        GetGuess()
    else:
        updateGuessList()
        if present in word
        updateBoard())
        else
        incrementStrikes()
if lose:
    determineVictory():
else:
    determineDefeat():



    # Round Loop
    while True:
            # Set Strikes to an empty string and
            # Guess list to empty list
        refreshRoundVars(dict0)
        # Game-Active Loop.
        # If either condition == True, it is an active game.
        while "XXXXXX" not in strikes and "_" in working_word:
            print("----------------------------")
            print("Winstreak: ", winstreak)
            print("Strikes: ", strikes)
            print("Previous Guesses: ", "".join(guess_list))
            print("Your word is: " + working_word)
            print("")
            # Take a guess from the user.
            # Check if the guess is qualifying. If not, ask again.
            guess = input("Go ahead, guess a letter:")
            print("..........................")

            if len(guess) != 1 or guess not in letters:
                guess = print("Sorry, I only take single lowercase letters of the English alphabet. Maybe try a vowel. Or a consonant.")
            # Check if the guess has already been guessed. Ask again if so.
            elif guess in guess_list:
                guess = print("You already guessed that one. Try again:")
            else:
                guess_list += guess
                if guess in w_list:
                    while guess in w_list:
                        swapCorrect()
                        print("Nice! Got one.")
                    if "_" in ww_list:
                            print("Try again.")
                else:
                    strikes += "X"
                    print("Not so much.")

        #  End of Game determination.
        if strikes == "XXXXXX":
            print("Bummer, you lost. The word was " + word + ".")
            print("")
            print (word + " – " + pos + " " + definition)
            print("")
            print ("Game Over, friend. :(")
            winstreak = 0
        else:
            #wins += 1
            print("")
            print("Awesome! You got it. The word was " + word + ". You win!")
            print("")
            print (word + " – " + pos + " " + definition)
            print("")
            print("+1 for the Win Streak. See how many you can get in a row!")
            print("")
        winstreak += 1

runHangman()

import random
import json

# Set Win Streak and High Score Counters
def runGame():
    # Import and Parse JSON word dictionaries into a single dict
    # Define accedptable letters for user input
    json1 = open ("sat-words/dictionary.json")
    dict1 = json.load(json1)
    json2 = open ("sat-words/dictionary2.json")
    dict2 = json.load(json2)
    dict = dict1 + dict2
    letters = "abcdefghijklmnopqrstuvwxyz"
    guess_list = ""
    # Set the winstreak to 0,
    winstreak = 0
    print("")
    print("This ain't baseball, it's SAT Hangman. Six strikes and you're out.")
    print("")
    # Startroundloop
    while True:
        # Set strikes to an empty string
        strikes = ""
        # Grab a random selection from dictionary
        # Define variables for the word, part of speech,
        # and definition of the random selection
        selection = random.choice(dict)
        word = selection["word"].lower()
        pos = selection["type"]
        definition = selection["definition"]
        # Set a new variable called working_word representing the gameboard, then
        # populate it with as many _'s as the random word has characters.
        working_word = ""
        for char in range(len(word)):
            working_word += "_"
        # Create separate list variables for the random word, the game board,
        # and letters already guessed
        w_list = list(word)
        ww_list = list(working_word)
        guess_list = []
        # While loop to test if the game is active.
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
                        index = w_list.index(guess)
                        ww_list[index] = guess
                        w_list[index] = "_"
                        working_word = "".join(ww_list)
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

runGame()

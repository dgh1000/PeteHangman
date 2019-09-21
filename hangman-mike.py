#
#

def runGame():
    # Guess letters of the alphabet until fill in phrase without guessing
    # too many wrong letters.
    #
    # Players guesses letters of alpha. , program acknowledges correct or
    # incorrect. if correct fill in blank, if inaccurate fill in body part.
    # check for hanging body.
    #
    # if then else: conditional structure
    # while: loop structure
    # for : loop
    #
    isSolved = False
    isDead = False
    workingAnswer = '______'
    answer = 'cookie'
    counter = 0

    while not isSolved and not isDead:
        # request a character from user
        c = input('enter a letter')
        # comparison
        if <c in string>:
            print 'success'
            print the word with empty dashes
            if all solved:
                isSolved = True
        else:
            increment counter
            if counter == 6:
                isDead = True
     if isSolved :
         print 'happy days'
     else:
         print 'may God bless your soul'


        # respond: right or wrong, also check game over


#runGame()
print("hi!")
print('hi!\n')

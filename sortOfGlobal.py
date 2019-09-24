
# --------------------------------------------------------------------------
#  Simple example below
def main():
    d = {'strikes': 1, 'selected': 'antidisestablishmentarism', 'working' : '___' }
    doSomething(d)
    print( d ['strikes'])

def doSomething(d):
    d['strikes'] = 'yup!'
    d2['strikes'] = 'yup!'

# uncomment this to run simple example
# main()

# --------------------------------------------------------------------------
#  More complicated example below
def playRound(d):
    # The following will raise an exception if the user
    # enters something other than an integer. We'll leave
    # that be, for now.
    n = int(input('Enter a number:'))
    if n % 2 == 0:
        d['evens'] = d['evens'] + 1
    else:
        d['odds'] = d['odds'] + 1

def main2():
    d = { 'odds': 0, 'evens': 0 }
    while True:
        playRound(d)
        if d['odds'] + d['evens'] > 4:
            break

    print('You ended up with {} odd numbers and {} even'.format(d['odds'], d['evens']))

# uncomment this to run 
main2()


def guessBigOrSmall(guess):
    import random
    a_list = [ random.randrange(1, 7),  random.randrange(1, 7), random.randrange(1, 7)]
    print ('<<<<< ROLE THE DICE!>>>>>')
    print ('The points are' + str(a_list)),
    if sum(a_list) <= 10 and guess == 'Small':
        return True
    elif sum(a_list) > 10 and guess == 'Big':
        return True
    else:
        return False

running=True
print ('<<<<< GAME STARTS! >>>>>')
while running:
    guess = raw_input('Big or Small:')
    if guessBigOrSmall(guess):
        print ('you win!')
    else:
        print ('you lose!')
    if raw_input('try again?')=='yes':
        running=True
    else:
        running=False
print ('Game Over!')


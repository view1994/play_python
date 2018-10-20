#coding:utf-8

import random
choice={'Big','Small'}
money=1000;
def main():
    #global money
    while money>0:
        start_game()
    else:
        print ("GAME OVER!")

def start_game():
    global money
    print ('<<<<<<<<<<<<<<<<<<GAME STARTS!>>>>>>>>>>>>>>>>>>>')
    guess=raw_input("Big or Small?")
    while guess not in choice:
        guess = raw_input('invalid word!please type \"Big\" or "Small:"')
    else:
        bet=raw_input('How much do you wanna bet? -')
        while int (bet)>money:
            bet = raw_input ('your bet is too much, please bet a num less than your money:-')
        points_sum=roll_the_dice()
        if (points_sum>10 and guess=='Big') |(points_sum<=10 and guess=='Small'):
            print ('YOU WIN!')
            money+=int(bet)
            print ('you gained '+bet+',you have '+str(money)+' now')
        else:
            print ('YOU LOSE')
            money-=int(bet)
            print('you lost '+bet+',you have '+str(money)+' now')

def roll_the_dice():
    print ('<<<<<<<<<<<<<<<<ROLL THE DICE!>>>>>>>>>>>>>>>>>>')
    import random
    a_list=[random.randrange(1,7),random.randrange(1,7),random.randrange(1,7)]
    print ('the points is '+str(a_list)),
    return sum(a_list)

if __name__ == "__main__":
    main()

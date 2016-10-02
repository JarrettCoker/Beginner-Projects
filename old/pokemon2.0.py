# Turn Based Pokemon Style Game
# Python 2.7.10
# Written by Oddjob922

import time, random, sys



def play_again():
    opt = raw_input('Would you like to play again? [Y/N]\n>')
    if opt == 'y' or opt == 'Y':
        game()
    elif opt == 'n' or opt == 'N':
        print 'Thanks for playing! Game written by Oddjob922'
        gameOver = True
        sys.exit(0)




def scratch(p_health,c_health,whos_turn):
    fail_chance = random.randint(1,5)
    print '%s uses scratch!' % whos_turn
    time.sleep(1)
    if fail_chance == 4:
        print '...But it failed!'
        if whos_turn == 'Player':
            return c_health
        elif whos_turn == 'Opponent':
            return p_health
    else:
        damage = random.randint(18,25)
        if whos_turn == 'Player':
            c_health = c_health - damage
            print 'Scratch dealt %i damage to the opponent!' % damage
            return c_health
        elif whos_turn == "Opponent":
            p_health = p_health - damage
            print 'Scratch dealt %i damage to you!' % damage
            return p_health

def stomp(p_health,c_health,whos_turn):
    fail_chance = random.randint(1,5)
    print '%s uses stomp!' % whos_turn
    time.sleep(1)
    if fail_chance == 4:
        print'...But it failed!'
        if whos_turn == 'Player':
            return c_health
        elif whos_turn == 'Opponent':
            return p_health
    else:
        damage = random.randint(10,35)
        if whos_turn == 'Player':
            c_health = c_health - damage
            print 'Stomp dealt %i damage to the opponent!' % damage
            return c_health
        elif whos_turn == "Opponent":
            p_health = p_health - damage
            print 'Stomp dealt %i damage to you!' % damage
            return p_health

def self_heal(p_health,c_health,whos_turn):
    fail_chance = random.randint(1,5)
    print '%s uses self-heal!' % whos_turn
    time.sleep(1)
    if whos_turn == 'Player' and p_health > 75:
        print "...But your health is too high!"
        return p_health
    elif whos_turn == 'Opponent' and c_health > 75:
        print "...But their health is too high!"
        return c_health
    else:
        if fail_chance == 4:
            print'...But it failed!'
            if whos_turn == 'Player':
                return p_health
            elif whos_turn == 'Opponent':
                return c_health
        else:
            heal_amount = random.randint(18,25)
            if whos_turn == 'Player':
                p_health = p_health + heal_amount
                print 'Self-heal gave back %i HP to you!' % heal_amount
                return p_health
            elif whos_turn == "Opponent":
                c_health = c_health + heal_amount
                print 'Self-heal gave back %i HP the opponent!' % heal_amount
                return c_health
        





def game():
    gameOver = False
    p_health = 100; c_health = 100 #Declaring initial health values for player and computer
    whos_turn = 'Player' #Player gets first turn
    while gameOver == False:
        time.sleep(1)
        if p_health <= 0:
            print "You ran out of health and lose!"
            play_again()
        elif c_health <= 0:
            print "Your opponent ran out of health, you win!"
            play_again()
        else:
            if whos_turn == 'Player':
                print '''The moves available to you are:
                -1: Scratch (18-25 damage)
                -2: Stomp (10-35 damage)
                -3: Self-heal (18-25 HP)
                There is always a chance that any move might fail, so be careful!'''
                print "Your opponent has %i health, and you have %i" % (c_health,p_health) #prints out current health of player and computer
                error = True
                while error == True:
                    try:
                        move = raw_input('Its your turn, pick a move!\n>')
                        move = int(move)
                        error = False
                    except ValueError:
                        print "Not a valid move!"
                        time.sleep(1)
                if move == 1:
                    c_health = scratch(p_health,c_health,'Player')
                    whos_turn = 'Opponent'
                elif move == 2:
                    c_health = stomp(p_health,c_health,'Player')
                    whos_turn = 'Opponent'
                elif move == 3:
                    p_health = self_heal(p_health,c_health,'Player')
                    whos_turn = 'Opponent'
            elif whos_turn == 'Opponent':
                if c_health < 35:
                    c_lowhealth_chance = random.randint(1,2)
                    if c_lowhealth_chance == 2:
                        c_health = self_heal(c_health,p_health,'Opponent')
                        whos_turn = 'Player'
                        continue
                    else:
                        move = random.randint(1,3)
                        if move == 1:
                            p_health = scratch(p_health,c_health,'Opponent')
                            whos_turn = 'Player'
                        elif move == 2:
                            p_health = stomp(p_health,c_health,'Opponent')
                            whos_turn = 'Player'
                        elif move == 3:
                            c_health = self_heal(p_health,c_health,'Opponent')
                            whos_turn = 'Player'
                        
                else:
                    move = random.randint(1,3)
                    if move == 1:
                        p_health = scratch(p_health,c_health,'Opponent')
                        whos_turn = 'Player'
                    elif move == 2:
                        p_health = stomp(p_health,c_health,'Opponent')
                        whos_turn = 'Player'
                    elif move == 3:
                        c_health = self_heal(p_health,c_health,'Opponent')
                        whos_turn = 'Player'
game()

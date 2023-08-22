"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    sum=0
    has1=False
    while num_rolls:
        current_dice=dice()    
        if current_dice==1:
            has1=True
        else:
            sum += current_dice
        num_rolls-=1
    if has1:
        return 1
    return sum
    


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2
    if (player_score%10 - opponent_score//10%10) ==0:
        return 1
    else:
        return 3*abs(player_score%10 - opponent_score//10%10)



def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3
    if num_rolls:
        return roll_dice(num_rolls,dice) 
    else:
        return boar_brawl(player_score, opponent_score)

    #take_turn(3, 15, 9, make_test_dice(4, 6, 1))
    #1
    #
    #take_turn(0, 12, 41)
    #6




def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Fuzzy Factors.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def hog_gcd(x, y):
    """Return the greatest common divisor between X and Y"""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    gdc, counter = 1, 1 
    if x==0 or y==0:                # if x or y is 0, then return non-zero 
        return (max(x,y))
    while counter<= min(x,y):       #iterates x times or y times depending on which is lower
        if x%counter==0 and y%counter==0:
            gcd = counter
        counter+=1
    return gcd
     

    #one way is to find the divisors for both separately, then combine them again
    #together, then 




def fuzzy_points(score):
    """Return the new score of a player taking into account the Fuzzy Factors rule.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    if hog_gcd(score,100)>10:
        return score+ 2* (hog_gcd(score, 100)//10%10)
    return score 


def fuzzy_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Fuzzy Factors.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    return fuzzy_points(simple_update(num_rolls, player_score, opponent_score, dice))
    
     
    
    


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the oppononent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, fuzzy_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Fuzzy
    Factors rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as fuzzy_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    #won==False
    while (score0<goal and score1<goal):  
        if who==0:
            num_roll = strategy0(score0,score1)
            score0=update(num_roll,score0,score1,dice)
        elif who==1:
            num_roll = strategy1(score1,score0)
            score1= update(num_roll,score1,score0,dice)
        who=1-who

    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # END PROBLEM 6
    return lambda x,y: n


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    # END PROBLEM 7
    #limit=goal
    while True:
        for i in range(goal):
            for j in range(goal):
                if strategy(i,j)==strategy(j,i)==strategy(i,i)==strategy(j,j):
                    continue
                else:
                    return False
        if strategy(i,j)==strategy(j,i)==strategy (i,i)==strategy(j,j):
            return True

    


    



def make_averaged(original_function, total_samples=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)(1,dice) = 3.0
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8
    def average_helper(*args):
        sum=0
        for i in range(total_samples):
            sum+= original_function(*args)
        return sum/(total_samples)

    return average_helper

#dice = make_test_dice(3, 1, 5, 6)
#averaged_roll_dice = make_averaged(roll_dice, 1000) (2, dice)
#the (2,dice) means in roll_dice, there are num_rolls=2, the dice is (3,1,5,6)
#def roll_dice(num_rolls, dice=six_sided): REMINDER
#   returns sum if there's no 1 within the num_rolls 

#so sort of like make_averaged(roll_dice(2,dice) , 1000)

#(3,1) has a 1 so sum is 0. (5,6) is sum 11
#thousand times?  1(500) + (11)(500) = 6000. Average is 6000/1000=6.0


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    i,max,max_value=1,0,0
    while i<=10:
        x=make_averaged(roll_dice,total_samples)(i,dice)
        if x >max_value:
            max=i
            max_value = x
        i=i+1
    return max
    # END PROBLEM 9






def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, fuzzy_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6)))  # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('fuzzy_strategy win rate:', average_win_rate(fuzzy_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def boar_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Fuzzy Factors.
    """
    # BEGIN PROBLEM 10
    if boar_brawl(score,opponent_score )>=threshold:
        return 0
    else:
        return num_rolls

    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def fuzzy_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11

    newScore = fuzzy_update(0, score, opponent_score)
    if newScore >=  threshold+score:
        return 0
    else:
        return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11

#fuzzy_strategy(31, 21, threshold=10, num_rolls=2)
#1*3 = 3 
#3 + 31 = 34
#34 is not fuzzy. so no cool update to the current score
#34-31 = 3, but the threshold is 10 so we return num_roll=2

#fuzzy_strategy(44, 63, threshold=?, num_rolls=5)
#2*3 =  6
#6+44  = 50 
#50 is fuzzy yes so 
#50 + 2*5 = 50 + 10 =  60
#60-44 = 16, which is greater than threshold, i think so it returns numRolls not 0..?


#fuzzy_strategy(14, 21, threshold=8, num_rolls=2)
#2*3 = 6
#14+6 = 20
#20 is fuzzy yes so 
#20+ 2*2 = 24
#24-14 = 10 VS. 8 and 10>=8 so return 0





#fuzzy_strategy(30, 41, threshold=10, num_rolls=2)
#4-0 = 4. 4*3  = 12 
#30+12 = 42 
#42 and 100 gcd is under 10 so no fuzzy number 
#apparently you return 0 IDK why

#fuzzy_strategy(14, 21, threshold=8, num_rolls=2)
#2*3 = 6 
#14+6=20
#20 and 100 gcd is above 10, so yes 20 is a fuzzy. 
#2*2 = 4
#20+4 = 24 VS 20 + 10 =30
#answer is 0 IDK 

#fuzzy_strategy(14, 21, threshold=12, num_rolls=5)
#2*3 = 6
#14+6=20
#20 and GCD is is aboe 10, so 20 is yes fuzzy
#2*2 = 4
#20+4 = 24 VS 20+12 = 32
#answer is 5 IDK




    #fuzzy_strategy(44, 16, threshold=10, num_rolls=2) is apparently 50 
    # 


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

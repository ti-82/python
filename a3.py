# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################


def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer = []
    other = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # NOTE maybe shuffle here
    for n, card in enumerate(deck):
        if n % 2 == 1:
            dealer.append(card)
        else:
            other.append(card)

    return (dealer, other)


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    numCards = [card[:-1] for card in l]

    # set of unique number cards
    cards = set(numCards)

    for card in cards:
        # if this card is present in pairs
        if numCards.count(card) % 2 == 0:
            continue

        else:
            indx = numCards.index(card)
            no_pairs.append(l[indx])

    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    string = ' '.join(deck)
    print(string)


def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''

    num = input(f"Give me an integer between 1 and {n}: ")

    if num.isdigit():
        num = int(num)

        if num >= 1 and num <= n:
            return num

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    while True:

        num = input(f"Invalid number. Please enter integer between 1 and {n}: ")

        if num.isdigit():
            num = int(num)
            if num >= 1 and num <= n:
                return num


def get_suffix(n):
    """
    return the correct suffix for the integer n

    Precondition: n >= 1
    """

    if n == 1:
        sfx = 'st'
    elif n == 2:
        sfx = 'nd'
    elif n == 3:
        sfx = 'rd'
    else:
        sfx = 'th'

    return sfx


def play_game():
    '''()->None
    This function plays the game'''

    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # COMPLETE THE play_game function HERE
    turn = 1

    while True:
        print('*' * 30)

        if turn == 1:
            print('Your turn.\n')
            print('Your current deck of cards is:\n')
            print_deck(human)

            n = len(dealer)
            print(f'\nI have {n} cards. If 1 stands for my first card and')
            print(f'{n} for my last card, which of my cards would you like?')

            m = get_valid_input(n)
            sfx = get_suffix(m)

            print(f'You asked for my {m}{sfx} card.')
            print(f'Here it is. It is {dealer[m-1]}\n')
            print(f'With {dealer[m-1]} added, your current deck of cards is:\n')

            # update the decks
            human.append(dealer[m-1])
            del dealer[m-1]
            print_deck(human)

            # remove pairs
            print("\nAnd after discarding pairs and shuffling, your deck is:\n")
            human = remove_pairs(human)
            print_deck(human)
            print()

            # update the turn
            turn = (turn + 1) % 2
            wait_for_player()

        # computer turn
        else:
            print('My turn.')
            m = random.randint(0, len(human)-1)
            sfx = get_suffix(m+1)

            # update the decks
            dealer.append(human[m])
            del human[m]

            print(f'\nI took your {m+1}{sfx} card.')

            # update the turn
            turn = (turn + 1) % 2
            wait_for_player()

            # remove pairs at each turn
            dealer = remove_pairs(dealer)

        # win conditions
        if len(human) == 0:
            print('*' * 30)
            print('Ups. You do not have any more cards')
            print('Congratulations! You, Human, win')
            break

        elif len(dealer) == 0:
            print('Ups. I do not have any more cards')
            print('You lost! I, Robot, win')
            break


# main
play_game()

# poker.py
# 2017, polarysekt


from random import randint

g_ghPOKER_SUITS = [ "&spades;", "&hearts;", "&clubs;", "&diams;" ]
g_ghPOKER_VALUES = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]


def getDeck():
    retDeck = []
    for i in range(52):
        retDeck.append( i);
    
    return retDeck

def getHand():
    deck = getDeck()
    retHand = [ deck[randint(0,51)],deck[randint(0,51)],deck[randint(0,51)], deck[randint(0,51)], deck[randint(0,51)], deck[randint(0,51)], deck[randint(0,51)] ]

    return retHand

def getHandHTML():
    hand = getHand()
    retString = ""
    for ind in range(2):
        i = hand[ind]
        retString += '<span class="ghPokerCard">'
        s = getCardSuit(i)
        if s % 2 != 0:
            retString += '<span class="cardRed">'
        retString += str(getCardValue( i ))
        retString += getCardSuitHTML( i )
        if s % 2 != 0:
            retString += '</span>'
        retString += "</span> "
    retString += '<div class="ghPokerTable">'
    for ind in range(2,7):
        i = hand[ind]
        retString += '<span class="ghPokerCard">'
        s = getCardSuit(i)
        if s % 2 != 0:
            retString += '<span class="cardRed">'
        retString += str(getCardValue( i ))
        retString += getCardSuitHTML( i )
        if s % 2 != 0:
            retString += '</span>'
        retString += "</span> "
    retString += '</div>'
    return retString

def test_units():
    hand = getHand()
    getCardValue( hand[0] );
    getCardSuit( hand[0] )
    
    print( getHandHTML() )
    return True


def getCardValue( card ):
    return g_ghPOKER_VALUES[card % 13]

def getCardSuit( card ):
	return int(card/13)

def getCardSuitHTML( card ):
    return g_ghPOKER_SUITS[getCardSuit(card)]


def main():
    test_units()

if __name__ == "__main__":
    main()

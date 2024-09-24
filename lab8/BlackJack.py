import random, time
#import turtle

class Card():
    ''' Card(): create a card object. To create a deck, try \Card.test_Card()\! '''
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card(self):
        Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
        Suits = ['D','C','H','S']
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return ' '.join(res)
    #---------------------------------------------------------------------
    def render(self, x, y, color='blue', RENDER=False):
        ''' วาดไพ่ด้วยเต่า '''
        if not RENDER:
            return None
        # Draw border
        pen.penup()
        pen.color(color)
        pen.goto(x+50, y+75)
        xy = ((x+50, y+75), (x+50, y-75), (x-50, y-75), (x-50, y+75))
        pen.begin_fill()
        pen.pendown()
        for pos in xy:
            pen.goto(pos)
        pen.end_fill()
        pen.penup()
        # Draw card info
        if self.name not in ['','O']:
            # Draw suit in the middle
            pen.color('white')
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        pen.penup()
    #---------------------------------------------------------------------

class Deck:
    ''' Deck(): สร้างสำรับไพ่ '''
    Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Suits = ['D','C','H','S']
    def __init__(self):
        Names = Deck.Names
        Suits = Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names = Deck.Names
        Suits = Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return ' '.join(res)

def preamble(RENDER=False):
    ''' จัดการ environment ในการวาดเต่า '''
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor('black')
    wn.setup(800, 600)
    wn.title('Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet')
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------

def test_turtle_deck(RENDER=False):
    ''' ไว้ตรวจสอบเต่าวาดไพ่ ฟังชัน Card.render() '''
    preamble(RENDER)
    # create a deck f card
    deck = Deck()
    # shuffle deck
    deck.reset()
    print(deck)
    # render n cards (back) in a row
    nbOfCards = 5
    start_x = -250
    for x in range(nbOfCards):
        card = Card('', '')
        card.render(start_x + x*125, 175, 'orange', RENDER=True)
    time.sleep(1)
    # re-render n cards in a row
    start_x = -250
    for x in range(nbOfCards):
        card = deck.get_card()
        card.render(start_x + x*125, 175, RENDER=True)
    print('Done..')

def createVirtualDeck(s='K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'):
    dd = s.split()
    res = []
    suit = {'♦':'D','♣':'C','♥':'H','♠':'S'}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck
#------------------------------------------------------------------------------#
def count_function(cards):
    if not isinstance(cards, list):
        cards = [cards]
    score = 0
    aces = 0
    for card in cards:
        name = card.get_name()
        if name in ['J', 'Q', 'K', 'T']:
            score += 10
        elif name == 'A':
            aces += 1

        else:
            score += int(name)

    score += aces * 11
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def print_game(player, cards, countA, countB, x, show = False):
    if x == 1:
        a = countA
    else:
        a = countB
    if x == 1 and show == False:
        start_com_sym = cards[0]
        show_card = cards[1]
        lens = len(player)
        print(f"{' '*(9-lens)}{player}: O{Card.symbols[start_com_sym.get_suit()]} {show_card}{' '*(11-(3 * (a)))}-> {count_function(show_card)}")
    else:
        lens = len(player)
        print(f"{' '*(9-lens)}{player}: {' '.join(map(str, cards))}{' ' * (11-(3 * a))}-> {count_function(cards)}")



def action(player):
    action = str(input("Draw another card (y/n): ")).lower()
    if action in ['y', 'n']:
        return action
def play(player1='Computer', player2='Player', d=None, RENDER=False):
    print('Welcome to MikeLab BlackJack Casino.')
    preamble(RENDER)

    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:
        #----------------------------- virtual deck
        #d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)
    countA = 0
    countB = 0
    computer_hand = [deck.get_card()]
    human_hand = [deck.get_card()]
    computer_hand.append(deck.get_card())
    human_hand.append(deck.get_card())
    #print(deck)
    s_human = 0
    s_com = 0


    print_game(player1, computer_hand, countA, countB,1,)
    print_game(player2, human_hand, countA,countB,2)
    a = "++++++++++++++++++++++++++++++++++++++++++++++++++"
    if count_function(human_hand) < 21:
        while True:
            if len(human_hand) >= 5 and count_function(human_hand) <= 21:
                s_human = 999
                break
            if  count_function(human_hand) < 21 and (action(player2) == 'y' and len(human_hand) < 5):
                countB += 1
                human_hand.append(deck.get_card())
                print_game(player2, human_hand, countA, countB,2)
            else: break


    while True:
        if count_function(human_hand) <= 21 and len(computer_hand) < 5:
            if (count_function(computer_hand) <= 16  or count_function(computer_hand) < count_function(human_hand) or len(human_hand) > len(computer_hand)) and count_function(computer_hand) < 21 and len(computer_hand) < 5 :
                computer_hand.append(deck.get_card())
                countA += 1
                if (count_function(computer_hand) < count_function(human_hand) or count_function(computer_hand) <= 16) and count_function(computer_hand) <=21  and len(computer_hand) < 5:
                    computer_hand.append(deck.get_card())
                    countA += 1
                elif len(human_hand) == 5 and count_function(computer_hand) <21 and len(computer_hand) < 5:
                    computer_hand.append(deck.get_card())
                    countA += 1


                else: break
            elif count_function(computer_hand) > count_function(human_hand) :
                break

            elif (count_function(computer_hand) <= 16 or len(computer_hand) < 5) and count_function(computer_hand) < 21 and len(computer_hand) < 5 :
                computer_hand.append(deck.get_card())
                countA += 1

            elif len(computer_hand) == 5:
                break
            else:
                break
        elif count_function(human_hand) > 21:
            if count_function(computer_hand) <= 16 and count_function(computer_hand) < 21 and len(computer_hand) < 5 :
                computer_hand.append(deck.get_card())
                countA += 1
            else:
                break
        else:
            break

    print("+++++++++++++++++++++++++++++++++")
    print_game(player1, computer_hand, countA, countB,1, show = True)
    print_game(player2, human_hand, countA, countB,2)
    print(a)
    #human_hand.append(deck.get_card())
    computer_score = int(count_function(computer_hand))
    human_score = int(count_function(human_hand))
    if computer_score > 21:
        computer_score = 0
    if human_score > 21:
         human_score = 0
    # #print(s_com)

    s_human += human_score
    s_com += computer_score



    if len(human_hand) == 5 or count_function(human_hand) == 21:
        s_human = 1999
    elif count_function(human_hand) == 21 and len(human_hand) <= 5 :
        s_human =999

    if len(computer_hand) == 5 or count_function(computer_hand) == 21:
        s_com = 1999
    elif count_function(computer_hand) == 21 and len(computer_hand) <= 5:
        s_com = 999
    if len(human_hand) == 5 and len(computer_hand) != 5 and human_score < 21:
        s_human = 2000

    if len(computer_hand) == 5 and len(human_hand) != 5 and computer_score < 21:
        s_com = 2000
    if len(computer_hand) == 2 and computer_score ==21:
        s_com = 2000
    if len(human_hand) == 2 and human_score == 21:
        s_human = 2000
    if len(computer_hand) == 5 and len(human_hand) == 5:
        if computer_score ==0 and human_score <=21:
            s_com = 0
        elif human_score ==0 and computer_score <=21:
            s_human = 0



    if s_com > s_human :
        print(f"{player1} wins.")
    elif s_human > s_com:
        print(f"{player2} wins.")
    else:
        print("Draw!")
    print(a)



    #----------------------
    #print(deck) # for DEBUG
    #----------------------
    ###-------------- student code begins here --------------###
#play()
 ###--------------- student code ends here ---------------###
## main begins here
def testcase01():
    random.seed(2)
    play()
def testcase02():
    random.seed(16)
    play()
def testcase03():
    random.seed(30)
    play()
def testcase04():
    s = 'K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'
    play('Toto', 'Tutu', d=s)

def testcase05():
    s = 'A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase06():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase07():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠'
    play(d=s)
def testcase08():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠'
    play(d=s)
def testcase09():
    s = '5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
#------------------------------------------
q = int(input())
if q==1:
    testcase01()
elif q==2:
    testcase02()
elif q==3:
    testcase03()
elif q==4:
    testcase04()
elif q==5:
    testcase05()
elif q==6:
    testcase06()
elif q==7:
    testcase07()
elif q==8:
    testcase08()
elif q==9:
    testcase09()

#bug about aces 20 point
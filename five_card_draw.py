'''
-standard set of cards modeled (52, 4 of each from A to K)
-user recieves 5 random cards, as well as the computer
-user decides which cards to hold
-the computer calculates the best value and holds cards accordingly
-cards not held will be sent to the bottom of the deck (so they will not be used for the rest of the round)
-user cards are compared to the computer, the winner is decided by these points:
High-nothings:
    2-2
    3-3
    4-4
    5-5
    6-6
    7-7
    8-8
    9-9
    10-10
    J-11
    Q-12
    K-13
    A-14

Royal Flush: 119-131 (+117)
Straight Flush: 106-118 (+104)
Four of a Kind: 93-105 (+91)
Full House: 80-92 (+78)
Flush: 67-79 (+65)
Straight: 54-66 (+52)
3 of a kind: 41-53 (+39)
Two Pair: 28-40 (+26)
Two of a Kind: 15-27 (+13)
High Card: 2-14

-game can go on with a score between the user and the computer until the user decides to stop
'''
import random
from tkinter import *
from tkinter import ttk
class Poker:
    def __init__(self):
        self.score = 0
        self.cards = ["2C","2D","2H","2S",
             "3C","3D","3H","3S",
             "4C","4D","4H","4S",
             "5C","5D","5H","5S",
             "6C","6D","6H","6S",
             "7C","7D","7H","7S",
             "8C","8D","8H","8S",
             "9C","9D","9H","9S",
             "10C","10D","10H","10S",
             "JC","JD","JH","JS",
             "QC","QD","QH","QS",
             "KC","KD","KH","KS",
             "AC","AD","AH","AS"]

    def count_cards(self,user_held):
        m2 = m3 = m4 = m5 = m6 = m7 = m8 = m9 = m10 = mJ = mQ = mK = mA = 0
        #user_held = ['2','2','2','2','6']
        for card in user_held:
            start = card[0]
            match start:
                case '2':
                    m2+=1
                case '3':
                    m3 += 1
                case '4':
                    m4 += 1
                case '5':
                    m5 += 1
                case '6':
                    m6 += 1
                case '7':
                    m7 += 1
                case '8':
                    m8 += 1
                case '9':
                    m9 += 1
                case '1':
                    m10 += 1
                case 'J':
                    mJ += 1
                case 'Q':
                    mQ += 1
                case 'K':
                    mK += 1
                case 'A':
                    mA += 1
        matches = [m2, m3, m4, m5, m6, m7, m8, m9, m10, mJ, mQ, mK, mA]
        return matches
    def card_switches(self,card):
        match card[0]:
            case 'A':
                pog = 14
            case 'K':
                pog = 13
            case 'Q':
                pog = 12
            case 'J':
                pog = 11
            case '1':
                pog = 10
            case _:
                pog = int(card[0])
        return pog
    def find_high_nothing(self,matchy):
        if matchy[-1]:
            print("Ace high nothing!")
            self.score = 14
        elif matchy[-2]:
            print("King high nothing!")
            self.score = 13
        elif matchy[-3]:
            print("Queen high nothing!")
            self.score = 12
        elif matchy[-4]:
            print("Jack high nothing!")
            self.score = 11
        else:
            print("You have absolutely nothing!")
    def check_for_straights(self,sheesh):
        num_list = []
        is_straight = False
        is_royal = False
        #sheesh = ['KS','AS','JS','QS','10S']
        for pog in sheesh:
            pog = self.card_switches(pog)
            print(pog)
            num_list.append(pog)
        num_list.sort()
        print(num_list)
        print("set num_list:", list(set(num_list)) == num_list)
        if (num_list[-1]-num_list[0]== 4 or num_list == [2,3,4,5,14]) and list(set(num_list)) == num_list:
            is_straight = True
            if num_list == [10,11,12,13,14]:
                is_royal = True
                print("is royal?",is_royal)
        print(is_straight, "is straight")
        return (is_straight,is_royal,num_list[-1])

    def check_for_suit(self,sheesh):
        is_suit = True
        suit_list = []
        #sheesh = ['C','C','C','C','C']
        for s in sheesh:
            suit_list.append(s[-1])
        identical = suit_list[0]
        print("suit list:",suit_list)
        for s in suit_list:
            if not s==identical:
                is_suit = False
                pass
            identical = s
        return is_suit
    def hold(self,card):
        return
    def main(self):
        user_1 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(user_1)
        user_2 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(user_2)
        user_3 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(user_3)
        user_4 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(user_4)
        user_5 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(user_5)

        cpu_1 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(cpu_1)
        cpu_2 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(cpu_2)
        cpu_3 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(cpu_3)
        cpu_4 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(cpu_4)
        cpu_5 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(cpu_5)
        user_result = [user_1,user_2,user_3,user_4,user_5]
        root = Tk()
        frm = ttk.Frame(root, padding=100)
        frm.grid()
        ttk.Label(frm, text="Choose which cards to hold").grid(column=2, row=0)
        #ttk.Label(text="").grid(column=)
        for i in range(3,8):
            ttk.Button(frm, text=user_result[i-3], command=root.destroy).grid(column=i, row=20)
        root.mainloop()
        user_held = []
        hold_amount = int(input("How many cards would you like to hold? "))
        for i in range(hold_amount):
            card_hold = int(input("Type the number of the card (1-5): "))
            if card_hold not in user_held:
                user_held.append(user_result[card_hold-1])
        while len(user_held) <5:
            user_held.append(self.cards[random.randint(0, len(self.cards) - 1)])
        print("Your final cards:",user_held[0],user_held[1],user_held[2],user_held[3],user_held[4])
        #user_held = ['6S','4C','10S','10S','JS']
        cards = [user_held[0],user_held[1],user_held[2],user_held[3],user_held[4]]
        #cards = ['10S','JS','QS','8S','9S']
        matches = self.count_cards(cards)
        #print(matches)
        card_names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        i = 0
        match_exists = False
        bruh = 0
        match_4 = False
        match_3 = False
        match_2 = False
        count_pairs = 0
        pair_value = 0
        for m in matches:
            if m==4:
                match_4 = True
            elif m==3:
               print("3 of a kind for",card_names[i])
               match_3 = True
            elif m==2:
                match_2 = True
                count_pairs += 1
                pair_value = int(self.card_switches(card_names[i]))
                print(pair_value,'is the pair value')
            else:
                bruh += 1
            i+=1
        if bruh<13:
            match_exists = True
        suit = self.check_for_suit(user_held)
        straight = self.check_for_straights(user_held)
        if straight[0] and straight[1] and suit:
            print("Royal Flush!")
            self.score = 132
        elif straight[0] and straight[1]:
            print("Royal Straight!")
            self.score = 120
        elif straight[0] and suit:
            print("Straight Flush!")
            self.score = straight[2]+104
        elif match_4:
            print("4 of a kind!")
            if user_held[0]==user_held[1]: self.score = int(self.card_switches(user_held[0]))+91
            else: self.score = int(self.card_switches(user_held[2]))+91
        elif straight[0]:
            print("Straight!")
            self.score = int(self.card_switches(user_held[4])) + 52
        elif suit:
            print("Flush!")
            self.score = int(self.card_switches(user_held[4])) + 65
        elif match_2 and match_3:
            print("That's a full house!")
            self.score = int(self.card_switches(user_held[4])) + 78
        elif match_3:
            print("3 of a kind!")
            self.score = int(self.card_switches(user_held[2])) + 39
        elif count_pairs == 2:
            print("2 pairs!")
            self.score = int(self.card_switches(user_held[3])) + 26
            print(pair_value)
        elif count_pairs == 1:
            print("1 pair!")
            self.score = int(self.card_switches(user_held[3])) + 13

        else:
            self.find_high_nothing(matches)
        print("Your score is:",self.score)
        root.mainloop()
poker = Poker()
poker.main()
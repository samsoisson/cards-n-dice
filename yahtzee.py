import random


class Yahtzee:

    def __init__(self):
        self.small_score = 0
        self.large_score = 0
        self.total_score = 0
        self.round_number = 0
        self.d1,self.d2,self.d3,self.d4,self.d5=0,0,0,0,0
        self.complete_list = []
        self.category_points = {"1s": -1, "2s": -1, "3s": -1, "4s": -1, "5s": -1,
                           "6s": -1, "3 of a kind": -1, "4 of a kind": -1,
                           "Full House": -1, "Small Straight": -1, "Large Straight": -1, "Chance": -1,
                           "Yahtzee": -1} #unused categories will be assigned -1
        self.complete_categories = 0

    def start(self):
        self.roll_dice()

    def roll_dice(self): #assigns random values to the dice for up to 3 rounds per category
        #if the dice are not held by the user, it will be rolled
        if self.d1 == 0:
            self.d1 = random.randint(1,6)
        if self.d2 == 0:
            self.d2 = random.randint(1,6)
        if self.d3 == 0:
            self.d3 = random.randint(1,6)
        if self.d4 == 0:
            self.d4 = random.randint(1,6)
        if self.d5 == 0:
            self.d5 = random.randint(1,6)
        dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
        self.round_number += 1
        print("Rolling dice (Round",self.round_number,"/ 3)")
        for die in dice: #prints dice numbers
            print(die)
        self.hold()

    def hold(self): #prompts the user to hold any dice
        if self.round_number==3: #if the user is on round 3, the score will be calculated and the user cannot hold any dice
            self.find_score()
        else:
            cont = input("Would you like to continue rolling? (y/n) ")
            if cont != 'n': #if the user wants to keep rolling
                num_hold = input("Would you like to hold any dice? (y/n) ")
                if num_hold == "y":
                    hd1 = input("Hold "+ str(self.d1)+"? (y/n) ")
                    if hd1 != 'y': # if the user doesn't want to hold the die, the value will reset to 0 to make it random on the next roll
                        self.d1=0
                    hd2 = input("Hold " + str(self.d2) + "? (y/n) ")
                    if hd2 != 'y':
                        self.d2 = 0
                    hd3 = input("Hold " + str(self.d3) + "? (y/n) ")
                    if hd3 != 'y':
                        self.d3 = 0
                    hd4 = input("Hold " + str(self.d4) + "? (y/n) ")
                    if hd4 != 'y':
                        self.d4 = 0
                    hd5 = input("Hold " + str(self.d5) + "? (y/n) ")
                    if hd5 != 'y':
                        self.d5 = 0
                else: #if the user doesn't want to hold any dice, all values will be reset to 0
                    self.d1,self.d2,self.d3,self.d4,self.d5=0,0,0,0,0
                self.roll_dice()
            else: #if the user doesn't want to roll anymore, the scores will be calculated
                self.find_score()

    def find_score(self): # calculates different scores based on the dice
            dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
            sum=0 # sum is used in 3 of a kind, 4 of a kind, and Chance if applicable
            for die in dice:
                sum+=die
            ones = dice.count(1)
            twos = dice.count(2)
            threes = dice.count(3)
            fours = dice.count(4)
            fives = dice.count(5)
            sixes = dice.count(6)
            counts = [ones,twos,threes,fours,fives,sixes]  # list of amount in each number 1-6
            # amounts converted into corresponding point values
            twos*=2
            threes*=3
            fours*=4
            fives*=5
            sixes*=6

            # if the categories are unused, the values will update to the current set of dice
            if self.category_points["1s"] == -1:
                self.category_points["1s"] = ones
            if self.category_points["2s"] == -1:
                self.category_points["2s"] = twos
            if self.category_points["3s"] == -1:
                self.category_points["3s"] = threes
            if self.category_points["4s"] == -1:
                self.category_points["4s"] = fours
            if self.category_points["5s"] == -1:
                self.category_points["5s"] = fives
            if self.category_points["6s"] == -1:
                self.category_points["6s"] = sixes

            # used to determine qualification for categories like Yahtzee, 3 of a kind, 4 of a kind, Full House, and many more
            singles=0
            doubles=0
            triples=0
            quadruples=0
            quintuples=0
            for count in counts:
                if count>=1:
                    singles+=1
                if count>=2:
                    doubles+=1
                if count>=3:
                    triples+=1
                if count>=4:
                    quadruples+=1
                if count==5:
                    quintuples+=1

            #these values are changed from 0 if they qualify
            oak3 = 0 # 3 of a kind
            oak4 = 0 # 4 of a kind
            full_house = 0
            smst = 0 #small straight
            lgst = 0 #large straight
            chance = sum
            yahtzee = 0
            if triples: oak3 = sum # 3 of a kind
            if quadruples: oak4 = sum # 4 of a kind
            if quintuples==1: yahtzee = 50 # 5 of a kind
            if triples and doubles==2: full_house = 25 # a 3 of a kind and a different 2 of a kind
            if singles == 5 and ((twos and not ones) or (ones and not sixes)): lgst = 40 # 2,3,4,5,6 or 1,2,3,4,5
            if singles >= 4 and threes and fours and ((twos and (ones or sixes)) or (fives and (twos or sixes))): smst = 30 # 1,2,3,4 or 2,3,4,5 or 3,4,5,6

            # if the categories are unused, the values will update to the current set of dice
            if self.category_points["3 of a kind"] == -1: self.category_points["3 of a kind"] = oak3
            if self.category_points["4 of a kind"] == -1: self.category_points["4 of a kind"] = oak4
            if self.category_points["Full House"] == -1: self.category_points["Full House"] = full_house
            if self.category_points["Small Straight"] == -1: self.category_points["Small Straight"] = smst
            if self.category_points["Large Straight"] == -1: self.category_points["Large Straight"] = lgst
            if self.category_points["Chance"] == -1: self.category_points["Chance"] = chance
            if self.category_points["Yahtzee"] == -1: self.category_points["Yahtzee"] = yahtzee

            for key,value in self.category_points.items():
                    print(key,value) #prints categories with their corresponding points
            category_not_chosen = True
            while category_not_chosen: # loop to ensure the user selects a valid, unused category
                choice = input("Type the category you would like to choose: ")
                if choice in self.category_points and choice not in self.complete_list: # if 'choice' is a category and 'choice' is not used
                    category_not_chosen = False
                    self.complete_categories += 1
                else:
                    print("Please select an unused category.")
            new_points = self.category_points[choice]
            print("The point value is",new_points)
            if choice in ["1s","2s","3s","4s","5s","6s"]: # adds to subscore if applicable
                print("score added to small_score:",choice)
                self.small_score += new_points
            else: # adds to upper score if applicable
                self.large_score += new_points
            self.complete_list.append(choice) # used to check if the category has already been used
            for key in self.category_points:
                self.category_points[key] = -1
            self.category_points[choice] = new_points
            print(self.category_points,new_points)
            if self.complete_categories < 13: # if not all the categories are completed, the game will continue, resetting the dice and round number to 0
                print("Your current score is",self.small_score+self.large_score)
                self.d1=self.d2=self.d3=self.d4=self.d5=0
                self.round_number = 0
                self.roll_dice()
            else:
                if self.small_score >= 63: self.small_score += 35 # adds bonus if applicable
                print("Your subscore is:",self.small_score)
                print("Your upper score is:",self.large_score)
                print("Your total score is:",self.small_score+self.large_score)
                print("...Game over...")


game = Yahtzee()
game.start()



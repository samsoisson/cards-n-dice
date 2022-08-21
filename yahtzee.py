import random
from tkinter import *
from PIL import Image, ImageTk

class Yahtzee:

    def __init__(self):
        self.small_score = 0  # score between 1s,2s,3s,4s,5s,and 6s
        self.large_score = 0  # score from 3 of a kind to Yahtzee
        self.total_score = 0  # total of small score and large score, as well as the 35 pt bonus if achieved
        self.round_number = 0  # the user can only roll 3 times, so this prevents the user from rolling too much
        self.d1,self.d2,self.d3,self.d4,self.d5=0,0,0,0,0  # values of the dice from 1 to 6
        self.complete_list = []  # list of complete categories like "Chance","1s". this list will be checked to find which categories have not been used
        self.category_points = {"1s": -1, "2s": -1, "3s": -1, "4s": -1, "5s": -1,
                           "6s": -1, "3 of a kind": -1, "4 of a kind": -1,
                           "Full House": -1, "Small Straight": -1, "Large Straight": -1, "Chance": -1,
                           "Yahtzee": -1}  # stores categories and their points here. the values of -1 will be updated once the user is done rolling
        self.complete_categories = 0  # once this reaches 13, the game will end because all the categories have been used
        self.user_held = [0,0,0,0,0] # the dice that the user holds. if the user doesn't hold, the dice will default to 0 and be rerolled
        self.roll_button = Button(text="roll again",width=7,height=3,command=lambda: self.roll_dice(),bg='black',fg='green',font='ROMAN') # rerolls dice
        self.roll_button.grid(row=1,column=0,padx=500)
        self.end_button = Button(text="end turn", bg='black',fg='red',font='ROMAN',command=lambda: self.find_score(),width=7,height=3)  # ends turn and has user select category
        self.end_button.grid(row=1,column=1)
        self.score_label = Label(text="score: "+str(self.total_score),bg='black',fg='yellow',font='ROMAN') # displays current score and updates every round
        self.score_label.grid(row=0,column=1,pady=75)

        # when selected, the following dice will be held. button properties initialized in self.roll_dice()
        self.dice1 = Button()
        self.dice2 = Button()
        self.dice3 = Button()
        self.dice4 = Button()
        self.dice5 = Button()
        #self.one_image = Image.open("dice1.png")
        #self.one_image.pack()

    def start(self):
        self.roll_dice()

    def roll_dice(self): #assigns random values to the dice for up to 3 rounds per category
        #if the dice are not held by the user, it will be re-rolled
        self.round_number += 1

        if self.round_number==3: # removes Roll Button to stop the user from rolling more than 3 times
            self.roll_button['state']=DISABLED


        self.round_label = Label(text=("Rolling dice (Round " + str(self.round_number) + "/ 3)"),bg='black',fg='cyan',font='ROMAN')  # needs to be re-displayed every time to update the round number
        self.round_label.grid(row=0, column=0, padx=20, pady=20)
        # if the dice are not held, their value is 0. in this case, they will be re-rolled
        if self.user_held[0] == 0:
            self.d1 = random.randint(1,6)
        if self.user_held[1] == 0:
            self.d2 = random.randint(1,6)
        if self.user_held[2] == 0:
            self.d3 = random.randint(1,6)
        if self.user_held[3] == 0:
            self.d4 = random.randint(1,6)
        if self.user_held[4] == 0:
            self.d5 = random.randint(1,6)
        list_held = []
        def add_held_list(roll,num):  # adds each die roll selected to the held list, and disables which buttons were pressed
            self.user_held[num-1] = roll
            match num:
                case 1:self.dice1['state'] = DISABLED
                case 2:self.dice2['state'] = DISABLED
                case 3:self.dice3['state'] = DISABLED
                case 4:self.dice4['state'] = DISABLED
                case 5:self.dice5['state'] = DISABLED

        # removes previous dice rolls before displaying the new dice
        self.dice1.destroy()
        self.dice2.destroy()
        self.dice3.destroy()
        self.dice4.destroy()
        self.dice5.destroy()
        photo = PhotoImage(file = r"dice1.png")
        #photoimage = photo.subsample(6, 6)
        img1 = PhotoImage(file="dice1.png",width=100,height=100)
        img1Btn = Button(image=img1,bg='black')
        img1Btn.image = img1

        img2 = PhotoImage(file="dice2.png", width=100, height=100 )
        img2Btn = Button(image=img2, bg='black')
        img2Btn.image = img2

        img3 = PhotoImage(file="dice3.png", width=100, height=100)
        img3Btn = Button(image=img3, bg='black')
        img3Btn.image = img3

        img4 = PhotoImage(file="dice4.png", width=100, height=100)
        img4Btn = Button(image=img4, bg='black')
        img4Btn.image = img4

        img5 = PhotoImage(file="dice5.png", width=100, height=100)
        img5Btn = Button(image=img5, bg='black')
        img5Btn.image = img5

        img6 = PhotoImage(file="dice6.png", width=100, height=100)
        img6Btn = Button(image=img6, bg='black')
        img6Btn.image = img6

        photo_list = [img1,img2,img3,img4,img5,img6]

        d1image= photo_list[self.d1-1]
        d2image = photo_list[self.d2-1]
        d3image = photo_list[self.d3-1]
        d4image = photo_list[self.d4-1]
        d5image = photo_list[self.d5-1]

        self.dice1 = Button(image = d1image,command=lambda: add_held_list(self.d1,1))
        self.dice1.grid(row=2,column=0,pady=20)
        self.dice2 = Button(image=d2image,text=str(self.d2), command=lambda: add_held_list(self.d2,2))
        self.dice2.grid(row=3, column=0,pady=20)
        self.dice3 = Button(image=d3image,text=str(self.d3), command=lambda: add_held_list(self.d3,3))
        self.dice3.grid(row=4, column=0,pady=20)
        self.dice4 = Button(image=d4image,text=str(self.d4), command=lambda: add_held_list(self.d4,4))
        self.dice4.grid(row=5, column=0,pady=20)
        self.dice5 = Button(image=d5image,text=str(self.d5), command=lambda: add_held_list(self.d5,5))
        self.dice5.grid(row=6, column=0,pady=20)


    def find_score(self): # calculates different scores based on the dice
        self.roll_button.destroy()
        self.end_button.destroy()
        self.round_label.destroy()
        self.round_label = Label(text=("Selecting category..."),bg='black',fg='cyan',font='ROMAN') # label replaces the "Rolling dice" label
        self.round_label.grid(row=0, column=0, padx=442,pady=75)

        self.dice1.grid(row=1, column=0, pady=20)
        self.dice2.grid(row=2, column=0, pady=20)
        self.dice3.grid(row=3, column=0, pady=20)
        self.dice4.grid(row=4, column=0, pady=20)
        self.dice5.grid(row=5, column=0, pady=20)

        dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
        sum=0 # sum is used in 3 of a kind, 4 of a kind, and Chance if applicable
        for die in dice: # finds sum of all dice
            sum+=die

        # count of numbers 1-6
        ones = dice.count(1)
        twos = dice.count(2)
        threes = dice.count(3)
        fours = dice.count(4)
        fives = dice.count(5)
        sixes = dice.count(6)

        counts = [ones,twos,threes,fours,fives,sixes]  # list of amount in each number 1-6, used later for upper score

        # counts converted into corresponding point values
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

        # these values are changed from 0 if they qualify
        oak3 = 0  # 3 of a kind
        oak4 = 0  # 4 of a kind
        full_house = 0  # full house
        smst = 0  # small straight
        lgst = 0  # large straight
        chance = sum  # chance
        yahtzee = 0   # yahtzee

        if triples: oak3 = sum # 3 of a kind
        if quadruples: oak4 = sum # 4 of a kind
        if quintuples==1: yahtzee = 50 # 5 of a kind
        if triples and doubles==2: full_house = 25 # a 3 of a kind and a different 2 of a kind
        if singles == 5 and ((twos and not ones) or (ones and not sixes)): lgst = 40  # 2,3,4,5,6 or 1,2,3,4,5
        if singles >= 4 and threes and fours and ((twos and (ones or sixes)) or (fives and (twos or sixes))): smst = 30  # 1,2,3,4 or 2,3,4,5 or 3,4,5,6

        # if the categories are unused, the values will update to the current set of dice
        self.category_points["3 of a kind"] = oak3
        self.category_points["4 of a kind"] = oak4
        self.category_points["Full House"] = full_house
        self.category_points["Small Straight"] = smst
        self.category_points["Large Straight"] = lgst
        self.category_points["Chance"] = chance
        self.category_points["Yahtzee"] = yahtzee

        # used to remove buttons later if they have been displayed
        oneBool = twoBool = threeBool = fourBool = fiveBool = sixBool = oak3Bool = oak4Bool = full_houseBool = smstBool = lgstBool = chanceBool = yahtzeeBool = False

        # displays buttons if the category has not been selected

        category = "1s"
        if category not in self.complete_list:
            oneBool=True
            ones_button = Button(text=category, command=lambda: add_score("1s", ones),bg='black',fg='red',font='ROMAN')
            ones_button.grid(row=1,column=3)
            ones_label = Label(text=str(ones),bg='black',fg='red',font='ROMAN')
            ones_label.grid(row=1,column=4,padx=20)

        category = "2s"
        if category not in self.complete_list:
            twoBool=True
            twos_button = Button(text=category, command=lambda: add_score("2s", twos),bg='black',fg='orange',font='ROMAN')
            twos_button.grid(row=1,column=5)
            twos_label = Label(text=str(twos),bg='black',fg='orange',font='ROMAN')
            twos_label.grid(row=1, column=6,padx=50)

        category = "3s"
        if category not in self.complete_list:
            threeBool=True
            threes_button = Button(text=category, command=lambda: add_score("3s", threes),bg='black',fg='yellow',font='ROMAN')
            threes_button.grid(row=1,column=7)
            threes_label = Label(text=str(threes),bg='black',fg='yellow',font='ROMAN')
            threes_label.grid(row=1, column=8,padx=50,pady=50)

        category = "4s"
        if category not in self.complete_list:
            fourBool=True
            fours_button = Button(text=category, command=lambda: add_score("4s", fours),bg='black',fg='green',font='ROMAN')
            fours_button.grid(row=2,column=3,padx=30)
            fours_label = Label(text=str(fours),bg='black',fg='green',font='ROMAN')
            fours_label.grid(row=2, column=4,padx=30)

        category = "5s"
        if category not in self.complete_list:
            fiveBool=True
            fives_button = Button(text=category, command=lambda: add_score("5s", fives),bg='black',fg='blue',font='ROMAN')
            fives_button.grid(row=2,column=5,padx=30)
            fives_label = Label(text=str(fives),bg='black',fg='blue',font='ROMAN')
            fives_label.grid(row=2, column=6,padx=30)

        category = "6s"
        if category not in self.complete_list:
            sixBool=True
            sixes_button = Button(text=category, command=lambda: add_score("6s", sixes),bg='black',fg='purple',font='ROMAN')
            sixes_button.grid(row=2,column=7,padx=30)
            sixes_label = Label(text=str(sixes),bg='black',fg='purple',font='ROMAN')
            sixes_label.grid(row=2, column=8,padx=30)

        category = "3 of a kind"
        if category not in self.complete_list:
            oak3Bool=True
            oak3_button = Button(text=category, command=lambda: add_score("3 of a kind", oak3),bg='black',fg='red',font='ROMAN')
            oak3_button.grid(row=3,column=3,padx=30)
            oak3_label = Label(text=str(oak3),bg='black',fg='red',font='ROMAN')
            oak3_label.grid(row=3, column=4,padx=30)

        category = "4 of a kind"
        if category not in self.complete_list:
            oak4Bool=True
            oak4_button = Button(text=category, command=lambda: add_score("4 of a kind", oak4),bg='black',fg='orange',font='ROMAN')
            oak4_button.grid(row=3,column=5,padx=30)
            oak4_label = Label(text=str(oak4),bg='black',fg='orange',font='ROMAN')
            oak4_label.grid(row=3, column=6,padx=30)

        category = "Full House"
        if category not in self.complete_list:
            full_houseBool=True
            full_house_button = Button(text=category, command=lambda: add_score("Full House", full_house),bg='black',fg='yellow',font='ROMAN')
            full_house_button.grid(row=3,column=7,padx=30)
            full_house_label = Label(text=str(full_house),bg='black',fg='yellow',font='ROMAN')
            full_house_label.grid(row=3, column=8,pady=50,padx=30)

        category = "Small Straight"
        if category not in self.complete_list:
            smstBool=True
            smst_button = Button(text="Sm. Straight", command=lambda: add_score("Small Straight", smst),bg='black',fg='green',font='ROMAN')
            smst_button.grid(row=4,column=3,padx=30)
            smst_label = Label(text=str(smst),bg='black',fg='green',font='ROMAN')
            smst_label.grid(row=4, column=4,padx=30)

        category = "Large Straight"
        if category not in self.complete_list:
            lgstBool=True
            lgst_button = Button(text="Lg. Straight", command=lambda: add_score("Large Straight", lgst),bg='black',fg='blue',font='ROMAN')
            lgst_button.grid(row=4,column=5,padx=30)
            lgst_label = Label(text=str(lgst),bg='black',fg='blue',font='ROMAN')
            lgst_label.grid(row=4, column=6,padx=30)

        category = "Chance"
        if category not in self.complete_list:
            chanceBool=True
            chance_button = Button(text=category, command=lambda: add_score("Chance", chance),bg='black',fg='purple',font='ROMAN')
            chance_button.grid(row=4,column=7,padx=30)
            chance_label = Label(text=str(chance),bg='black',fg='purple',font='ROMAN')
            chance_label.grid(row=4, column=8,pady=50,padx=30)

        category = "Yahtzee"
        if category not in self.complete_list:
            yahtzeeBool=True
            yahtzee_button = Button(text=category, command=lambda: add_score("Yahtzee", yahtzee),bg='black',fg='white',font='ROMAN')
            yahtzee_button.grid(row=5,column=5,padx=30)
            yahtzee_label = Label(text=str(yahtzee),bg='black',fg='white',font='ROMAN')
            yahtzee_label.grid(row=5, column=6,padx=30)

        def add_score(category,points):  # adds points to the category selected
            self.complete_list.append(category)
            if category in ["1s","2s","3s","4s","5s","6s"]:
                self.small_score += points
            else:
                self.large_score += points
            self.total_score = self.large_score + self.small_score
            self.score_label.destroy()

            # if the buttons were displayed, they will now be removed from the screen
            if oneBool:
                ones_button.destroy()
                ones_label.destroy()
            if twoBool:
                twos_button.destroy()
                twos_label.destroy()
            if threeBool:
                threes_button.destroy()
                threes_label.destroy()
            if fourBool:
                fours_button.destroy()
                fours_label.destroy()
            if fiveBool:
                fives_button.destroy()
                fives_label.destroy()
            if sixBool:
                sixes_button.destroy()
                sixes_label.destroy()
            if oak3Bool:
                oak3_button.destroy()
                oak3_label.destroy()
            if oak4Bool:
                oak4_button.destroy()
                oak4_label.destroy()
            if full_houseBool:
                full_house_button.destroy()
                full_house_label.destroy()
            if smstBool:
                smst_button.destroy()
                smst_label.destroy()
            if lgstBool:
                lgst_button.destroy()
                lgst_label.destroy()
            if chanceBool:
                chance_button.destroy()
                chance_label.destroy()
            if yahtzeeBool:
                yahtzee_button.destroy()
                yahtzee_label.destroy()

            self.dice1.destroy()
            self.dice2.destroy()
            self.dice3.destroy()
            self.dice4.destroy()
            self.dice5.destroy()

            self.complete_categories += 1
            if self.complete_categories == 13:  # if all categories have been used, the game ends
                self.round_label.destroy()
                self.roll_button.destroy()
                self.end_button.destroy()
                self.score_label.destroy()
                space = Label(text='The game has concluded.',bg='#6C0A0A',fg='#6C0A0A',width=23,height=23)
                space.grid(column=0,row=0)
                gameover_label = Label(text="\tGame over!\t",bg='black',fg='white',font='ROMAN')
                gameover_label.grid(row=0, column=0,pady=40)
                results_label = Label(text='\tYour results:\t',bg='black',fg='red',font='ROMAN')
                results_label.grid(row=0,column=2,pady=40,)
                self.dice1.destroy()
                self.dice2.destroy()
                self.dice3.destroy()
                self.dice4.destroy()
                self.dice5.destroy()
                subscore_label = Label(text="Subscore: " + str(self.small_score) + " pts",bg='black',fg='purple',font='ROMAN')
                subscore_label.grid(column=0,row=2,pady=20)
                if self.small_score >= 63:
                    self.small_score += 35
                    bonus_label = Label(text="Bonus achieved! +35 pts",bg='black',fg='cyan',font='ROMAN',pady=20)
                else:
                    bonus_label = Label(text="Bonus not achieved...",bg='black',fg='yellow',font='ROMAN')
                bonus_label.grid(column=0,row=3,pady=20)
                upper_label = Label(text="Upper score: " + str(self.large_score) + " pts",bg='black',fg='orange',font='ROMAN')
                upper_label.grid(column=2,row=2,pady=20)
                total_label = Label(text="Total score: " + str(self.small_score + self.large_score) + " pts",bg='black',fg='white',font='ROMAN')
                total_label.grid(column=2,row=3,pady=20)
                play_again = Button(text="play again", command=lambda: self.start(),bg='black',fg='green',font='ROMAN')
                play_again.grid(column=0,row=4,pady=20)
                end = Button(text="end session", command=lambda: root.destroy(),bg='black',fg='red',font='ROMAN')
                end.grid(column=2,row=4,pady=20)
                spac = Label(text='The game has concluded.', bg='#6C0A0A', fg='#6C0A0A')
                spac.grid(column=2)

            else:
                # resets dice and user_held for the next round
                self.d1=self.d2=self.d3=self.d4=self.d5=0
                self.user_held = [0,0,0,0,0]
                self.roll_button = Button(text="roll again", width=7, height=3, command=lambda: self.roll_dice(),
                                          bg='black', fg='green', font='ROMAN')  # rerolls dice
                self.roll_button.grid(row=1, column=0, padx=500)
                self.end_button = Button(text="end turn", bg='black', fg='red', font='ROMAN',command=lambda: self.find_score(), width=7,height=3)  # ends turn and has user select category
                self.end_button.grid(row=1, column=1)
                self.score_label = Label(text="score: " + str(self.total_score), bg='black', fg='yellow',font='ROMAN')  # displays current score and updates every round
                self.score_label.grid(row=0, column=1)

                self.round_number = 0
                self.roll_dice()

root = Tk()
root.title("Cards n Dice")
#root.geometry('1000x1600')
#root.attributes('-fullscreen',True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
#root.configure(bg='#6C0A0A')
bg = PhotoImage(file="background.png")
bg_label = Label(root,image=bg)
bg_label.place(x=0,y=0,relheight=1,relwidth=1)
game = Yahtzee()
game.start()
root.mainloop()
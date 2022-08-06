import random
class blackjack:
    def __init__(self):
        self.player_score = 0
        self.cpu_score = 0
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
    def assign_points(self,card,is_player):
        points = 0
        if card[0] == 'A' and is_player:
            while True:
                value = str(input("Would you like the ace to be worth 1 or 11? "))
                if value == '11':
                    points = 11
                    break
                elif value == '1':
                    points = 1
                    break
                else:
                    print("Enter 1 or 11!")
        elif card[0] == 'A':
            points = 11

        return points

    def main(self):
        cpu1 = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(cpu1)
        print(cpu1)
        cpu2 = self.cards[random.randint(0, len(self.cards)-1)]
        self.cards.remove(cpu2)
        print(cpu2)

        player1 = self.cards[random.randint(0, len(self.cards)-1)]
        self.cards.remove(player1)
        print(player1)
        player2 = self.cards[random.randint(0, len(self.cards)-1)]
        self.cards.remove(player2)
        print(player2)

        self.cpu_score += self.assign_points("AC",False)
        print(self.cpu_score)

game = blackjack()
game.main()
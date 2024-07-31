import random

class Card:
    suits = ["Spades","Diamonds","Clubs","Hearts"]
    card_and_values = {"Ace":[1,11],"Two":2, "Three":3, "Four":4, "Five":5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack":10,"Queen": 10, "King": 10}
 
    def Randomn_card(self):
        self.suit = random.choice(self.suits)        
        self.number = random.choice(list(self.card_and_values)) 


    def __repr__(self):
        info = "The card {} of {} has been drawn with a value of {}".format(self.number,self.suit,str(self.card_and_values[self.number]))
        return info

class Player:
    
    cards_value = 0  

    def __init__(self,name,money):
        self.name = name 
        self.money = money
    
    


    def __repr__(self):
        info = "Hello i am {} and i have £{} to bet".format(self.name,str(self.money)) 
        return info
      

    def Draw_a_card(self):
        card.Randomn_card()
        card_drawn = card
        print("{} has drawn a {} of {} with a value of {}".format(self.name,card_drawn.number,card_drawn.suit,str(card_drawn.card_and_values[card_drawn.number])))
        if card_drawn.number == "Ace":
            val = input("Choose between value 1 and 11? ")
            self.cards_value += int(val)
        else:    
          self.cards_value += card_drawn.card_and_values[card_drawn.number]
    
    def BlackJack_draw_two_cards(self):
     self.Draw_a_card()
     self.Draw_a_card()

    def Stick_or_twist(self):
        iterate = 0
        if self.cards_value == 21:
                    print("Blackjack for {}".format(self.name)) 
                    iterate = 1
        while iterate == 0:
            s_o_t = input("{}'s value of cards is {}, would you like to Stick or Twist? ".format(self.name,self.cards_value))
            if s_o_t == "twist":
                self.Draw_a_card()
                if self.cards_value == 21:
                    print("Blackjack!")
                    break
                if self.cards_value > 21:
                    print("{} has gone bust!".format(self.name))
                    self.cards_value = "bust"
                    break     
            elif s_o_t == "stick":
                break
            else: 
                print("Choose a value of stick or twist")

    def Winner(self,other_player):
        if self.cards_value == "bust" and other_player.cards_value != "bust":
            print("{} wins".format(other_player.name))
            self.money -= bet
            other_player.money += bet
        if self.cards_value != "bust" and other_player.cards_value == "bust":
            print("{} wins".format(self.name))
            self.money += bet
            other_player.money -= bet
        if self.cards_value != "bust" and other_player.cards_value != "bust":
            if self.cards_value > other_player.cards_value:
                print("{} wins".format(self.name)) 
                self.money += bet
                other_player.money -= bet
            if other_player.cards_value > self.cards_value:
                print("{} wins".format(other_player.name))
                self.money -= bet
                other_player.money += bet
            if other_player.cards_value == self.cards_value:
                print("We have a Tie!")
        if self.cards_value == "bust" and other_player.cards_value == "bust":
            print("We have a tie")  
                            


card = Card()
player1= Player(input("What is your name? "),int(input("How much would you like to deposit? ")))  
player2= Player(input("What is your name? "),int(input("How much would you like to deposit? "))) 
play_or_not = "yes"
order = 1 
while play_or_not == "yes": 
  print(player1)
  print(player2)
  player1.cards_value = 0
  player2.cards_value = 0
  bet= int((input("How much do you want to bet? ")))
  if player1.money < bet or player2.money < bet:
     print("You have bet more than you have")
     max_bet = min(player1.money,player2.money)
     bet = int((input("Bet an amount less than {}! ".format(max_bet))))
  print("We are betting {}".format(bet)) 
  if order % 2 == 1:
    player1.BlackJack_draw_two_cards()
    player2.BlackJack_draw_two_cards()
    player1.Stick_or_twist()
    player2.Stick_or_twist()
  if order % 2 == 0:
    player2.BlackJack_draw_two_cards()
    player1.BlackJack_draw_two_cards()
    player2.Stick_or_twist()
    player1.Stick_or_twist()

  player1.Winner(player2)
  if player1.money == 0:
    print("{} has no more money to bet".format(player1.name))
    buy_back = input("Would you like to buy back in? ")
    if buy_back == "yes":
        player1.money = int(("How much would you like to deposit?"))
    else: 
        break    
  if player2.money == 0:
    print("{} has no more money to bet".format(player2.name))
    buy_back = input("Would you like to buy back in? ")
    if buy_back == "yes":
        player2.money = int(input("How much would you like to deposit?"))
    else: 
        break
  order += 1  
  play_or_not = input("Do you want to play again?")  

print("After finishing {} is leaving with £{} with and {} is leaving with £{}!".format(player1.name,player1.money,player2.name,player2.money)) 

     


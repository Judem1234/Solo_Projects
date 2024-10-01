"""
Created on 15/07/2022 10:37

Author: Judem

After completing the object-oriented programming section of my Codecademy Computer Science Course, I decided to reinforce
that knowledge by completing a command line 2 player Blackjack game that focuses on object-oriented programming. 
"""

import random 

class Card:
    suits = ["Spades","Diamonds","Clubs","Hearts"]
    card_and_values = {"Ace":[1,11],"Two":2, "Three":3, "Four":4, "Five":5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack":10,"Queen": 10, "King": 10}
 
    def Randomn_card(self):
        """
        A simple function to draw a random card.
        """
        self.suit = random.choice(self.suits) #adds the suit to the card  
        self.number = random.choice(list(self.card_and_values)) #adds the string value of the numerical cards or face cards, e.g 'Jack'


    def __repr__(self):
        info = "The card {} of {} has been drawn with a value of {}".format(self.number,self.suit,str(self.card_and_values[self.number]))
        return info

class Player:
    """
    This class defines the player and everything a player can posses while playing a game of Blackjack.
    """
    cards_value = 0  

    def __init__(self,name,money):
        self.name = name 
        self.money = money
    
    def __repr__(self):
        info = "Hello i am {} and i have £{} to bet".format(self.name,str(self.money)) 
        return info
      
    def Draw_a_card(self):
        """
        This function draws a randomn card, lets the user know the card and assigns that card to the player. The slight problem with this
        function is that it should ask you to give the value for ace after you recieve the two cards.
        """
        card.Randomn_card()
        card_drawn = card
        print("{} has drawn a {} of {} with a value of {}".format(self.name,card_drawn.number,card_drawn.suit,str(card_drawn.card_and_values[card_drawn.number])))
        if card_drawn.number == "Ace": #The ace can have two values and the user can choose
            val = input("Choose between value 1 and 11? ")
            self.cards_value += int(val)
        else:    
          self.cards_value += card_drawn.card_and_values[card_drawn.number] #add the value of the card to the persons total card value
    
    def BlackJack_draw_two_cards(self):
     """
     Simple function to draw two cards. One shouldn't be able to draw two of the same cards, however that is possible in this funtion.
     """
     self.Draw_a_card()
     self.Draw_a_card()

    def Stick_or_twist(self):
        """
        Now we have drawn to cards, this function allows the user to either stick or twist, if there is a Blackjack, the player
        goes bust or the player sticks, we break the stick or twist loop.
        """
        iterate = 0
        if self.cards_value == 21: #If the first two draws resulted in a Blacjack, important to note that you can't go bust on the first turn (unless they choose two aces value 11)
                    print("Blackjack for {}".format(self.name)) 
                    iterate = 1
        while iterate == 0:
            s_o_t = input("{}'s value of cards is {}, would you like to Stick or Twist? ".format(self.name,self.cards_value)) #This lets the user know what he is on, to make a deciosion to stick or twist
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
                print("Choose a value of stick or twist") #If the user didn't stick or twist via a false input, they will be asked to input again.

    def Winner(self,other_player): 
        """
        This function compares the two players scores and outputs who wins the round, whoever wins will receive the money they bet
        and the loser will lose it.
        """
        if self.cards_value == "bust" and other_player.cards_value != "bust": #If one player goes bust and the other isn't then the other player automatically wins 
            print("{} wins".format(other_player.name))
            self.money -= bet
            other_player.money += bet
        if self.cards_value != "bust" and other_player.cards_value == "bust":
            print("{} wins".format(self.name))
            self.money += bet
            other_player.money -= bet
        if self.cards_value != "bust" and other_player.cards_value != "bust": #If both aren't bust, we compare their scores and see whos is higher
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
        if self.cards_value == "bust" and other_player.cards_value == "bust": #If both are bust then it is a tie
            print("We have a tie")  
                            


card = Card()
player1= Player(input("What is your name? "),int(input("How much would you like to deposit? ")))  
player2= Player(input("What is your name? "),int(input("How much would you like to deposit? "))) 
play_or_not = "yes" #defines whether or not the players want to play or not
order = 1 #defines which round we are in
while play_or_not == "yes": 
  print(player1)
  print(player2)
  player1.cards_value = 0
  player2.cards_value = 0
  bet= int((input("How much do you want to bet? ")))
  if player1.money < bet or player2.money < bet: #Makes sure the bet is not over the deposited money
     print("You have bet more than you have")
     max_bet = min(player1.money,player2.money)
     bet = int((input("Bet an amount less than {}! ".format(max_bet))))
  print("We are betting {}".format(bet)) 
  if order % 2 == 1: #Makes sure that in the first round, player 1 draws first and in the next player 2 draws first, and so on
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
  if player1.money == 0: #This gives a player the ability to buy back in if they are out of money
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
  play_or_not = input("Do you want to play again?") #If the pair don't want the game to continue, they can end the game here

print("After finishing {} is leaving with £{} with and {} is leaving with £{}!".format(player1.name,player1.money,player2.name,player2.money)) #This shows the final outcome from playing the rounds of Blackjack.

     


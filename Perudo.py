"""
Created on 02/09/2024 11:10 2024

Author: Judem

When I was on holiday playing perudo, I questioned whether it would be possible to simulate all 
the possible scenarios to obtain odds to help with your decision whether to call it or go higher
so that if the odds were much higher or lower than 0.5 then you could make a relativley confident
decision. 
"""

def multlist(lst):
   """
   A simple function to help later that takes all the elements of a list and multiplies them together.
   """
   for i in range(len(lst)):
            if i == 0:
               mult_of_prob = lst[i]
            else:
               mult_of_prob = mult_of_prob * lst[i]
   return mult_of_prob
          
def listmaker(n,bottom,top,addlst = [],output = []):
  """
  This function generates all possible list of length n ranging from numbers bottom to top. I chose 
  a recursive approach as this was the topic I struggled most with in my Codecademy Computer Science 
  course, so the best way to work on it is to try my own example.
  """
  ticker = 0
  elt = bottom
  while ticker != 1:
    if n == 1: # base case, ranges through the possible final indexed numbers with respect to the fixed rest of the list
      while elt < top + 1:  
        addlst.append(elt)
        other_list = []
        for i in addlst:
          other_list.append(i)
        output.append(other_list) 
        elt += 1 
        addlst.pop(-1)  
      return other_list  
    addlst.append(elt) #adding all the fixed non final indices before running through the final index
    listmaker(n-1,bottom,top,addlst,output)
    elt += 1
    addlst.pop(-1) #removes the number at that indice in preperation to add one the the number in that index
    if elt == top + 1: #here so that the numbers don't go over to top number
      ticker = 1 #this allows you to jump out of the while loop and return soemthing from the function, so one can break recursion   
  return output


def staircase123(lst):
    """
    A simple function that looks for any rolls that contain just a 123 staircase.
    """
    if lst.count(1) > 0 and lst.count(2) > 0 and lst.count(3) > 0 and lst.count(4) == 0:
        all_indices = [0,1,2,3,4]
        all_indices.remove(lst.index(1))
        all_indices.remove(lst.index(2))
        all_indices.remove(lst.index(3))
        return [True,all_indices[0],all_indices[1]]
    else:
        return [False]
    
def staircase1234(lst):
    """
    A simple function that looks for any rolls that contain just a 1234 staircase.
    """
    if lst.count(1) > 0 and lst.count(2) > 0 and lst.count(3) > 0 and lst.count(4) > 0 and lst.count(5) == 0:
        all_indices = [0,1,2,3,4]
        all_indices.remove(lst.index(1))
        all_indices.remove(lst.index(2))
        all_indices.remove(lst.index(3))
        all_indices.remove(lst.index(4))
        return [True,all_indices[0]]
    else:
        return [False]

def staircase12345(lst):
    """
    A simple function that looks for any rolls that contain a 12345 staircase.
    """
    if lst.count(1) > 0 and lst.count(2) > 0 and lst.count(3) > 0 and lst.count(4) > 0 and lst.count(5) > 0:
        return [True]
    else:
        return [False]


def prob_of_rolling_n_of_i_with_k_rolls(n,i,k):
    """
    This function outputs the probability of obtaining n of i with k rolls by simulating all the rolls with achieve it and then dividing by
    by the total number of possible outcomes, the probability.
    """
    no_of_rolls = 0
    if k > 1:
       all_poss_rolls = listmaker(k,1,6,[],[])
    elif k == 1: #I had a problem using listmaker when k was 1 so i decided to give it its own case for simplicity
       all_poss_rolls = []
       for i in range(1,7):
          all_poss_rolls.append([i])   
    else:
       return 1
    for roll in all_poss_rolls:
        if staircase123(roll)[0] == True: #The if and elif cases are for when some staircase is present so there are special rules, thus treated seperately
            count = 0
            if k == 5: 
              for idx in range(1,3):
                  if roll[staircase123(roll)[idx]] == 1 or roll[staircase123(roll)[idx]] == i:
                      count += 1    
              if count == n - 4:
                  no_of_rolls += 1
            if k == 4:
              if roll[staircase123(roll)[1]] == 1 or roll[staircase123(roll)[1]] == i:
                count += 1
              if count == n - 4:
                 no_of_rolls += 1
            if k == 3:
              if n == 4:
                 no_of_rolls += 1       
        elif staircase1234(roll)[0] == True:
            count = 0
            if k == 5:
              if roll[staircase1234(roll)[1]] == 1 or roll[staircase1234(roll)[1]] == i:
                  count += 1
              if count == n - 5:
                  no_of_rolls += 1
            if k == 4:
               if n == 5:
                  no_of_rolls += 1      
        elif staircase12345(roll)[0] == True:  
            if n == 6:
                no_of_rolls += 1
        else: #if there is no staircase it is pretty simple to check whether the roll has n amount of i
          if roll.count(1) + roll.count(i) == n:
              no_of_rolls += 1 
    return no_of_rolls / 6 ** k #returns the number of desired rolls divided by the total number of possible outcomes, the probability 

def prob_of_getting_n_of_i_with_k_players(what_need,number_needed,how_many_players,player_dice_list):
   """
   This function outputs the probability of rolling n of i with k players by simulating all possible scenarios where k players
   roll a combined number of i's which adds to n, then for each scenario finding the probability of that happening. Finally
   we sum up the probability of each scenario to get the total probability. The additional input players dice list is included
   as it tells you how many dice each player has for their turn.
   """
   probability = 0
   if how_many_players > 1:
     all_poss_scenarios = listmaker(how_many_players,0,6,[],[]) #the min and max of each perudo turn is 0 and 6
   elif how_many_players == 1:
     all_poss_scenarios = []
     for i in range(0,7):
       all_poss_scenarios.append([i])   
   for scenario in all_poss_scenarios:
      if sum(scenario) == what_need:  
         list_of_probs = []
         mult_of_prob = 0
         for i in range(len(player_dice_list)):
            prob = prob_of_rolling_n_of_i_with_k_rolls(scenario[i],number_needed,player_dice_list[i])
            list_of_probs.append(prob)
         probability += multlist(list_of_probs) #we multiply the probailities in the list to find the probaility of that scenario       
   return probability

def perudo():
   """
   This allows the user to set up the variables in the turn to calculate the odds in order to make a decision based on probability
   """
   prob = 0
   other_players = int(input('How many other players are there?')) 
   dice_number = int(input('What number are we playing with?'))
   dice_total = int(input('How many dice were called?'))
   your_dice = int(input('How many of the number do you have?'))
   how_many_dice_other_players = []
   for i in range(other_players):
      how_many_dice_other_players.append(int(input('How many dice does player {} have?'.format(i+1))))
   if dice_total-your_dice < ((1/2) * (6*other_players)) // 1: #The if and else is implemented to save time by not computing unnecessary calculations
       for i in range(dice_total-your_dice): #add all the less than scenarios and subtract it from 1
         prob += prob_of_getting_n_of_i_with_k_players(i,dice_number,other_players,how_many_dice_other_players)
       return "There is a {}% chance of there being atleast {} {}'s in the hand.".format((1 - prob)*100,dice_total,dice_number) 
   else:
       for i in range(dice_total-your_dice,6*other_players + 1): #add all the greater than scenarios up to the maximum
         prob += prob_of_getting_n_of_i_with_k_players(i,dice_number,other_players,how_many_dice_other_players)  
       return "There is a {}% chance of there being atleast {} {}'s in the hand.".format(prob*100,dice_total,dice_number)   
  
       
print(perudo())        
          
          
          
          
          
          
          
          
          
          
     


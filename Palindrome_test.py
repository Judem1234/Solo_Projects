"""
This is an example of one of the Euler problems I have completed. I am particularly happy with this one as I 
have added the ability to find the highest palindrome for any number input (not just when n = 4) whilst 
making some clever changes to save a lot of time!
"""
def is_palindrome(number):
    """
    A simple function to Return True if the input is a palindrome and False if not.
    """
    string_number = f'{number}'  
    if len(string_number) < 2:
        return True
    left_pointer = 0
    right_pointer = len(string_number) - 1
    while left_pointer < right_pointer:
        if string_number[left_pointer] == string_number[right_pointer]:
            left_pointer += 1
            right_pointer -= 1
        else:
            return False 
    return True   
 

def highest_palindrome(n):
     """
     This function takes input n and returns the highest palindrome which is the multiple of two
     numbers of length n. The plan is to range through second numbers with fixed first number 
     until we find a palindrome, then we set bounds so that we are not wasting unnecessary time,
     finally we compare each palindrome so we can find the highest one.
     """ 
     highest_poss = 9
     lower_bound = 0
     final_result = 0
     for i in range(1,n): #The highest possible number with n digits is n 9's
         highest_poss += 9*(10**i)
     first_number = highest_poss
     while first_number > lower_bound: #If first number falls below lower bound, we have already checked all the follwing multiples of first number times second number up to lower bound, and the rest are smaller
      second_number = highest_poss + 1
      while second_number > lower_bound:
          second_number += -1
          if second_number == 0:
              break
          if is_palindrome(first_number * second_number) == True:
              temporary_result = first_number * second_number
              if second_number > lower_bound: #We don't need the second number to go lower than the lower bound as the result on next iteration will be smaller
                lower_bound = second_number 
              break
      if temporary_result > final_result: #If the palindrom is higher we can replace the lower one
          final_result = temporary_result
      first_number += -1 #Iterate again with first number minus one
     return final_result 

print(highest_palindrome(4))



            
            

           
       

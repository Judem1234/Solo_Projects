def is_palindrome(number):
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
 

def highest_palindrome(number):
     highest_poss = 9
     first_lower_bound = 0
     second_lower_bound = 0
     final_result = 0
     itertations = 1
     for i in range(1,number):
         highest_poss += 9*(10**i)
     first_number = highest_poss
     while first_number > first_lower_bound:
      second_number = highest_poss + 1
      while second_number > second_lower_bound:
          second_number += -1
          if second_number == 0:
              break
          if is_palindrome(first_number * second_number) == True:
              temporary_result = first_number * second_number
              if second_number > second_lower_bound:
                second_lower_bound = second_number
                first_lower_bound = second_number
              break
      if temporary_result > final_result:
          final_result = temporary_result
          print(first_number,second_number)
      first_number += -1
      itertations += 1 
     return final_result

print(highest_palindrome(5))


            
            

           
       
print("Data Management Question Solver")

def factorials(x):
  '''
  This function does factorials

  Factorial is mainly used for permutation, this function replaces x! and does the same thing.
  


  Parameters
  ------------
  x : int
    The number that will be used in this function should be an integer because it is mainly used to solve for simple permutation questions, which will not include float numbers.
  
  Returns
  -------
  int
    The final value returned should be equivelant to x!, and thus it is a integer.
  
  Warnings 
  --------
  The integer entered should not be too big, otherwise the code will take foreover to run.

  Raises 
  ------
  TypeError
    If the input is not integer
  Exception
    If the calculation goes wrong
  
  '''
  if not isinstance(x, (int)):  
		  raise TypeError('Factorial expecting an int as input')
  answer = 1
  for i in range(1, x+1):
    answer*=i
  if not isinstance(answer, int):
		 raise Exception('Factorial calculation did not return a int value as expected.')
  return answer



def permutation(n,r):
  '''
  This function does permutations and it relies on the factorial function

  Permutation is used when we need to determine the number of ways we arrange a group of items 
  


  Parameters
  ------------
  n : int
    The number that will be used in this function should be an integer because it is mainly used to solve for simple permutation questions, which will not include float numbers.
  r : int
    The number that will be used in this function should be an integer because it is mainly used to solve for simple permutation questions, which will not include float numbers.
  
  Returns
  -------
  int
    The final value returned should be equivelant to n!/(n-r)!, and thus it is a integer.
  
  Warnings 
  --------
  The integer entered should not be too big, otherwise the code will take foreover to run.

  Raises 
  ------
  TypeError
    If the input is not an integer
  Exception
    If the calculation goes wrong
  
  '''
  if not isinstance(n, (int)):  
		  raise TypeError('Permutation expecting an int as input')
  if not isinstance(r, (int)):  
		  raise TypeError('Permutation expecting an int as input')
  if n < r:
    print("Not possible")
    return(0)
  else:
    R = factorials(n-r)
    n = factorials(n)
    NpickR = int(n/R)
  if not isinstance(NpickR, int):
		 raise Exception('Permutation calculation did not return a int value as expected.')
  return NpickR


def modifiedRuleOfSum(suit,card):
  '''
  This function finds the sum of the input

  Modified rule of sum is used when there is an overlap.
  


  Parameters
  ------------
  suit : str
    The input for this function must be a string because it is the name of one suit (Hearts, Diamonds, Spades, Hearts).
  card : str
    The input for cards must be a string as well, because in order to keep it consistent, a string input is required.
  
  Returns
  -------
  int
    The final value returned should be an integer because the function is used to count number of cards.
  
  Warnings 
  --------
  All input must be strings

  Raises 
  ------
  TypeError
    If the input is not a string
  Exception
    If the calculation goes wrong
  ValueError
        If the input does not exist in the function
  
  '''
  GeneralSet = ["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING", "FACECARDS"]
  CLUBS = ["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
  SPADES = ["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
  DIAMONDS = ["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
  HEARTS = ["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
  FACECARDS = ["JACK","QUEEN","KING"]
  numberOfCards = 0  
  overlap = 0 

  if not isinstance(suit, (str)):  
		  raise TypeError('modifiedRuleofSum expecting a str as input')
  if not isinstance(card, (str)):  
		  raise TypeError('modifiedRuleofSum expecting a str as input')
  if suit != 'CLUBS' and suit != 'SPADES' and suit != 'DIAMONDS' and suit != 'HEARTS':
      raise ValueError('Input value is not one of the four suits (CLUBS, SPADES, DIAMONDS, HEARTS)')
  if card not in GeneralSet:
      raise ValueError('Input value is not one of the element in the Genral Set')

  setOfSuit = set(locals()[suit])
  setOfFacecards = set(FACECARDS)
  if card == "FACECARDS":
    
     if setOfFacecards.intersection(setOfSuit):   
      overlap = overlap + 3
      numberOfCards = 4*(int(len(FACECARDS)))
  else:
    if card in locals()[suit]:
      overlap = overlap + 1
  
  suitNumber = len(locals()[suit])

  totals = suitNumber + numberOfCards - overlap
  if not isinstance(totals, int):
		 raise Exception('Modefied rule of sum calculation did not return a int value as expected.')
  return totals
 


print(factorials(5))
print(permutation(8,3))
print(modifiedRuleOfSum('SPADES','ACE'))

try:
    print(modifiedRuleOfSum("CLUBS",'FACECARDS'))
    print(modifiedRuleOfSum("CLUB","2"))
    print(modifiedRuleOfSum("SPADES",2))
except (TypeError,ValueError) as c:
    print('Something went wrong: ' + str(c))
except Exception as c:
    print('Something went wrong: ' + str(c))
else:
  print("Executing the Modified Rule of Sum function")


try:
    print(permutation(10,6))
    print(permutation(10,10))
    print(permutation("a0"))
    print(permutation(10.005,10))
except TypeError as a:
    print('Something went wrong: ' + str(a))
except Exception as a:
    print('Something went wrong: ' + str(a))
else:
  print("Executing the Permutation function")

try:
    print(factorials(8))
    print(factorials("a0"))
    print(factorials(10.005))
    print(factorials("hi"))
except TypeError as a:
    print('Something went wrong: ' + str(a))
except Exception as a:
    print('Something went wrong: ' + str(a))
else:
  print("Executing the x! function")


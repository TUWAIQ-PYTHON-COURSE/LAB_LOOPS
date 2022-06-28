'''
1) Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
2) Using a while loop and input , do the following :
Ask the the user : "what is the product of 7 * 24 ?"
check if the answer is right then exit the loop and print "You answered this Question correctly"
if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.

'''

# Using loops 
#using range 
from itertools import product


for x in range (45, 210, 1): # to get range from 45 to 210
       # to skip  a number of a sequance  
    if x == 100:
        continue  
    #to exit a loop , we use break 
    elif x == 205:
        break
    print(x)

#using while loop




while True:
    x = input("Enter the prodcut 7*24 =  ")
    if int(x) == 168:
      print("You answered this Question correctly")
      break
    else: 
        print(type(x))
        print("Your Answer is wrong try again..")
    


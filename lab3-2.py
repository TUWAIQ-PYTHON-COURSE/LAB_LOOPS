## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
from operator import truediv

for number in range(45,210):
    if number==100:
        continue
    elif number==205:
        break
    print(number)

    #Ask the the user : "what is the product of 7 * 24 ?"
    
while  True :
    x=int(input("what is the product of 7 * 24 ?")) 
    if x==168 :
      print("You answered this Question correctly")
      break
    else:
      print("try again")


    #check if the answer is right then exit the loop and print "You answered this Question correctly"
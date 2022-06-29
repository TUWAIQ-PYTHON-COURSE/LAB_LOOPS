''' 
1) Using range(), make a range from 45 to 210, 
using a for loop iterate over the sequence and print the elements.
 Skip the number 100 and break the loop at 205
 '''
for x in range(45, 210, 1):
    if x == 100:
        continue
    
    elif x == 205:
        break
    print(x)
'''
2) Using a while loop and input , do the following :
'''
while True :
    question = int(input("what is the product of 7 * 24 ?"))
    if question == 168:
        print("You answered this Question correctly")
        break
    print("Your Answer is wrong try again..")   
            





    

    

    
    
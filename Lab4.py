# 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205

for i in range(45 , 210):

    if i == 100:
        continue 
    elif i == 205:
        break 

    print(i)

    #Ask the the user : "what is the product of 7 * 24 ?"

    #check if the answer is right then exit the loop and print "You answered this Question correctly"
    #if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
    


    
while True :
    num= int(input("what is the product of 7 * 24 ?"))
    if num ==168:
        print("correct")
        break
    else:
        print("try again")
        

        
            
    




   
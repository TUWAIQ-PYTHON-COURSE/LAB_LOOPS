for num in range(45 , 210 ):
    if num == 100 :
        continue
    elif num == 205 :    
        break
    print(num)


while True:
    userAnswer = input("what is the product of 7 * 24 ?")
    
    if int(userAnswer) == 215:
        print("You answered this Question correctly")
        break
    if int(userAnswer) !=215:
        print("Your Answer is wrong try again..")
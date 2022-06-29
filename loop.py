for x in range(45,210):
   
    if x==100:
        continue
    elif x==205:
        break
    print(x)

correct_answer=168
user_answer=""
while correct_answer != user_answer:
    user_answer = int(input("what is the product of 7 * 24 ?"))
    if correct_answer != user_answer:
         print("Your Answer is wrong try again..")
print( "You answered this Question correctly")    
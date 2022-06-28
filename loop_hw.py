# Q1


for number in range(45, 211, 1):
    if number == 100:
        continue
    elif number == 205:
        break
    print(number)

# Q2
x : bool = True
while x:
    result : int = input("what is the product of 7 * 24 ?") 
    if int(result) == 168:
        condition = False
        break
    print("Your Answer is wrong try again..")

print("You answerd this Question correctly")

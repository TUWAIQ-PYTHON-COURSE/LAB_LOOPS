#[1]

for numbers in range(45,210,1):
    if numbers == 100:
        continue
    elif numbers == 205:
        break
    print(numbers)

#[2]
answer = int(input("What is the product of 7 * 24 ?"))

while answer > 0:
    if answer == 168:
        print("You answered this Question correctly")
        break
    
    elif answer != 168:
         print("Your Answer is wrong try again..")
         answer = int(input("What is the product of 7 * 24 ?"))
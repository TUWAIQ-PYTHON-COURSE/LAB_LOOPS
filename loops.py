

for letter in range(45, 210):

    if letter == 100:
        continue
    
    elif letter == 205:
        break
    print(letter)

answer = int(input('what is the product of 7 * 24?'))
while True:
    if answer == 168:
        print("You answered this Question correctly")
        break
    
    if answer != 168:
        print("Your Answer is wrong try again.. ")
        


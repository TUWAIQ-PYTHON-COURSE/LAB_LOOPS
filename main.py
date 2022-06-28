for x in range(45, 210):
    if x == 100:
        continue
    elif x == 205:
        break

    print(x)


while True:
    q = print("what is the product of 7 * 24 ?")
    a = input()

    if int(a) == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again")
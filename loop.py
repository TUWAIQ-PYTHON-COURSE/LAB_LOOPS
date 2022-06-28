for i in range(45, 210):
    if i == 100:
        continue
    if i == 205:
        break
    print(i)

def practice():
    print('what is the product of 7 * 24 ?')
    while True:
        try:
            num = int(input('Enter your answer : '))
            if num == 168:
                print('You answered this Question correctly')
                break
            if num != 168:
                print('Your Answer is wrong try again..')
        except:
            print('Please enter an integer number ')

practice()

xrange = (45, 210)



    

for letter in range(45, 210):

    #to exit a loop , we use break
    if letter == 100:
        continue

    
    elif letter == 201:
        break

    print(letter)




x: int = input("what is the product of 7 * 24 ?     :")


yy : int = 7
nn : int = 24
 
#xx = (yy*nn)


while int(x) == 7*24 :

    print("You answered this Question correctly")
    break

else:
    print("Your Answer is wrong try again..")


#else:
#print("Your Answer is wrong try again..")
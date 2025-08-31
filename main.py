import random
random_no=random.choice([-1,0,1])

'''
1 for snake
-1 for water
0 for gun
'''

you=input("Enter your choice:")
youdict={"s":1,"w":-1,"g":0}
younum=youdict[you]
print("Your Choice:", younum)
print("Computer Choice:", random_no)

if younum==random_no:
    print("It's a tie!")
else:
    if (younum==1 and random_no==-1) or (younum==0 and random_no==1) or (younum==-1 and random_no==0):
        print("You win!")
    elif (younum==0 and random_no==-1) or (younum==-1 and random_no==1) or (younum==1 and random_no==0)  :
        print("You lose!")
    else:
        print("Something went wrong")
        
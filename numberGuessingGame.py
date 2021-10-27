import random 
n=random.randint(1,9)
print("Take a guess between 1 to 9")
for i in range(1,6):
    print(i)
    guess=int(input("Enter your guess"))
    if(guess==n):
        print("Congratulations, You Win")
        break
    elif(guess>n):
        print("Your guess to high")
    else:
        print("Your guess is to low")

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess any no. from 1-10: "))
    guess_count+=1

    if guess == secret_number:
        print("You won")
        break

else:
    print("Better luck next time")
    
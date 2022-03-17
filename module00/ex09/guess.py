import random

if __name__ == "__main__":
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")
    target = random.randint(1, 100)
    count = 1
    while True:
        try:
            print("What's yout guess between 1 and 99?")
            value = input(">> ")
            if value == "exit":
                print("Goodbye!")
                break

            if value.isnumeric():
                value = int(value)
                if value == target:
                    if target == 42:
                        print("The answer to the ultimate question of life, the universe and everything is 42.")
                    if count == 1:
                        print("Congratulations, you got it in your first try!")
                    else:
                        print("Congratulations, you've got it!")
                        print("You won in {} attempts!".format(count))
                    break
                elif value < target:
                    print("Too low!")
                else:
                    print("Too high!")
            else:
                raise ValueError
        
        except ValueError:
            print("That's not a number.")
        
        count += 1

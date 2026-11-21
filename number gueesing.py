
import random

secret = random.randint(1,20)
maximum_Guess = 6
attemps = 0

while attemps<maximum_Guess:
    myGuess = int(input("MY input: "))

    if myGuess == secret:
        print(f"{secret} you guessed it congrats")
        break
    elif myGuess > secret:
        attemps +=1
        print(f"too high attemps:{attemps}")

    elif myGuess < secret:
        attemps +=1
        print(f"too low attemps:{attemps}")

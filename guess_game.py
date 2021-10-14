secret_word = "Victor"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
        print("This is your " + str(guess_count) + " try.")
    else:
            out_of_guesses = True

if not out_of_guesses:
    print("You Win!")
else:
    print("You lose!")

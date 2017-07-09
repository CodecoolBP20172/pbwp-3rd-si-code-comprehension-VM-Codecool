import random  # imports the random module, which contains a variety of things to do with random number generation

guessesTaken = 0  # making a "guessesTaken" global variable and assigning it to 0

print('Hello! What is your name?')  # printing out a sting for the user to see
myName = input()  # assigning myName to a user input

number = random.randint(1, 20)  # assigning "number" to a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# printing out well + the name what the user gave and I am thinking etc

while guessesTaken < 6:  # while guessesTaken variable is less then 6
    print('Take a guess.')  # printing out 'take a guess' for the user to see
    guess = input()  # the variable equals to user input (which should be a number otherwise it chrashes)
    guess = int(guess)  # changing user input into an integer

    guessesTaken += 1  # increasing variable by 1 (after every guessesTaken)

    if guess < number:  # if user input guess is less then the number we generated then:
        print('Your guess is too low.')  # then give a user a feedback about it (too low)

    if guess > number:  # if user input is higher then the number we generated then:
        print('Your guess is too high.')  # give a feedback to the user about it (too high)

    if guess == number:  # if the user input equals to the generated number then:
        break  # break out of the while loop

if guess == number:  # if user input guess equals to the generated number then :
    guessesTaken = str(guessesTaken)  # transorm guessesTaken from an integer into a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # show user 'Good job' + the name what you given to the program in the beggining, and also tell her/him
    # that how many guesses it took to get the number (it can be from 1-6)

if guess != number:  # if user input guess is not equals to the generated number (after 6 guesses) then:
    number = str(number)  # convert number into a string
    print('Nope. The number I was thinking of was ' + number)  # show the user what was the generated number

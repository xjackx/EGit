'''
Name:Ranbir Dixit
Program: Hangman
Version:1
Description: User has 10 tries to guess all the letters for a hard coded word
'''
word="trust"
#convert string to list
wordlist=list(word)
#list to hold the correct user input
correct_letters=[]
#list to hold all the user input
all_guesses=[]
#limit of the number of guesses allowed
guess = 10
print wordlist
#loop through the 10 allowed guesses; if word is found before all guesses used, break
while guess > 0:
    #validate user_input is in lower case
    user_guess=str(raw_input("guess a letter in the word: ")).lower()
    print "user guess: ",user_guess
    #check to see if the user_guess is in the word and update two lists, correct guesses and 
    for inputguess in user_guess:
        print "user guess in word ", user_guess
        correct_letters.append(user_guess)
        #search for occurence of index in word and update correct letters list
        #guessed_letter=word.index(user_guess)
#        print "guessed letter:", guessed_letter
#        correct_letters.append(user_guess)
#        all_guesses.append(user_guess)
        guess-=1
        print "you have", guess, "guesses left"
    else:
        print "_"
        all_guesses.append(user_guess)
        guess-=1
        print "you have", guess, "guesses left"
    print "all guesses:", all_guesses
    print "correct guesses",correct_letters

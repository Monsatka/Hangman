##Hangman game 

print("Let's play Hangman!")
print("You will get 15 attempts to guess the word ...")
print("The word alone is 13 characters long...")

guess = input("Try to guess the letter: ")
word = ["h", "a", "c", "k", "t", "o", "b", "e", "r", "f", "s"]

for i in range(15):
        guess = input("Try to guess the letter: ")
        if guess in word: 
                print("You have guessed the letter!")
                word.remove(guess)
        else: 
                print("You haven't guessed the letter!")
        
        if i < 13 and len(word) == 0:
                print("You have won!")
                break
        elif len(word) == 0:
                print("The guessed word was 'hacktoberfest'.")
        else:
                pass

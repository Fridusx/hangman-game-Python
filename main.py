import random
import art
import words


print(art.logo)
print(f"Your current stage {art.stages[6]}")
print("You have to guess the word that hidden. You have 6 lives)")

word = random.choice(words.word_list)
print(word)

storage = ""
main_storage = []
storage_correct_word = []

game_end = False

lives = 6

for hiden_word in range(len(word)):
    storage += "_"
print(f"Your hidden word is {storage}")

for correct_word in word:
    storage_correct_word += correct_word


while not game_end == True:
    guess = input("Write a letter: ")
    display = ""

    if guess in storage_correct_word and guess in main_storage:
        print("You have already guessed this letter. Be careful!")

    for list in word:
        if list == guess:
            display += guess
            main_storage += guess 

        elif list in main_storage:
            display += list
        else:
            display += "_"
    
    if guess not in storage_correct_word:
        print("That letter is not in the hidden word(")
        lives -= 1
    

    print(f"You cerrently have {lives}/6 lives")
    print(art.stages[lives])
    print(display)
            
    if "_" not in display:
        print("*************** You win! ***************")
        print(art.like)
        game_end = True
    if lives == 0:
        print(f"You lose! The correct word : {word}")
        game_end = True
    
   


    
    

    



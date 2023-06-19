from Hangman_art import stages, logo, end
print(logo)
import random
from Hangman_words import word_list
word = random.choice(word_list)

guess_list = []
for char in word:
  guess_list.append("_")

lives = 6
end_of_game = False
while(not end_of_game):
  guess = input("Enter your guess : ").lower()
  if guess in guess_list:
    print(f"You've already guessed {guess}")
  for i in range(len(word)):
    if guess == word[i]:
      guess_list[i] = guess
      
  if guess not in guess_list:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")


  if lives == 0:
    end_of_game = True
    print("You lose.")
  print(f"{' '.join(guess_list)}")

  if "_" not in guess_list :
    end_of_game = True
    print("You win. Congratulations!!!")

  
  print(stages[lives])

print(f"The word was {word}")
print(end)
print("The End")

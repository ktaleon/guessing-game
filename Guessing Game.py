import threading
import time

def timer ():
    global my_timer
    my_timer = 30

    for x in range(30):
        my_timer = my_timer - 1
        time.sleep(1)
    print("Out of time!")

countdown_thread =  threading.Thread(target = timer)
countdown_thread.start()

guess_word = ["cat", "dog", "fish", "bird","cow","goat","sheep"]
guesses = ""
x = 0
count = 0
print("WELCOME TO KARL'S GUESSING GAME!")
print("INSTRUCTIONS:")
print("You will have to guess a word that is predetermined by the system")
print("If you get it wrong 5 times the word to guess will change")
print("You only get 30 guesses")
print("Hint! The word is a name of an animal")

while guesses != guess_word[x]:
    guesses = str(input())
    guesses = guesses.lower()
    if guesses == guess_word[x]:
        print("Correct! Congratulations you won 1,000,000 pesos!")
    else:
        print("Try again!")

    count += 1

    if count % 5 == 0:
        x += 1
        if x == 4:
            x = 0
    if count == 30:
        print("Sorry try again later :(")
        break  
    if my_timer == 0:
        break
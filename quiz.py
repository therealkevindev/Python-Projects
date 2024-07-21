# lower() function is used to convert the string to lowercase
# even if the user write's it different CAPS.
# Example: anDroId => android || changes due to the lower() function

import time # => for the time.sleep() function

print("Hello, Welcome to my quiz game! 🚀")
print("This quiz is about computers!")

# Ask the user if they want to play or they don't want to
playing = input("Do you want to play my game 😁? (y/n): ")

# if condition to play.
if playing.lower() == "y": 
    print("Okay, Let's get started 😁🚀")

else:
    exit()

score = 0

question = input("What's full form of RAM? 🎮: ")

# Showing the program the correct answer.

if question.lower() == "random access memory":
    print("You got the the answer correct! 🚀")
    score += 1

else:
    print("Nice, Try but your answer is wrong 😭")




question = input("What's the most popular operating system used in phones? 📱: ")

# Showing the program the correct answer.

if question.lower() == "android":
    print("You got the the answer correct! 🚀")
    score += 1

else:
    print("Nice, Try but your answer is wrong 😭")




question = input("What's the most popular operating system used in servers💻?: ")

# Showing the program the correct answer.

if question.lower() == "linux":
    print("You got the the answer correct! 🚀")
    score += 1

else:
    print("Nice, Try but your answer is wrong 😭")

print("Okay, we have seen you're results!")
print("We are processing the score")

time.sleep(2)

print(f"You're score is {score} out of 3")
print("Thank you for playing my game!, 😁")

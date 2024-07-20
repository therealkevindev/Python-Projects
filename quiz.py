print("Welcome to my quiz game! 🦀")

playing = input("Do you want play my game? 🙋: ")

if playing.lower() != "yes":
    exit()

score = 0

print("Okay, Let's begin 😅")

question = input("What's the full form of CPU? 💻: ")

if question.lower() == "central processing unit":
    
    print("You got the correct answer 😁")
    score = score + 1

else:
    print("oh, that's incorrect 😖")

question = input("What's the full form of RAM? 💻: ")

if question.lower() == "random access memory":
    print("You got the correct answer 😁")
    score = score + 1

else:
    print("oh, that's incorrect 😖")

question = input("What's the full form of GPU? 💻: ")

if question.lower() == "graphics processing unit":
    print("You got the correct answer 😁")
    score = score + 1

else:
    print("oh, that's incorrect 😖")

print(f"You're total score is {score} out of 3")

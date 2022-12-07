
lives = 3
correctAnswer = 150

while lives > 0:
    answer = int(input("100 + 50 = " ))
    if answer == correctAnswer:
        print("YOU WON!")
        break
    else:
        lives = lives - 1
else:
    print("YOU LOSE!")

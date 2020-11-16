print("Hello, welcome to Arnold Schwarzenegger trivia! This is a game built following a tutorial on YouTube.")

ans = input("Are you ready to play (yes/no): ")
score = 0
total_q = 4

if ans.lower() == "yes":
    ans = input("1. What is Arnold Schwarzenegger's age? ")
    if ans == "73":
        score += 1
        print("Correct! He's still going strong!")
    else:
        print("Wrong!")

    ans = input("2. How many Mr Olympia titles did he win? ")
    if ans == "7":
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

    ans = input("3. How many Terminator movies are there? ")
    if ans == "2":
        score += 1
        print("Correct!")
    else:
        print("Wrong! Everything after T2 doesn't count because they are terrible.")

    ans = input("4. What state did he become governor of in 2003? ")
    if ans.lower() == "california":
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print("Thank you for playing, you got ",score," questions correct.")
mark = (score/total_q) * 100

print("Mark: ", mark)
print("Thanks to Tech with Tim for the tutorial!")





print("boolean quiz")

answer1 = int(input("question1: enter a number less than 10\n"))
print(answer1 < 10)

answer2 = int(input("question2: enter a number >= 5\n"))
print(answer2 >= 5)

answer3 = int(input("question3: enter 7\n"))
print(answer3 == 7)

answer4 = int(input("question4: enter a number not equal to 3\n"))
print(answer4 != 3)

answer5 = int(input("question5: enter a number <= 12\n"))
print(answer5 <= 12)

answer6 = int(input("question6: enter a number between 1 and 10\n"))
print(answer6 >= 1 and answer6 <= 10)

answer7 = int(input("question7: enter a number less than 0 or greater than 20\n"))
print(answer7 < 0 or answer7 > 20)

answer8 = int(input("question8: enter a number greater than 5 and less than 15\n"))
print(answer8 > 5 and answer8 < 15)

print("done")
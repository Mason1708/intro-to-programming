import random
leaderboard = []
while True:
    secret_number = random.randint(1, 100)
    print("\nGuess the number between 1 and 100")
    name = input("Enter your name: ")
    attempts = 0
    while True:
        guess = int(input("Guess: "))
        attempts += 1
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print(f"Correct! {attempts} attempts.")
            leaderboard.append((attempts, name))
            break
    leaderboard.sort()
    print("\n--- Leaderboard ---")
    for rank, (score, player) in enumerate(leaderboard, start=1):
        print(f"{rank}. {player} - {score} attempts")
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
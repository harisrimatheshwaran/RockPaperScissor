import gamemod as gm

user_name = input("Enter your name: ")
rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
    print(f"\n--- Round {i+1} ---")
    comp_choice = gm.computer()
    user_choice = gm.user()
    print(f"TINSON: {comp_choice}")
    print(f"{user_name}: {user_choice}")
    final = gm.result(comp_choice, user_choice)
    print(final)
    if i < rounds - 1:
        continue_game = input("Do you want to continue to the next round? (yes/no): ")
        if continue_game == 'no':
            break
wins=gm.final_result(user_name)
print("\n" + wins)

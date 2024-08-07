def draw(ch1, ch2):
    if ch1 == 1 and ch2 == 2:
        return 1


def game(op_1, op_2):
    rat = '__QQ\n()">'.split('\n')
    hunter = ' O \n/|\\\n/ \\'.split('\n')
    lion = ' /\_/\ \n( o.o )\n > ^ < '.split('\n')
    score_1 = 0
    score_2 = 0
    count = 1
    while count <= 5:
        print()
        print(f"Round {count}!")
        print(f"{op_1} {score_1} / {op_2} {score_2}")
        choice_1 = int(input(f"{op_1}'s choice (1/rat, 2/hunter and 3/lion): "))
        choice_2 = int(input(f"{op_2}'s choice (1/rat, 2/hunter and 3/lion): "))
        if choice_1 == 1:
            if choice_2 == 2:
                print(rat[0], end="      ")
                print(hunter[0])
                print(rat[1], end="  VS  ")
                print(hunter[1])
                print("   ", end="       ")
                print(hunter[2])
                score_1 += 1
            elif choice_2 == 3:
                print(rat[0], end="      ")
                print(lion[0])
                print(rat[1], end="  VS  ")
                print(lion[1])
                print("   ", end="       ")
                print(lion[2])
                score_2 += 1
            elif choice_2 == 1:
                print(rat[0], end="      ")
                print(rat[0])
                print(rat[1], end="  VS  ")
                print(rat[1])

        elif choice_1 == 2:
            if choice_2 == 1:
                print(hunter[0], end="      ")
                print(rat[0])
                print(hunter[1], end="  VS  ")
                print(rat[1])
                print(hunter[2])
                score_2 += 1
            elif choice_2 == 3:
                print(hunter[0], end="      ")
                print(lion[0])
                print(hunter[1], end="  VS  ")
                print(lion[1])
                print(hunter[2], end="      ")
                print(lion[2])
                score_1 += 1
            elif choice_2 == 2:
                print(hunter[0], end="      ")
                print(hunter[0])
                print(hunter[1], end="  VS  ")
                print(hunter[1])
                print(hunter[2], end="      ")
                print(hunter[2])
        elif choice_1 == 3:
            if choice_2 == 1:
                print(lion[0], end="      ")
                print(rat[0])
                print(lion[1], end="  VS  ")
                print(rat[1])
                print(lion[2])
                score_1 += 1
            elif choice_2 == 2:
                print(lion[0], end="      ")
                print(hunter[0])
                print(lion[1], end="  VS  ")
                print(hunter[1])
                print(lion[2], end="      ")
                print(hunter[2])
                score_2 += 1
            elif choice_2 == 3:
                print(lion[0], end="      ")
                print(lion[0])
                print(lion[1], end="  VS  ")
                print(lion[1])
                print(lion[2], end="      ")
                print(lion[2])

        if abs(score_1 - score_2 >= 3) or (score_1 + score_2 == 4 and abs(score_1 - score_2) == 2):
            if score_1 > score_2:
                print()
                print(f"{op_1} {score_1} / {op_2} {score_2}")
                print(f"{op_1} win!")
                break
            else:
                print()
                print(f"{op_1} {score_1} / {op_2} {score_2}")
                print(f"{op_2} win!")
                break
        elif count == 5:
            if score_1 > score_2:
                print()
                print(f"{op_1} {score_1} / {op_2} {score_2}")
                print(f"{op_1} win!")
                break
            elif score_1 < score_2:
                print()
                print(f"{op_1} {score_1} / {op_2} {score_2}")
                print(f"{op_2} win!")
                break
            else:
                print()
                print(f"{op_1} {score_1} / {op_2} {score_2}")
                print("Draw!")
                break
        count += 1
    else:
        print()
        print(f"{op_1} {score_1} / {op_2} {score_2}")
        print("Draw!")


play_1 = input("Player1 name: ")
play_2 = input("Player2 name: ")
game(play_1, play_2)


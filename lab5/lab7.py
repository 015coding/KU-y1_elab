def dica(lucky, candidates):
    dic = {}
    counts = {}
    for i in range(candidates):
        id_card = input(f"Enter ID card number {i+1}: ")
        dic[i] = id_card
    for i in dic:
        count = dic[i].count(str(lucky))
        counts[i] = count

    max_count = -1
    winner = 0
    for i in counts:
        if counts[i] > max_count:
            max_count = counts[i]
            winner = dic[i]
        elif counts[i] == max_count:
            if dic[i] > winner:
                winner = dic[i]
    return winner



lucky = int(input("Enter lucky number : "))
candidates = int(input("Enter amount of candidates : "))
print(f"Winner: {dica(lucky, candidates)}")

def chain(txt):
    len_chain = len(txt[0])
    spt_txt = []
    bee = 1
    x = 0
    max = 0

    for i in range(len(txt)):
        for item in txt:
            spt_txt.append(item)
    for i in range(1, len(txt)):
        x += 1
        count = 0
        if x > max and i != (len(txt)-1):
            max = x
        elif x >= max and i == (len(txt)-1):
            max = x +1
        for j in range(len_chain):
            if txt[i-1][j] != txt[i][j]:
                count += 1
            if count > 2:
                bee += 1
                x = 0
                break
    print(f"{bee} Chain(s). Maximum length is {max} word(s).")





txt = input("Text: ").split()
#txt = "SUN TON BOW GOD LOT KID FAX BAT FAT CAR EAT FEE SEA MAP DRY SPY TAP".split()
chain(txt)
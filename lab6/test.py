def findsub(word, sub):
    a = 0
    shift_position = int(len(sub))
    result = []
    len_sub = len(sub)
    check = 0
    count = 0
    while a < len(word)-1:
        for i in range(0, len_sub):
            try:
                if word[a+i] == sub[i]:
                    check += 1
                else:
                    check = 0
                    pass
            except:
                continue
        if check == len_sub:
            result.append(sub[0:len_sub])
            a += shift_position
            check = 0
            count += 1
        else:
            result.append(word[a])
            a += 1
    result.append(word[len(word)-1])
    return result, count

def findsub_v2(word,sub):
    a = 0
    shift_position = int(len(sub))
    result = []
    len_sub = len(sub)
    check = 0
    count = 0
    gaa = []
    while a < len(word):
        for i in range(0, len_sub):
            try:
                if word[a+i] == sub[i]:
                    check += 1
                    gaa.append(word[a+i])
                else:
                    gaa.append("?")
            except:
                continue
        if check >= len_sub-1:
            result.append(gaa)
            a += shift_position
            check = 0
            count += 1
            gaa = []
        else:
            gaa = []
            result.append(word[a])
            a += 1
    #result.append(word[len(word)-1])
    return result

#txt = "acabababababcbabab"
#substrings = "aba"
txt = input("Text: ")
substrings = input("Substring: ")
x = []
y = []
for item in txt:
    x.append(item)
for item in substrings:
    y.append(item)

final, check = findsub(x, y)
if check > 0 :
    for item in final:
        if isinstance(item,list):
            print(f"[{''.join(item)}]",end="")
        else:
            print(item, end='')
else:
    x = findsub_v2(x, y)
    for item in x:
        if isinstance(item,list):
            print(f"[{''.join(item)}]",end="")
        else:
            print(item, end='')


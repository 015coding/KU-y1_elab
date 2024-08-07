def findsub(word, sub):
    a = 0
    shift_position = int(len(sub))
    result = []
    len_sub = len(sub)
    check = 0
    while a < len(word):
        if word[a] == sub[0] and word[a+1] == sub[1] and word[a+2] == sub[2]:
            result.append(sub[0:len_sub])
            a += shift_position
            check += 1
        else:
            result.append(word[a])
            a += 1
    return result, check

def findsub_shi(word,sub):
    shift = 3
    count = 0
    result = []
    while count < len(word):
        if word[count] == sub[0] or word[count+1] == sub[1] or word[count+2] == sub[2]:
            pass

txt = "acabababababcbabab"
substrings = "aba"
x = []
y = []
for item in txt:
    x.append(item)
for item in substrings:
    y.append(item)

final, check = findsub(x, y)
if check >= 1:
    print(final)
elif check == 0:
    findsub_shi(x, y)


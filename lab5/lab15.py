#text = "a b c a b d a f a a a f g r a f d e g d"
#text = "a a b b c c d e f g g a h h b c x x x x"
dc = {}
i = 1
count = 0

def getMultilinesInput():
    text = ""
    while True:
        line = input()
        if not line:
            break
        text += line + ' '
    return text
print("Parse a long paragraph (or text) below, following an ENTER as needed:")
text = getMultilinesInput()
k = int(input("Top K rank: "))

for item in text.lower().split():
    if item in dc:
        dc[item] += 1
    else:
        dc[item] = 1
x = dict(sorted(dc.items(), key=lambda item: item[1], reverse=True))
sort = list(x.items())
lens = len(sort)
while count < k:
    #i += 1
    try:
        item, sort_num = sort[i]
        item1, sort_num1 = sort[i-1]
        if sort_num == sort_num1:
            print(f"{item1}: {sort_num1}", end=", ")
            i +=1
        else:
            i += 1
            count += 1
            print(f"{item1}: {sort_num1}")
    except :
        print(f"{item}: {sort_num}")
        break






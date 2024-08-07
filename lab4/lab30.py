#a = eval("[[1,3],[1,3],[13,15,17],[5,7],[9,11],[9,11],[9,11],[5,7]]")
a = eval(input("Input: "))
count = {}
for i in a:
     b = str(i)
     if b not in count:
         count[b] = 1
     else:
         count[b] +=1
sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
for key, value in sorted_count.items():
    print(f"{key}: {value}")
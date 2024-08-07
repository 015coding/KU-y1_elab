s = "python"

lens = (len(s))
for c in s:
    print(" ", lens,c)
    lens -= 1

lens = len(s)
for i in range(len(s)):
    
    print(' '*lens , s[i])
    lens -= 1

digital = [0 , 1, 5]
for i in digital :
    print( i)
    break

else :
    print("wtf")

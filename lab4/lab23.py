
def str_count(n):
    lst = []
    count = 0
    
    for letter in n:
        lst.append(letter)

    lst_len = len(lst)
    for i in range (lst_len):
        if lst[i] != ' ':
            if lst[i].islower() :
                count +=1
    return count
        
word = str(input("Enter list of words: "))

print(str_count(word))

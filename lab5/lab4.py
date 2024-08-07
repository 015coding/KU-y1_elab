inp = int(input("input: "))
x = inp //2 +1
count_s = inp // 2
c_item = 1
if inp % 2 != 0:
        while c_item <= inp :
            print(" "*count_s+"#"*c_item)
            c_item += 2
            count_s -=1
        c_item -= 2
        count_s +=1
        while c_item > 1:
            c_item -= 2
            count_s +=1
            print(" "*count_s+"#"*c_item)
sec = int(input("s: "))

def final(sec):
    h = sec // 3600
    m = (sec - h*3600)//60
    s = sec - (m*60 + h*3600)
    return h,m,s
h,m,s = final(sec)

print(f"{sec} seconds equals {h} hour(s) {m} minute(s) and {s} second(s)" )

x = int(input("x: "))
y = int(input("y: "))

round = y // 24
time = x + (y - (24*round))

if time >= 24 :
    time_final = time -24
    print(f"She comes at {time_final}:00")
else:
    print(f"She comes at {time}:00")

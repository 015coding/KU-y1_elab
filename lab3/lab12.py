S = int(input("Input starting food (S): "))
P = int(input("Input Paun's eating rate (P): "))
G = int(input("Input Gane's eating rate (G): "))

def eat(S,P,G):
    P_time  = S//P
    G_time = (S - (P_time*P)) // G
    D = S - ((G_time*G)+(P_time*P))
    return D , P_time , G_time

D , P_time , G_time = eat(S,P,G)

print(f"Pane eats {P_time} time(s)")
print(f"Gane eats {G_time} time(s)")
print(f"Remaining {D} for dog")

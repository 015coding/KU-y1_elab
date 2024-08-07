man = str(input("What's the result of Manchester city's match? "))
live = str(input("What's the result of Liverpool's match? "))

if man == "won" and live == "won" :
    man_score = int(input("What is the margin that Manchester city won by? "))
    live_score = int(input("What is the margin that Liverpool won by? "))
    if man_score == live_score :
        play_off = str(input("Which team won the play-off match?(Manchester city/Liverpool) "))
        if play_off == "Manchester city":
            print("Manchester city is the champion of Premier League.")
        else:
            print("Liverpool is the champion of Premier League.")
    elif man_score > live_score :
        print("Manchester city is the champion of Premier League.")
    else:
        print("Liverpool is the champion of Premier League.")
        
elif man == "won" and live == "lost":
    print("Manchester city is the champion of Premier League.")
elif man == "lost" and live == "won":
    print("Liverpool is the champion of Premier League.")
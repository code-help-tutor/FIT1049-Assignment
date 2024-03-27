WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def suits(hand):
    clubs = []
    diamonds = []
    hearts = []
    spades = []
    for i in range(5):
        if hand[i][1] == "C":
            clubs.append(hand[i])
        if hand[i][1] == "D":
            diamonds.append(hand[i])
        if hand[i][1] == "H":
            hearts.append(hand[i])
        if hand[i][1] == "S":
            spades.append(hand[i])
    return [clubs, diamonds, hearts, spades]

def flush(hand):
    clubs = []
    diamonds = []
    hearts = []
    spades = []
    for i in range(5):
        if hand[i][1] == "C":
            clubs.append(hand[i])
        if hand[i][1] == "D":
            diamonds.append(hand[i])
        if hand[i][1] == "H":
            hearts.append(hand[i])
        if hand[i][1] == "S":
            spades.append(hand[i])
    if len(clubs) == 5:
        return True
    if len(diamonds) == 5:
        return True
    if len(hearts) == 5:
        return True
    if len(spades) == 5:
        return True
    else:
        return False


def straight(hand):
    n = len(hand)
    checklist = []
    Min = 10
    Max = 2
    #print(n)
    #print(len(checklist))
    for i in range(n):
        checklist.append(hand[i][0])
    #print(checklist)
    for i in range(n):
        if checklist[i] <= Min:
            Min = int(checklist[i])
        if checklist[i] >= Max:
            Max = checklist[i]
    #print(Min,Max)
    cha = Max - Min
    #print(cha)
    if cha == n-1:
        return True
    if Min >= 10:
        return True
    else:
        return False


print(suits([(4,"C"),(8,"H"),(3,"C"),(2,"D"),(8,"C")]))
print(flush([(4,"D"),(8,"D"),(3,"D"),(2,"D"),(10,"D")]))
print(flush([(4,"C"),(8,"H"),(3,"C"),(2,"D"),(8,"C")]))
print(straight([(4,"C"),(2,"D"),(5,"S"),(6,"H"),(3,"D")]))
print(straight([(2,"C"),(3,"D"),(4,"S"),(5,"H"),(5,"D")]))
print(straight([(2,"C"),(3,"D"),(4,"S"),(5,"H"),(7,"D")]))
print(straight([(12,"C"),(13,"D"),(11,"D")]))
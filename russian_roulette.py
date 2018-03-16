import random

def main():
    winnings = 0
    alive = True

    while(alive):
        print("Winnings:", winnings)
        bet = input("Set a bet? ")
        rounds = input("How many rounds will be set in cylinder? ")

        cylinder = [1] * int(rounds)

        while len(cylinder) < 6:
            cylinder.append(0)
        
        cylinder = spin(cylinder)

        if cylinder[0] == 1:
            alive = False
            print("You dead")
        else:
            profit = multiplier(bet, rounds)
            winnings += profit
            print("You won", profit)

        print("###########################")
           
def spin(cylinder):
    print("Cylinder before spin:", cylinder)
    
    temp = [0] * 6
    
    steps = random.randint(1,50)
    print("Indexes forward:", steps)
    print("Total cycles:",round(steps/6,2))
        
    for index, value in enumerate(cylinder):
        new_index = index + steps
        if new_index > 5:
            new_index = new_index % 6
        temp[new_index] = value
    cylinder = temp[:]
    print("Cylinder after spin:", cylinder)
    return cylinder
    
def multiplier(bet, rounds):
    profit = int(bet) * int(rounds) * 1.2
    return profit
    
main()

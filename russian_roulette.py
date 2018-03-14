import random

def main():
    winnings = 0
    
    rounds = input("How many rounds? ")
    cylinder = [1] * int(rounds)
    while len(cylinder) < 6:
        cylinder.append(0)
    print(cylinder)

    rand = random.randint(1,6)
    print("rand:", rand)
    temp = [0] * 6
    print(temp)
    for index, value in enumerate(cylinder):
        new_index = index + rand
        print(new_index)
        if new_index > 5:
             new_index = new_index % 6
             print(new_index)
        temp[new_index] = value
    cylinder = temp[:]

    if cylinder[0] == 1:
        print("You dead")
    else:
        value = multiplier(bet, rounds)
        winnings += value
        print(f"You won {value}")
        
       
        
    

def multiplier(bet, rounds):
    value = bet * rounds * 1.2
    return value
    

main()

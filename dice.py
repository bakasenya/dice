from numpy import random 

def roll_dice_random():
    prev_number = random.randint(1, 7)
    roll_count = 0
    while True:
        roll_dice = random.randint(1, 7)
        roll_count += 1
        print(f"Rolled: {roll_dice}")
        
        if prev_number == roll_dice:
            print("The current number matches the previous number")
            print(f"It rolled {roll_count} time!")
            break
        
        prev_number = roll_dice
        

result = roll_dice_random()



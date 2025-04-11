import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"die1: {die1}, die2: {die2}, total: {total}")

def main():  
    die = 10
    print(f"Value of 'die' in main() starts as {die}")
    for _ in range(3):
        roll_dice()
        print(f"'die' in main() is still {die}")

if __name__ == '__main__':
    main()

  

import random

FISHING_COST = 1
STARTING_BALANCE = 100
STARTING_BAIT = 10
STARTING_ROD = "Wood"

fish_count = {
    "Carp" : 5,
    "Trout" : 5,
    "Boot" : 5,
    "Treasure" : 2
}

fish_value = {
    "Carp" : 10,
    "Trout" : 5,
    "Boot" : 1,
    "Treasure" : 100
}

fish_inventory = []

        
def catch_fish(bait, fishes):
    if bait < FISHING_COST:
        print("You do not have enough bait to fish.")
    bait -= FISHING_COST
    
    all_fish = []
    for fish, fish_count in fishes.items():
        for _ in range(fish_count):
            all_fish.append(fish)
        
    remaining_fish = all_fish[:]
    caught_fish = random.choice(remaining_fish)
    remaining_fish.remove(caught_fish)
        
    return bait, caught_fish
    
        
def store_fish(fish):
    fish_inventory.append(fish)
    
def get_fish_value(fish, values):
    value = values[fish]
    return value
    
def get_inventory_value(inventory, values):
    inventory_value = 0
    for fish in inventory:
        inventory_value += values[fish]
    return inventory_value
    
def print_fisher_stats(name, rod, bait, balance):
    print(f"{name} is using {rod} rod with {bait} bait and a balance of ${balance}")


def get_user():
    name = input("Please tell me your name: ")
    rod = STARTING_ROD
    bait = STARTING_BAIT
    balance = STARTING_BALANCE
    
    return name, rod, bait, balance

def main():
    name, rod, bait, balance = get_user()
    print(f"Hi {name}! We have provided you with a {rod} rod and {bait} bait to get started with.")
    while True:
        fishing = input("Press enter to fish, or q to quit")
        if fishing.lower() == "q":
            break
        bait, caught_fish = catch_fish(bait, fish_count)
        store_fish(caught_fish)
        caught_value = get_fish_value(caught_fish, fish_value)
        print(f"You have caught a {caught_fish}!")
        sell = input(f"Would you like to sell the fish for ${caught_value}? (y/n)")
        if sell.lower() == "y":
            balance += caught_value
            fish_inventory.remove(caught_fish)
        
        break
    
    
    print_fisher_stats(name, rod, bait, balance)
    print(fish_inventory)
        
if __name__ == "__main__":
    main()
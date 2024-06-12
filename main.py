import random

FISHING_COST = 1
STARTING_BALANCE = 100
STARTING_BAIT = 10
STARTING_ROD = "Wood"

fish_inventory = []

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


class Fisher:
    def __init__(self, name, bait, rod, balance, inventory):
        self.name = name
        self.bait = bait
        self.rod = rod
        self.balance = balance
        self.inventory = inventory
        
        
    def cast_rod(self):
        self.bait -= FISHING_COST
            
    def catch_fish(self, fishes):
        if self.bait < FISHING_COST:
            print("You do not have enough bait to fish.")
        
        self.cast_rod()
        all_fish = []
        for fish, fish_count in fishes.items():
            for _ in range(fish_count):
                all_fish.append(fish)
        
        remaining_fish = all_fish[:]
        caught_fish = random.choice(remaining_fish)
        remaining_fish.remove(caught_fish)
        fish_inventory.append(caught_fish)
        
        
        
def main():
    print("--- Fishing Game ---")
    user = get_user()
    display_user(user)
    display_inventory(user)
    while user.bait > 0:
        user.catch_fish(fish_count)
        display_user(user)
        display_inventory(user)
    get_inventory_value(user, fish_value)
    
def get_user():
    name = input("Please tell me your name: ")
    bait = STARTING_BAIT
    rod = STARTING_ROD
    balance = STARTING_BALANCE
    inventory = fish_inventory
    user = Fisher(name, bait, rod, balance, inventory)
    
    return user
    
def display_user(fisher):
    print(f"{fisher.name}: bait = {fisher.bait}, rod = {fisher.rod}, balance = {fisher.balance}")
    
def display_inventory(fisher):
    print(f"{fisher.name}: {fisher.inventory}")
    
def get_inventory_value(fisher, values):
    inventory_value = 0
    for fish in fisher.inventory:
        inventory_value += values[fish]   
    print(f"{fisher.name}'s inventory: ${inventory_value}")
    
if __name__ == "__main__":
    main()
import random
class Player:
    def __init__(self, name, height, weight, strength, skills, vertical, on_ball_speed, off_ball_speed, passing, shooting, dribbling, perimeter_defense, interior_defense, driving_dunk, standing_dunk, post_moves, layups, free_throws):
        self.name = name
        self.height = height
        self.weight = weight
        self.strength = strength
        self.skills = skills
        self.vertical = vertical
        self.on_ball_speed = on_ball_speed
        self.off_ball_speed = off_ball_speed
        self.passing = passing
        self.shooting = shooting
        self.dribbling = dribbling
        self.perimeter_defense = perimeter_defense
        self.interior_defense = interior_defense
        self.driving_dunk = driving_dunk
        self.standing_dunk = standing_dunk
        self.post_moves = post_moves
        self.layups = layups
        self.free_throws = free_throws
        self.overall = (skills + shooting + dribbling + perimeter_defense + interior_defense + passing + layups + free_throws) // 8
        self.pockets = int(0)

def create_player(position, name):
    stats = {
        'PG': (190, 180, 60, 70, 70, 70, 75, 80, 75, 75, 70, 55, 50, 35, 60, 75, 75),
        'SG': (195, 185, 70, 65, 75, 70, 70, 70, 80, 70, 65, 65, 65, 55, 65, 70, 80),
        'SF': (198, 190, 70, 65, 75, 70, 70, 70, 80, 70, 65, 65, 65, 55, 65, 70, 80),
        'PF': (205, 230, 70, 65, 75, 70, 70, 70, 80, 70, 65, 65, 65, 55, 65, 70, 80),
        'C':  (215, 220, 70, 65, 75, 70, 70, 70, 80, 70, 65, 65, 65, 55, 65, 70, 80),
    }
    return Player(name, *stats.get(position, (190, 180, 60, 70, 70, 70, 75, 80, 75, 75, 70, 55, 50, 35, 60, 75, 75)))

def display_stats(player):
    print(f"Player Stats for {player.name}:")
    for attr, value in vars(player).items():
        print(f"{attr.capitalize()}: {value}")

def train_player(player):
    print("Train your player: (1) Improve Technique (2) Increase Physical Attributes")
    choice = input("Enter your choice (1-2): ")
    if choice == '1':
        player.shooting += 2
        player.dribbling += 2
        player.passing += 2
        print(f"{player.name}'s technique has improved!")
    elif choice == '2':
        player.strength += 2
        player.vertical += 2
        player.on_ball_speed += 2
        player.off_ball_speed += 2
        print(f"{player.name}'s physical attributes have improved!")
    player.overall = (player.skills + player.shooting + player.dribbling + 
                      player.perimeter_defense + player.interior_defense + 
                      player.passing + player.layups + player.free_throws) // 8

def scrim(player):
    print("Scrim in progress...")
    if player.overall >= 85:
        print(f"{player.name} performed excellently in the scrim!")
        print(f"Reward: +{random.randint(50,100)}$ to Pockets")
    elif player.overall <= 75:
        print(f"{player.name} got whooped.")
        train_player(player)
    else:
        print(f"Scrim did not go so well...")
        train_player(player)

def main_menu():
    position = input("What position do you want to play? (PG/SG/SF/PF/C): ")
    name = input("What is your player's name? ")
    player = create_player(position, name)
    print(f"Player Name: {player.name}, Overall Rating: {player.overall}")

    while True:
        print("What would you like to do next? (1) View Player Stats (2) Train Player (3) Scrim (4) Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            display_stats(player)
        elif choice == '2':
            train_player(player)
        elif choice == '3':
            scrim(player)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()

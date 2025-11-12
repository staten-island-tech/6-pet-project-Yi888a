
class Player:
    def __init__(self, name, overall, height, weight, strength, skills, vertical, on_ball_speed, off_ball_speed, passing, shooting, dribbling, perimeter_defense, interior_defense, driving_dunk, standing_dunk, post_moves, layups, free_throws):
        self.name = name
        self.overall = (int(skills) + int(shooting) + int(dribbling) + int(perimeter_defense) + int(interior_defense) + int(passing) + int(layups) + int(free_throws)) // 8
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
player_position = input("What position do you want to play? ")
player_name = input("What is your player's name? ")
if player_position == 'PG':
 player1 = Player(player_name, 0, 190, 180, 60, 70, 70, 70, 75, 80, 75, 75, 70, 55, 50, 35, 60, 75, 75)
elif player_position == 'SG':
     player1 = Player(player_name, 0, 195, 185, 70, 65, 75, 70, 70, 70, 80, 70, 65, 65, 65, 55, 65, 70, 80)
elif player_position == 'SF':
      player1 = Player(player_name, 0, 198, 190, 70, 65, 75, 70, 70, 70, 80, 70, 65, 65, 65, 55, 65, 70, 80)



print(f"Player Name: {player1.name}, Overall Rating: {player1.overall}")
print("What would you like to do next? (1) View Player Stats (2) Train Player (3) Scrim (4) Exit")
choice = input("Enter your choice (1-4): ")
if choice == '1':
    print(f"Player Stats for {player1.name}:")
    print(f"Height: {player1.height} Centimeters")
    print(f"Weight: {player1.weight} Kilograms")
    print(f"Strength: {player1.strength}")
    print(f"Skills: {player1.skills}")
    print(f"Vertical: {player1.vertical} inches")
    print(f"On-Ball Speed: {player1.on_ball_speed}")
    print(f"Off-Ball Speed: {player1.off_ball_speed}")
    print(f"Passing: {player1.passing}")
    print(f"Shooting: {player1.shooting}")
    print(f"Dribbling: {player1.dribbling}")
    print(f"Perimeter Defense: {player1.perimeter_defense}")
    print(f"Interior Defense: {player1.interior_defense}")
    print(f"Driving Dunk: {player1.driving_dunk}")
    print(f"Standing Dunk: {player1.standing_dunk}")
    print(f"Post Moves: {player1.post_moves}")
    print(f"Layups: {player1.layups}")
    print(f"Free Throws: {player1.free_throws}")
elif choice == '2':
    print("What would you like to do to train your player? (1) Improve Technique (2) Increase Physical Attributes")
    train_choice = input("Enter your choice (1-2): ")
if train_choice == '1':
        player1.shooting += 2
        player1.dribbling += 2
        player1.passing += 2
        print(f"{player1.name}'s technique has improved!")
elif train_choice == '2':
        player1.strength += 2
        player1.vertical += 2
        player1.on_ball_speed += 2
        player1.off_ball_speed += 2
        print(f"{player1.name}'s physical attributes have improved!")
else:
        print("Invalid choice.")

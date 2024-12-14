# CSC 2080 - Homework Assignment #8

# 1. Chapter 9 Discussion Question 1 (pg 308)
# Structure chart for the given main function.

# Main function
def main():
    # Call the function to print introductory message
    printIntro()
    
    # Get the dimensions of the area (length and width)
    length, width = getDimensions()
    
    # Calculate the amount of material needed based on the length and width
    amtNeeded = computeAmount(length, width)
    
    # Print the report with the calculated details
    printReport(length, width, amtNeeded)


# Function to print introductory message
def printIntro():
    print("This program calculates the amount of material needed for a project.")

# Function to get dimensions (length and width) from the user
def getDimensions():
    # Get the length from the user input
    length = float(input("Enter the length of the area: "))
    # Get the width from the user input
    width = float(input("Enter the width of the area: "))
    
    # Return both length and width as a tuple
    return length, width

# Function to compute the amount of material needed
def computeAmount(length, width):
    # Assuming we need to calculate area and multiply by a constant to determine amount needed
    return length * width * 1.5  # For example, 1.5 is the factor for material per unit area

# Function to print the report of the calculations
def printReport(length, width, amtNeeded):
    print(f"Dimensions of the area: {length} x {width}")
    print(f"Amount of material needed: {amtNeeded} units")

# 2. Chapter 9 Programming Exercise 1 (pg 309) - Best of n game simulation

# Function to simulate a best of n game for racquetball
def racquetball_simulation(best_of_n):
    # Initialize player scores
    player_A_wins = 0
    player_B_wins = 0
    
    # Loop through each game in the best of n series
    for game_num in range(1, best_of_n + 1):
        print(f"Game {game_num}:")
        
        # Alternate serves between Player A and Player B
        if game_num % 2 == 1:  # Player A serves in odd-numbered games
            server = "Player A"
        else:  # Player B serves in even-numbered games
            server = "Player B"
        
        print(f"Server: {server}")
        
        # Simulate game result (random win/loss for each player)
        game_winner = simulate_game(server)
        
        # Update player win counts based on game result
        if game_winner == "Player A":
            player_A_wins += 1
        else:
            player_B_wins += 1

    # Determine and print the match winner
    if player_A_wins > player_B_wins:
        print("Player A wins the match!")
    elif player_B_wins > player_A_wins:
        print("Player B wins the match!")
    else:
        print("The match is a tie!")

# Function to simulate a single game (random win for Player A or Player B)
def simulate_game(server):
    import random
    return random.choice(["Player A", "Player B"])

# Call racquetball_simulation to simulate a best of 5 match
# Note: You can modify the number of games as needed (e.g., best_of_n = 5)
racquetball_simulation(5)

# 3. Chapter 9 Programming Exercise 2 (pg 309) - Racquetball simulation with shutouts

# Function to simulate a best of n game with shutouts
def racquetball_simulation_shutout(best_of_n):
    # Initialize player stats
    player_A_wins = 0
    player_B_wins = 0
    player_A_shutouts = 0
    player_B_shutouts = 0
    
    # Loop through each game in the best of n series
    for game_num in range(1, best_of_n + 1):
        print(f"Game {game_num}:")
        
        # Alternate serves between Player A and Player B
        if game_num % 2 == 1:  # Player A serves in odd-numbered games
            server = "Player A"
        else:  # Player B serves in even-numbered games
            server = "Player B"
        
        print(f"Server: {server}")
        
        # Simulate game result and check for shutout
        game_winner, shutout = simulate_game_shutout(server)
        
        # Update player win and shutout counts
        if game_winner == "Player A":
            player_A_wins += 1
            if shutout:
                player_A_shutouts += 1
        else:
            player_B_wins += 1
            if shutout:
                player_B_shutouts += 1

    # Print the match results including shutout stats
    print(f"Player A wins: {player_A_wins}")
    print(f"Player B wins: {player_B_wins}")
    print(f"Player A shutouts: {player_A_shutouts}")
    print(f"Player B shutouts: {player_B_shutouts}")
    print(f"Player A shutout percentage: {player_A_shutouts / player_A_wins * 100:.2f}%")
    print(f"Player B shutout percentage: {player_B_shutouts / player_B_wins * 100:.2f}%")

# Function to simulate a single game with a potential shutout
def simulate_game_shutout(server):
    import random
    # Simulate a shutout (no points for the losing player)
    game_winner = random.choice(["Player A", "Player B"])
    shutout = random.choice([True, False])
    return game_winner, shutout

# Call racquetball_simulation_shutout to simulate a best of 5 match with shutouts
# Note: You can modify the number of games as needed (e.g., best_of_n = 5)
racquetball_simulation_shutout(5)

# 4. Explanation of API and interaction with endpoints

# An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other.
# It defines the methods and data structures that developers can use to interact with the functionality of a service or system.
# Endpoints are specific locations within an API where specific functionality can be accessed or called, usually via a URL.
# For example, the Google Maps API has an endpoint for requesting directions between two locations.

# Real-world example of an API: 
# The Twitter API allows developers to access public data from Twitter (such as tweets, followers, etc.) and interact with the platform programmatically.

# 5. Explanation of a framework vs language

# A programming language is a set of rules that allows developers to write code that can be executed by a computer.
# A framework is a pre-built set of tools and libraries that helps developers build applications faster by providing reusable code for common tasks.

# Example of a framework and its underlying language:
# Flask is a Python-based framework used for building web applications. It provides tools for routing, handling requests, rendering HTML templates, and more.
# Flask is built on Python, which is the underlying language used to develop the application logic.

# Real-world company using Flask:
# Netflix uses Flask as part of its backend services for building web APIs and handling various user interactions.

# Lauren Sheehan, Gahana Nagaraja, Manoj Avineni Sudhakar
# 12/5/23
# This program defines the main function to run the game

from GameEngine import GameEngine

def main():
    """
    Initializes and runs gameplay and calls all necessary functions
    :return: N/A
    """
    # Instantiate and store a GameEngine object
    game_engine = GameEngine()
    # Initialize the game using the initializeGame() function
    game_engine.initializeGame()
    # Displays game's introduction
    game_engine.intro()
    # Stores remaining veggies in the game
    remaining_veggies = game_engine.remainingVeggies()

    # Runs program as long as there are still veggies on the field
    while remaining_veggies > 0:
        print(f"{remaining_veggies} Veggies remaining. Current score: {game_engine.getScore()}")
        # Prints out field
        game_engine.printField()
        # Moves rabbits
        game_engine.moveRabbits()
        # Moves Captain
        game_engine.moveCaptain()
        # Determine the new number of remaining veggies
        remaining_veggies = game_engine.remainingVeggies()
    # Displays game over information
    game_engine.gameOver()
    # Handles the high score functionality
    game_engine.highScore()


main()

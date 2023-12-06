# Lauren Sheehan, Gahana Nagaraja, Manoj Avineni Sudhakar
# 12/5/23
# This program puts together the functionality of the game and defines all the necessary functions

import pickle
import random
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit

class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        """
        Initializes and manages the game
        """
        self._field = []
        self._num_of_rabbits = []
        self._captain_object = None
        self._possible_veggies = []
        self._score = 0

    def initVeggies(self):
        """
        Read in Veggie file (if it exists) and puts veggies in the field
        :return: N/A
        """
        file_exists = True
        while file_exists:
            # Prompt user for input
            file_name = input("Please enter the name of the vegetable point file: ")
        # If the file exists, read in file, if it does not, keep asking user until they input a file that exists
            try:
                with open(file_name, "r") as veggie_file:
                    line_size = veggie_file.readline().strip().split(",")

                    field_size = (int(line_size[1]), int(line_size[2]))

                    self._field = [[None for _ in range(field_size[1])] for _ in range(field_size[0])]

                    veggie_lines = veggie_file.readlines()
                    for veggie_line in veggie_lines:
                        veggie_data = veggie_line.strip().split(",")      # Delimited w/commas
                        name, symbol, points_worth = veggie_data[0], veggie_data[1], int(veggie_data[2])
                        veggie = Veggie(name, symbol, points_worth)
                        self._possible_veggies.append(veggie)

                    for _ in range(self.__NUMBEROFVEGGIES):
                        location = (random.randint(0, field_size[0]-1), random.randint(0, field_size[1]-1))

                        while self._field[location[0]][location[1]] is not None:
                            location = (random.randint(0, field_size[0]-1), random.randint(0, field_size[1]-1))

                        veggie = random.choice(self._possible_veggies)
                        self._field[location[0]][location[1]] = veggie

            except FileNotFoundError:
                print(f"{file_name} does not exist! Please enter the name of the vegetable point file:")
                continue
            else:
                break

    def initCaptain(self):
        """
        Initializes Captain object on the field randomly and makes sure it doesn't overlap with rabbits
        :return: N/A
        """
        # Random location for the Captain object
        location = (random.randint(0, len(self._field)-1), random.randint(0, len(self._field[0])-1))

        # Randomly generates Captain's location until it can be put in spot that does not contain a rabbit
        while self._field[location[0]][location[1]] is not None:
            location = (random.randint(0, len(self._field)-1), random.randint(0, len(self._field[0])-1))

        # New Captain object created using random location
        captain = Captain(location[0], location[1])
        self._captain_object = captain
        self._field[location[0]][location[1]] = captain

    def initRabbits(self):
        """
        Initializes rabbit objects on the field randomly and makes sure it doesn't overlap with the Captain
        :return: N/A
        """
        # Randomly chooses a location for the rabbit object (until an empty location is found)
        for _ in range(self.__NUMBEROFRABITS):
            location = (random.randint(0, len(self._field)-1), random.randint(0, len(self._field[0])-1))

            # Randomly generates Rabbit's location until it can be put in spot that does not contain the Captain
            while self._field[location[0]][location[1]] is not None:
                 location = (random.randint(0, len(self._field)-1), random.randint(0, len(self._field[0])-1))

            # New Rabbit object created using random location
            rabbit = Rabbit(location[0], location[1])
            self._num_of_rabbits.append(rabbit)
            self._field[location[0]][location[1]] = rabbit


    # Initialize the game
    def initializeGame(self):
        """
        Initializes the whole game by initializing the veggies, the Captain, and rabbits
        :return: N/A
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    # Counts remaining veggies on the field
    def remainingVeggies(self):
        """
        Counts the number of veggies left on the field
        :return: Number of veggies on the field
        """
        count = 0
        for row in self._field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        """
        Displays intro information about the game and the list of veggies with their
        symbols and point values
        :return: N/A
        """
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest\n"
              "as many vegetables as possible before the rabbits eat them\n"
              "all! Each vegetable is worth a different number of points\n"
              "so go for the high score!")
        print("\nThe list of possible vegetables are:")
        for veggie in self._possible_veggies:
            print(veggie)

        print("\nCaptain Veggie is V, and the rabbits are R's.")
        print("\nGood Luck!")

    def printField(self):
        """
        Prints the field with updated veggies and creatures and adds a border
        :return: N/A
        """
        # Printing the top border
        print("#" * (len(self._field[0]) * 2 + 3))

        # Printing each row with borders
        for row in self._field:
            print("#", end=" ")
            for item in row:
                if item is None:
                    print(" ", end=" ")
                else:
                    print(item.get_symbol(), end=" ")
            print("#")

        # Printing the bottom border
        print("#" * (len(self._field[0]) * 2 + 3))

    def getScore(self):
        """
        Gets the player's score
        :return: The player's score
        """
        return self._score

    def moveRabbits(self):
        """
        Moves rabbits around the field making sure they don't run into the Captain/ other rabbits
        :return: N/A
        """
        for rabbit in self._num_of_rabbits:
            # Current position of the rabbit
            current_x, current_y = rabbit.get_x(), rabbit.get_y()
            # Moves rabbit left/right and up/down one position
            new_x = current_x + random.choice(range(-1, 2))
            new_y = current_y + random.choice(range(-1, 2))
            # If the rabbit stays still (is 0), pick a new move
            while new_x == current_x and new_y == current_y:
                new_x = current_x + random.choice(range(-1, 2))
                new_y = current_y + random.choice(range(-1, 2))

            # Ensures movement stays within the bounds of the field
            if 0 <= new_x < len(self._field) and 0 <= new_y < len(self._field[0]):
                if (
                    any((new_x == r.get_x() and new_y == r.get_y()) or
                    (new_x == self._captain_object.get_x() and new_y == self._captain_object.get_y())
                    for r in self._num_of_rabbits)
                ):
                    continue

                # Removes rabbit from its current position
                self._field[current_x][current_y] = None
                # Moves rabbit to its new position in the field
                self._field[new_x][new_y] = rabbit
                # Updates the rabbit's position after being moved
                rabbit.set_x(new_x)
                rabbit.set_y(new_y)

    def moveCptVertical(self, vertical_movement):
        """
        Moves Captain vertically (each step is commented below)
        :param vertical_movement: How much the Captain will move up or down
        :type vertical_movement: integer
        :return: N/A
        """
        # Determines position of Captain in the field
        current_x, current_y = self._captain_object.get_x(), self._captain_object.get_y()
        # How the vertical movement will be updated
        new_x = current_x + vertical_movement

        # Warns user if they step on a bunny
        if 0 <= new_x < len(self._field):
            if isinstance(self._field[new_x][current_y], Rabbit):
                print("Don't step on the bunnies!")
            # Tells user they collected a vegetable
            else:
                if isinstance(self._field[new_x][current_y], Veggie):
                    veggie = self._field[new_x][current_y]
                    print(f"Yummy! A delicious {veggie.get_name()} found")

                    # Updates point values
                    self._captain_object.addVeggie(veggie)
                    self._score += veggie.get_points_worth()

                # Removes Captain from current position
                self._field[current_x][current_y] = None
                # Moves Captain vertically within the field
                self._field[new_x][current_y] = self._captain_object
                # Updates Captain's position after movement
                self._captain_object.set_x(new_x)

    def moveCptHorizontal(self, horizontal_movement):
        """
        Moves Captain horizontally (each step is commented below)
        :param horizontal_movement: How much the Captain will move left or right
        :type horizontal_movement: integer
        :return: N/A
        """
        # Determines position of Captain in the field
        current_x, current_y = self._captain_object.get_x(), self._captain_object.get_y()
        # How the horizontal movement will be updated
        new_y = current_y + horizontal_movement

        # Warns user if they step on a bunny
        if 0 <= new_y < len(self._field[0]):
            if isinstance(self._field[current_x][new_y], Rabbit):
                print("Don't step on the bunnies!")
            # Tells user they collected a vegetable
            else:
                if isinstance(self._field[current_x][new_y], Veggie):
                    veggie = self._field[current_x][new_y]
                    print(f"Yummy! A delicious {veggie.get_name()} found")

                    # Updates point values
                    self._captain_object.addVeggie(veggie)
                    self._score += veggie.get_points_worth()

                # Removes Captain from current position
                self._field[current_x][current_y] = None
                # Moves Captain horizontally within the field
                self._field[current_x][new_y] = self._captain_object
                # Updates Captain's position after movement
                self._captain_object.set_y(new_y)

    def moveCaptain(self):
        """
        Allows player to input the direction they would like to move the Captain
        :return: N/A
        """
        # Prompt user for input on which direction they would like to move the Captain
        direction = input("Would you like to move up(W), down(S), left(A) or right(D)?").lower()

        # Determines each direction for the Captain (also tells them if their choice is invalid)
        if direction == 'w':
            self.moveCptVertical(-1)
        elif direction == 's':
            self.moveCptVertical(1)
        elif direction == 'a':
            self.moveCptHorizontal(-1)
        elif direction == 'd':
            self.moveCptHorizontal(1)
        else:
            print(f"{direction} is not a valid option")

    def gameOver(self):
        """
        Displays the game over info (veggies harvested and player's final score)
        :return: N/A
        """
        print("GAME OVER!")
        # Lists veggies the Captain harvested
        veggies_harvested = self._captain_object.getVeggieList()
        if veggies_harvested:
            print("You managed to harvest the following vegetables:")
            for veggie in veggies_harvested:
                print(f" -{veggie.get_name()}")
        # Notifies player if they did not collect any veggies
        else:
            print("You did not harvest any vegetables.")

        # Tells player their final score
        print(f"Your score was: {self._score}")

    def highScore(self):
        """
        Handles player high scores, ranks them, and prints out the information
        :return: N/A
        """
        # Declares a list to store player high scores
        high_scores = []
        # Opens and pickles file into the list of high score (raises exception if it does not exist, pass)
        try:
            with open(self.__HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)
        except FileNotFoundError:
            pass

        # Prompts player for their initials
        player_initials = input("Please enter your three initials to go on the scoreboard: ").upper()[:3]
        score_of_player = (player_initials, self._score)

        # Adds tuple into the list of high scores
        if not high_scores:
            high_scores.append(score_of_player)

        else:
            added_score = False
            for i, (player_initial, score) in enumerate(high_scores):
                # Ranks scores from highest to lowest
                if self._score > score:
                    high_scores.insert(i, score_of_player)
                    added_score = True
                    break

            # If there are no high scores yet, adds it to list of high scores
            if not added_score:
                high_scores.append(score_of_player)

        # Prints out the high scores
        print("HIGH SCORES")
        for player_initial, score in enumerate(high_scores, start=1):
            print(f"{player_initial}   {score}")

        # Pickle the list of high scores to the file and closes it
        with open(self.__HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)


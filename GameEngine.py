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

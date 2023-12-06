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

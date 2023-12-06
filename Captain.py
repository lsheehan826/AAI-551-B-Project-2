# Lauren Sheehan, Gahana Nagaraja, Manoj Avineni Sudhakar
# 12/5/23
# This program defines the Captain class, the addVeggie function, and the getter function for the veggie list

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        """
        Initializes the Captain class (inheriting from Creature)
        :param x: Vertical position of the Captain
        :type x: integer
        :param y: Horizontal position of the Captain
        :type y: integer
        :return: N/A
        """
        super().__init__(x, y, "V")

        self._veggie_list = []

    def addVeggie(self, veggie):
        """
        Adds to Captain's veggies
        :param veggie: The veggie that will be added
        :type veggie: string
        :return: N/A
        """
        self._veggie_list.append(veggie)

    def getVeggieList(self):
        """
        Gets the list of veggies the Captain collects
        :return: List of veggies the Captain collected
        """
        return self._veggie_list

    
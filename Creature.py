# Lauren Sheehan, Gahana Nagaraja, Manoj Avineni Sudhakar
# 12/5/23
# This program defines the Creature class and creates getter and setter functions

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
        Initializes the Creature class (inheriting from FieldInhabitant)
        :param x: Vertical position of the creature
        :type x: integer
        :param y: Horizontal position of the creature
        :type y: integer
        :param symbol: Symbol representing the creature
        :type symbol: string
        :return: N/A
        """
        super().__init__(symbol)
        self._x = x
        self._y = y

    # Getter functions
    def get_x(self):
        """
        Gets the vertical position of the creature
        :return: Vertical position of the creature
        """
        return self._x

    def get_y(self):
        """
        Gets the horizontal position of the creature
        :return: Horizontal position of the creature
        """
        return self._y

    # Setter functions
    def set_x(self, x):
        """
        Sets the vertical position of the creature
        :param x: Vertical position of the creature
        :type x: integer
        :return: Vertical position of the creature
        """
        self._x = x

    def set_y(self, y):
        """
        Sets the horizontal position of the creature
        :param y: Horizontal position of the creature
        :type y: integer
        :return: Horizontal position of the creature
        """
        self._y = y

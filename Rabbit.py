# Lauren Sheehan, Gahana Nagaraja, Manoj Avineni Sudhakar
# 12/5/23
# This program defines the Rabbit class and creates getter and setter functions

from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        """
        Initializes the Rabbit class (inheriting from Creature)
        :param x: Vertical position of the rabbit
        :type x: integer
        :param y: Horizontal position of the rabbit
        :type y: integer
        :return: N/A
        """
        super().__init__(x, y, "R")
        self._x = x
        self._y = y

    # Getter functions
    def get_x(self):
        """
        Gets the vertical position of the rabbit
        :return: Vertical position of the rabbit
        """
        return self._x

    def get_y(self):
        """
        Gets the horizontal position of the rabbit
        :return: Horizontal position of the rabbit
        """
        return self._y

    # Setter functions
    def set_x(self, x):
        """
        Sets the vertical position of the rabbit
        :param x: Vertical position of the rabbit
        :type x: integer
        :return: Vertical position of the rabbit
        """
        self._x = x

    def set_y(self, y):
        """
        Sets the horizontal position of the rabbit
        :param y: Horizontal position of the rabbit
        :type y: integer
        :return: Horizontal position of the rabbit
        """
        self._y = y

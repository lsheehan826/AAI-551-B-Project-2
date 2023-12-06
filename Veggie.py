# Lauren Sheehan, Gahana Nagaraja, Manoj Avineni Sudhakar
# 12/5/23
# This program defines the Veggie class and creates getter and setter functions

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points_worth):
        """
        Initializes the Veggie class (inheriting from FieldInhabitant)
        :param name: The name of the veggie
        :type name: string
        :param symbol: Symbol representing the veggie
        :type symbol: string
        :param points_worth: The point value of each veggie
        :type points_worth: integer
        :return: N/A
        """
        super().__init__(symbol)
        self._name = name
        self._points_worth = points_worth

    # Getter functions
    def get_name(self):
        """
        Gets the name of the veggie
        :return: Name of the veggie
        """
        return self._name

    def get_points_worth(self):
        """
        Gets the point value of each veggie
        :return: The point value of each veggie
        """
        return self._points_worth

    # Setter functions
    def set_name(self, name):
        """
        Sets the name for the veggie
        :param name: Name of the veggie
        :type name: string
        :return: N/A
        """
        self._name = name

    def set_points_worth(self, points_worth):
        """
        Sets the point value of each veggie
        :param points_worth: Point value of each veggie
        :type points_worth: integer
        :return: N/A
        """
        self._points_worth = points_worth

    # Lists out vegetable symbols, names, and point values
    def __str__(self):
        """
        Creates a formatted string of veggie info
        :return: Symbol, name, and point values for each veggie
        """
        return f"{self.get_symbol()}: {self.get_name()} {self.get_points_worth()} points"

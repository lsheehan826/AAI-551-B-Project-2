# Lauren Sheehan, Gahana Nagaraja, Manoj Avineni Sudhakar
# 12/5/23
# This program defines the FieldInhabitant class and creates getter and setter functions

class FieldInhabitant:
    def __init__(self, symbol):
        """
        Initializes FieldInhabitant class
        :param symbol: Symbol representing the type of field inhabitant
        (type of veggie, the Captain, or a rabbit)
        :type symbol: string
        :return: N/A
        """
        self._symbol = symbol

    def get_symbol(self):
        """
        Gets the symbol of the field inhabitant
        :return: Symbol representing the inhabitant
        """
        return self._symbol

    def set_symbol(self, symbol):
        """
        Sets symbols for the field inhabitants
        :param symbol: Symbol representing the inhabitant
        :type symbol: string
        :return: N/A
        """
        self._symbol = symbol

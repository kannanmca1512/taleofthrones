from kingdom import Kingdom
class Southeros:
    """
    Class to contain the World of Southeros
    """

    def __init__(self, kingdoms=[]):
        self.__rulingKingdom = None
        self.__kingdom_count = 0
        self.register_kingdoms(kingdoms)

    def register_kingdom(self, name, emblem):
        """
        Creates a Kingdom Class for the given kingdom name and emblem
        """
        new_kingdom = Kingdom(name, emblem)
        self.__kingdom_count += 1
        return new_kingdom
    
    def register_kingdoms(self, kingdoms):
        """
        Registers all the kingdoms
        """
        for name, emblem in kingdoms:
            self.register_kingdom(name, emblem)
    
    def get_kingdom(self, name):
        """
        Get the Kingdom Object from the Name of the kingdom
        """
        return Kingdom.get_kingdom(name)

    def ruler(self):
        """Get the Ruler of Southeros
        """
        if self.__rulingKingdom == None:
            self.__rulingKingdom = self.__ruling_kingdom()
        return self.__rulingKingdom

    def __ruling_kingdom(self):
        """
        Get the Ruler of Southeros
        """
        return Kingdom.get_ruler()

    def get_total_kingdoms(self):
        """
        Return the count of Total Kingdoms in Southeros
        """
        return self.__kingdom_count
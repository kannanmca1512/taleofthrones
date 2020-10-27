from Message import Message

class MessageVerify:
    """
    Class that verifies if the message sent results in positive or negitive reply
    """
    @classmethod
    def verify(cls, prospect_kingdom, message):
        message_dict = cls.__get_frequency_of_each_character(message)
        chiper_emblem_name = cls.__chiper_emblem(prospect_kingdom.emblem(), 
                prospect_kingdom.emblem_length())
        emblem_dict = cls.__get_frequency_of_each_character(chiper_emblem_name)
        for key in emblem_dict.keys():
            message_key_count = message_dict.get(key, 0)
            if message_key_count < emblem_dict[key]: return False
        return True

    @classmethod
    def __get_frequency_of_each_character(cls, text):
        """
        Returns the frequency of each character in the given string
        """
        freq = {}
        for key in text: 
            freq[key] = freq.get(key, 0) + 1
        return freq

    @classmethod
    def __chiper_emblem(cls, text, chiper_key):
        """
        Chiper the emblem text based on the length of the emblem
        """
        chiper_word = ""
        for char in text:
            if char >= 'A' and char <= 'Z':
                newChar = chr(((ord(char) - 65 + chiper_key)%26)+65)
                chiper_word += newChar
            else:
                chiper_word += char
        return chiper_word


class Kingdom:
    """
    Class Kindom, holds all the details of a Kingdom in Southeros
    """
    __kingdoms = dict()    # static variable to hold the list of all the kingdoms of Southeros
    def __init__(self, name, emblem):
        self.__kingdom_name = name
        self.__kingdom_emblem = emblem
        self.__ally_kingdoms = []
        Kingdom.__add_kingdom(self)
    
    @classmethod
    def get_kingdom(cls, name):
        """
        Class Method to get Kingdom Object from Name of Kingdom 
        """
        if name in cls.__kingdoms.keys():
            return cls.__kingdoms[name]
        else:
            raise Exception("Kindom not Found!")
    
    @classmethod
    def __add_kingdom(cls, kingdom):
        """
        Class Method to add Kingdom Object to the list of Kingdoms
        """
        cls.__kingdoms[kingdom.name()] = kingdom
    
    def get_allies(self):
        """
        Returns the list of Allies the Kingdom has
        """
        allies = []
        for kingdom in self.__ally_kingdoms:
            allies.append(kingdom.name())
        return allies
    
    def name(self):
        """
        Get the name of the kingdom
        """
        return self.__kingdom_name
    
    def emblem(self):
        """
        Get the emblem of the kingdom
        """
        return self.__kingdom_emblem

    def emblem_length(self):
        """
        Get the length of emblem of the kingdom
        """
        return len(self.emblem())
    
    def add_ally(self, otherKingdom):
        """
        Adds the passed kingdom ally of the caller Kingdom
        """
        if otherKingdom.name() == None:
            raise Exception("Kindom not Found!")
        elif otherKingdom == self:
            raise Exception("Cannot add itself as ally")
        else:
            if not self.is_ally(otherKingdom):
                self.__ally_kingdoms.append(otherKingdom)
                otherKingdom.add_ally(self)

    def is_ally(self, otherKingdom):
        """
        Checks if the passed Kingdom is ally of the Caller Kingdom
        """
        return otherKingdom in self.__ally_kingdoms

    def total_allies(self):
        """
        Return the total count of Allies a Kingdom has
        """
        return len(self.__ally_kingdoms)

    def send_message(self, message):
        """
        Sends Message to Other Kingdom. If the message response if True,
        Adds the both sender and reciever Kingdoms as Allies 
        """
        otherKingdom = message.get_receiver()
        if otherKingdom == self:
            raise Exception("Cannot send message to itself")
        
        response = MessageVerify.verify(otherKingdom, message.get_message())
        
        if response:
            self.add_ally(otherKingdom)
        
        return response

    def is_ruler(self):
        """
        Checks if the Kingdom is a ruling Kingdom
        """
        return self.total_allies() >= 3

    @classmethod
    def get_all(cls):
        """
        Class Method to iterate over all the Kingdoms
        """
        for kingdom_name in cls.__kingdoms.keys():
            yield cls.__kingdoms[kingdom_name]
        
    @classmethod
    def get_ruler(cls):
        """
        Class Method to get the Ruler of all Kingdoms
        """
        for kingdom in cls.get_all():
            if kingdom.is_ruler():
                return kingdom
        return None
    
    @classmethod
    def remove_all_kingdoms(cls):
        """
        Removes all the Kingdoms
        """
        for kingdom in cls.get_all():
            del kingdom
        cls.__kingdoms.clear()

    


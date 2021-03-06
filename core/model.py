# first commit
__name__ = "model"


class AppException(Exception):
    """ Custom exception class """
    def __init__(self,value):
        self.message = value

    def __str__(self):
        return repr(self.message)

class User:
    """ class represents Facebook user """
    def __init__(self):
        """ constructor """
        self.id = None
        self.name = None
        self.gender = None
        self.relationship_status = None
        self.hometown = None
        self.location = None
        self.religion = None
        self.birthday = None
        self.zodiac = None
        self.favorite_athletes = None
        self.education = None
        self.sports = None
        self.languages = None
        self.work = None
        self.favorite_teams = None
        self.work = None
        self.education = None
        self.age = None
    
    def __str__(self):
        """ toString representation """
        return str(self.name)
        

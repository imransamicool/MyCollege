
class IdCheckException(Exception):
    """This exception has to be raised if the csv store has a duplicate id in it already
     what is entered by the user during input of a new student"""
    pass


class AgeCheckException(Exception):
    """This exception to be raised if the user enters the age of student and
    same is less than eight years meaning the entered student can be admitted to college"""
    pass

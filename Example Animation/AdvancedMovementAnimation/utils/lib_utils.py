#used for creating static functions
class StaticFunction():
    def __init__(self, function):
        self.__call__ = function
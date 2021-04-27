
class Singleton():
    """
    Example on singleton class
    """
    # private class variable to store the instance
    _instance = None

    # dunder to set the _instance if there is none that is initiated else is simply returned
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example
ex_single1 = Singleton()
ex_single2 = Singleton()
# id is to check whether the memory address for both the instances are the same
print('is first instance the same with second instance:', id(ex_single1) == id(ex_single2))

class Singleton:
    def __new__(cls, *args, **kwargs):
        if "_instance" not in vars(cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

    def getInstanceWithValue(self):
        return f"{self}, {self.value}"


bigBoom = Singleton(5)
nextBigBoom = Singleton(69)

print("\nReal singleton results")
print(bigBoom.getInstanceWithValue())
print(nextBigBoom.getInstanceWithValue())
print(bigBoom == nextBigBoom)
print(bigBoom.getInstanceWithValue() == nextBigBoom.getInstanceWithValue())


# Not real Singleton, two different objects pointing to the same attribute
class NotSingleton:
    __instance = None

    def __init__(self, value):
        if NotSingleton.__instance is None:
            NotSingleton.__instance = self
        self.value = value

    def getInstance(self):
        return NotSingleton.__instance

    def getInstanceWithValue(self):
        try:
            if self.value:
                return f"{self}, {self.value}"
        except:
            return NotSingleton.__instance

biggerBoom = NotSingleton(5)
nextBiggerBoom = NotSingleton(69)

print("\nNot real singleton results")
print(biggerBoom.getInstanceWithValue())
print(nextBiggerBoom.getInstanceWithValue())
print(biggerBoom == nextBiggerBoom)
# two objects pointing to same attribute
print(biggerBoom.getInstance() == nextBiggerBoom.getInstance())
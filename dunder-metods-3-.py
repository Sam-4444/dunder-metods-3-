class person1:

    def __init__(self):
        self.name = "sam"
        self.number = 44
        self.age = 33


p1 = person1()
print(p1.__dict__)
p2 = person1()
print(p2.__dict__)
print(p1.__dict__ is p2.__dict__)


class person2:
    __slots__ = ["name", "number", "age"]

    def __init__(self):
        self.name = "sam"
        self.number = 44
        self.age = 33


p1 = person2
print(p1.__slots__)
p2 = person2
print(p2.__slots__)
print(p1.__slots__ is p2.__slots__)

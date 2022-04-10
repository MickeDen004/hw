class Nikolai:
    """
    Class of person
    """

    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        """Constructor"""
        super(Nikolai, self).__setattr__("age", age)
        if name == "Николай":
            super(Nikolai, self).__setattr__("name", name)
        else:
            line = f" Непраильное имя: {name}. Правильное - Николай"
            super(Nikolai, self).__setattr__("name", line)


person_1 = Nikolai("Николай", 89)
print(person_1.name, person_1.age)
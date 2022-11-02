class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Person:
    def __init__(self):
        self.name = "Human"

    def talk(self):
        return "talk"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        # TODO: fill this
        self.obj = obj
        self.adapted_methods = adapted_methods

    def __getattr__(self, attr):
        # TODO: fill this
        if attr in self.adapted_methods.keys():
            return getattr(self.obj, self.adapted_methods[attr])
        return getattr(self.obj, attr)


if __name__ == "__main__":
    dog = Dog()
    talkable = Adapter(dog, talk='bark')
    print(talkable.name)
    print(talkable.talk())

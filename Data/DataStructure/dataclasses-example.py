from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    """
    Example on dataclasses ~ struct , only available on python 3.7 above.
    source = https://www.youtube.com/watch?v=vRVVyl9uaZc, Arjan Codes
    """

    sort_index: int = field(init=False, repr=False)  # init False to exclude sort_index from init, repr false to exclude var from repr
    name: str
    job: str
    age: int
    strength: int = 100  # example on default value

    # this dunder is called after __init__
    def __post_init__(self):
        # this is workaround for frozen=True, as you cannot assign object directly
        # self.sort_index = self.strength will fail
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f'{self.name}, {self.job} ({self.age})'


if __name__ == '__main__':
    person1 = Person('Geralt', 'Witcher', 30, 99)
    person2 = Person('Yennefer', 'Sorceress', 25)
    person3 = Person('Yennefer', 'Sorceress', 25)
    print(id(person2))
    print(id(person3))
    print(person2 is person3)
    print(person1)
    print(person1 > person2)

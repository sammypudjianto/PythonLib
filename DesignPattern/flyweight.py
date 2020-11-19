
class SimpleFlyWeight():
    """
    principle: predefined the values and reuse it time to time
    """
    def __init__(self):
        self.grades = [letter + suffix for letter in 'ABCD' for suffix in ('+', '', '-')] + ['F']

    def compute_grade(self, percent):
        percent = max(59, min(99, percent))
        return self.grades[(99-percent) * 3 // 10]


class DynamicFlyWeight():
    _instances = {}

    def __new__(cls, percent):
        percent = max(50, min(99, percent))
        letter = 'FDCBA'[(percent - 50) // 10]
        self = cls._instances.get(letter)
        if self is None:
            self = cls._instances[letter] = object.__new__(DynamicFlyWeight)
            self.letter = letter
        return self

    def __repr__(self):
        return 'Grade {!r}'.format(self.letter)


if __name__ == '__main__':
    simple_example = SimpleFlyWeight()
    print('equivalent grade for 0:', simple_example.compute_grade(0))
    print('equivalent grade for 99:', simple_example.compute_grade(99))
    print('equivalent grade for 77:', simple_example.compute_grade(75))
    print(
        DynamicFlyWeight(55),
        DynamicFlyWeight(85),
        DynamicFlyWeight(95),
        DynamicFlyWeight(100))
    print(len(DynamicFlyWeight._instances))
    print(DynamicFlyWeight(99), DynamicFlyWeight(100))
    print(len(DynamicFlyWeight._instances))
    print(DynamicFlyWeight(75))
    print(len(DynamicFlyWeight._instances))

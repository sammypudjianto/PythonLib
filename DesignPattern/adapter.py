"""
Common pattern to bridge between different expected interface.
Think of it as electric UK-EU power adapter.

The following is classic adaptation from [FREEMAN] p 238 - 240.
The task is to make the turkey behaves like a duck.
"""


class Duck:
    def quack(self):
        print('Quack')

    def fly(self):
        print('I\'m flying')


class Turkey:
    def gobble(self):
        print('gobble')

    def fly(self):
        print('I\'m flying a short distance')


class DuckAdapter:
    # passing the adaptee , e.g. Turkey, as the argument
    # this example is super rough as is pretty much coupled with Turkey
    # When re-implementing this , you might want to put the argument as abstraction.
    def __init__(self, tky: Turkey):
        self.turkey = tky

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


d = Duck()
t = Turkey()
d_pretender = DuckAdapter(t)

# Call the same function as a duck
print('Calling the duck')
d.quack()
d.fly()

print('\n Calling the Turkey')
t.gobble()
t.fly()

# Call the same function as duck
print('\n Calling the Turkey to behave as a duck')
d_pretender.quack()
d_pretender.fly()

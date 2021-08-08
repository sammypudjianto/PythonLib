"""
This module shows different error raise due to variable scope
"""
def a():
    print(x)
    # will raise NameError: name 'x' is not defined
    # if there is no global x before or after the function

def b():
    print(x)
    x = 1
    # will raise UnboundLocalError: local variable 'x' referenced before assignment
    # regardless if there is  global variable x or not


x = 0
def c():
    print(x)
    # will print 0


def d():
    global x
    print(x)
    x = 2
    print(x)
    # will print 0


def e():
    enc = 2

    def f():
        print(enc)

    f()


if __name__ == '__main__':
    e()

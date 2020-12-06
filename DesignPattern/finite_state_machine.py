from abc import ABC, abstractmethod


class Node(ABC):

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def transition(self):
        pass


class NodeA(Node):
    def __init__(self):
        self.name = 'NodeA'

    def action(self):
        print(self.name)

    def transition(self):
        pass


class NodeB(Node):
    def __init__(self):
        pass

    def action(self):
        print(self.name)

    def transition(self):
        pass


class StateMachine():
    def __init__(self):
        self.curr_node = NodeA()

    def run(self):
        self.curr_node.do()
        self.curr_node = self.


if __name__ == '__main__':
    print(__name__)
    o = ThirdParty
    run = True
    s = input('Enter your message\n')
    print(s)

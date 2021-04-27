from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, publisher, *args, **kwargs):
        pass


class Publisher:
    def __init__(self):
        # put the list of
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def del_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self, *args, **kwargs):
        for ob in self.__observers:
            ob.update(self, *args, **kwargs)


class ObsExample(Observer):
    def update(self, publisher, *args, **kwargs):
        print('--updating ', id(self), ':', *args, ' ', kwargs)


# ------------EXAMPLE
if __name__ == '__main__':
    p = Publisher()
    for _ in range(3):
        p.add_observer(ObsExample())

    p.notify_observer('olala', j='jala')

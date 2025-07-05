import abc


class AbstractClass(abc.ABC):
    @abc.abstractmethod
    def thismethod(self):
        raise NotImplementedError()
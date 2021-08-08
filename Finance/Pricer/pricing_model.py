from abc import ABCMeta, abstractmethod


class PricingModel(metaclass=ABCMeta):
    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def calculate_delta(self):
        pass

    @abstractmethod
    def calculate_gamma(self):
        pass

    @abstractmethod
    def calculate_vega(self):
        pass

    @abstractmethod
    def calculate_theta(self):
        pass

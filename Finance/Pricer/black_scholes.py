import numpy as np
from pricing_model import PricingModel
from scipy.stats import norm


class BlackScholes(PricingModel):
    """
    with BS model
    """
    def __init__(
            self,
            spot,
            interest_rate,
            vol,
            div_yield,
            repo_rate,
            dt,
            strike,
            c_or_p):
        self.spot = spot
        self.interest_rate = interest_rate
        self.vol = vol
        self.div_yield = div_yield
        self.repo_rate = repo_rate
        self.dt = dt
        self.strike = strike
        self.c_or_p = c_or_p

    def df(self):
        return np.exp(-self.interest_rate * self.dt)

    def d1(self):
        numerator = (
            np.log(self.spot/self.strike) +
            (
                self.interest_rate -
                self.div_yield -
                self.repo_rate +
                0.5 * self.vol ** 2) * self.dt)
        denumerator = self.vol * np.sqrt(self.dt)
        return numerator/denumerator

    def d2(self):
        numerator = (
            np.log(self.spot/self.strike) +
            (
                self.interest_rate -
                self.div_yield -
                self.repo_rate -
                0.5 * self.vol ** 2) * self.dt)
        denumerator = self.vol * np.sqrt(self.dt)
        return numerator/denumerator

    def calculate_price(self):
        if self.c_or_p == 'C':
            return self.df() * (
                self.spot *
                np.exp((-self.div_yield - self.repo_rate) * self.dt) *
                norm.cdf(self.d1()) -
                self.strike * norm.cdf(self.d2()))
        elif self.c_or_p == 'P':
            return self.df() * (
                self.strike * norm.cdf(-self.d2()) -
                self.spot *
                np.exp((-self.div_yield - self.repo_rate) * self.dt) *
                norm.cdf(-self.d1()))

    def calculate_delta(self):
        if self.c_or_p == 'C':
            return norm.cdf(self.d1())
        elif self.c_or_p == 'P':
            return norm.cdf(-self.d1())

    def calculate_vega(self):
        return self.spot * norm.pdf(self.d1()) * np.sqrt(self.dt)

    def calculate_gamma(self):
        return norm.pdf(self.d1()) / (self.spot * self.vol * np.sqrt(self.dt))

    def calculate_theta(self):
        if self.c_or_p == 'C':
            return (
                -self.spot * norm.pdf(self.d1) * self.vol/ (2 * np.sqrt(self.dt))
                - self.interest_rate * self.strike * self.df() * norm.cdf(self.d2())
                )
        elif self.c_or_p == 'P':
            return (
                -self.spot * norm.pdf(self.d1) * self.vol/ (2 * np.sqrt(self.dt))
                + self.interest_rate * self.strike * self.df() * norm.cdf(-self.d2())
                )

    def calculate_rho(self):
        if self.c_or_p == 'C':
            return (
                self.strike * self.dt * self.df() * norm.cdf(self.d2()))
        elif self.c_or_p == 'P':
            return (
                -self.strike * self.dt * self.df() * norm.cdf(-self.d2()))


if __name__ == '__main__':
    spot = 1
    r = 0.0
    v = 0.2
    div = 0
    repo = 0
    dt = 1
    strike = 1
    cp = 'C'
    b = BlackScholes(
        spot=spot,
        interest_rate=r,
        vol=v,
        div_yield=div,
        repo_rate=repo,
        dt=dt,
        strike=strike,
        c_or_p=cp)

    print('a', b.calculate_price())

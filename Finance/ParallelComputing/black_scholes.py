import numpy as np


class BlackScholes():
    """
    BlackScholesMerton calculator
    """
    def __init__(
            self,
            initial_spot,
            strike,
            interest_rate,
            volatility,
            annualized_time_to_maturity,
            call_or_put='C',
            european_or_american='E'
            ):
        self.s0 = initial_spot
        self.k = strike
        self.r = interest_rate
        self.vol = volatility
        self.maturity = annualized_time_to_maturity
        self.c_or_p = call_or_put
        self.e_or_a = european_or_american

    def pv_mc(self, num_steps, num_paths):
        dt = self.maturity / num_steps
        rand = np.random.standard_normal((num_steps+1, num_paths))
        s = np.zeros((num_steps+1, num_paths))
        s[0] = self.s0

        for t in range(1, num_steps+1):
            s[t] = s[t-1] * np.exp(
                (self.r - 0.5 * self.vol ** 2) * dt
                + self.vol * np.sqrt(dt) * rand[t]
            )

        pv = (
            np.exp(-self.r * self.maturity)
            * np.sum(np.maximum(0, s[-1] - self.k) / num_paths)
        )
        return pv

    def pv(self):
        pass

    def delta(self):
        pass

    def vega(self):
        pass

    def gamma(self):
        pass

    def theta(self):
        pass

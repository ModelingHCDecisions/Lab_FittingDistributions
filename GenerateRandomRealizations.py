import deampy.random_variates as rvgs
import numpy as np

# a random number generator
rng = np.random.RandomState(seed=0)

# gamma
gamma = rvgs.Gamma(shape=0.9835458832943496,
                   scale=1.9199027077975956,
                   loc=0)
# generate 10 realizations from gamma
print('Realizations from gamma:')
for i in range(10):
    print(gamma.sample(rng))

# gamma-Poisson
gammaPoisson = rvgs.GammaPoisson(shape=0.3693765965041004,
                                 scale=9.154827879319111,
                                 loc=0)
# generate 10 realizations from gamma-Poisson
print('Realizations from gamma-Poisson:')
for i in range(10):
    print(gammaPoisson.sample(rng))

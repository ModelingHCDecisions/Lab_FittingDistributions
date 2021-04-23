import SimPy.RandomVariateGenerators as RVGs

# fitting an exponential distribution
exp_params = RVGs.Exponential.fit_mm(mean=10)
print('Parameters of exponential distribution:', exp_params)

# fitting a beta distribution
beta_params = RVGs.Beta.fit_mm(mean=20,
                               st_dev=5,
                               minimum=0,
                               maximum=50)
print('Parameters of beta distribution:', beta_params)

# fitting a Poisson distribution
poisson_params = RVGs.Poisson.fit_mm(mean=20)
print('Parameters of Poisson distribution', poisson_params)

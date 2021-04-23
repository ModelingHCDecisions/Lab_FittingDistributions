import SimPy.InOutFunctions as IO
import SimPy.Plots.Histogram as Hist
import SimPy.Plots.ProbDist as Plot
import SimPy.RandomVariateGenerators as RVGs
import SimPy.Statistics as Stat

# read weekly number of drinks
cols = IO.read_csv_cols(file_name='dataNumOfDrinks.csv',
                        n_cols=1,
                        if_ignore_first_row=True,
                        if_convert_float=True)

# make a histogram
Hist.plot_histogram(data=cols[0],
                    title='Weekly Number of Drinks',
                    bin_width=1)

# mean and standard deviation
stat = Stat.SummaryStat(name='Weekly number of drinks',
                        data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

# fit a Poisson distribution
fit_results = RVGs.Poisson.fit_ml(data=cols[0])
print('Fitting a Poisson distribution:', fit_results)

# plot the fitted Poisson distribution
Plot.plot_poisson_fit(data=cols[0], fit_results=fit_results, x_label='Weekly number of drinks', bin_width=1)

# fit a gamma-Poisson distribution
fit_results = RVGs.GammaPoisson.fit_ml(data=cols[0])
print('Fitting a gamma-Poisson distribution:', fit_results)

# plot the fitted gamma-Poisson distribution
Plot.plot_gamma_poisson_fit(data=cols[0], fit_results=fit_results, x_label='Weekly number of drinks', bin_width=1)

# fit a beta-binomial distribution
fit_results = RVGs.BetaBinomial.fit_ml(data=cols[0])
print('Fitting a beta-binomial distribution:', fit_results)

# plot the fitted beta-binomial distribution
Plot.plot_beta_binomial_fit(data=cols[0], fit_results=fit_results, x_label='Weekly number of drinks', bin_width=1)

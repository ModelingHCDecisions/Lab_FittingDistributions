import deampy.in_out_functions as io
import deampy.plots.histogram as hist
import deampy.plots.prob_dists as plot_dist
import deampy.random_variates as RVGs
import deampy.statistics as stats

# read weekly number of drinks
cols = io.read_csv_cols(file_name='dataNumOfDrinks.csv',
                        n_cols=1,
                        if_ignore_first_row=True,
                        if_convert_float=True)

# make a histogram
hist.plot_histogram(data=cols[0],
                    title='Weekly Number of Drinks',
                    bin_width=1)

# mean and standard deviation
stat = stats.SummaryStat(name='Weekly number of drinks',
                         data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

# fit a Poisson distribution
fit_results = RVGs.Poisson.fit_ml(data=cols[0])
print('Fitting a Poisson distribution:', fit_results)

# plot the fitted Poisson distribution
plot_dist.plot_poisson_fit(
    data=cols[0], fit_results=fit_results, x_label='Weekly number of drinks', x_range=(0, 40), bin_width=1)

# fit a gamma-Poisson distribution
fit_results = RVGs.GammaPoisson.fit_ml(data=cols[0])
print('Fitting a gamma-Poisson distribution:', fit_results)

# plot the fitted gamma-Poisson distribution
plot_dist.plot_gamma_poisson_fit(
    data=cols[0], fit_results=fit_results, x_label='Weekly number of drinks', x_range=(0, 40), bin_width=1)

# fit a beta-binomial distribution
fit_results = RVGs.BetaBinomial.fit_ml(data=cols[0])
print('Fitting a beta-binomial distribution:', fit_results)

# plot the fitted beta-binomial distribution
plot_dist.plot_beta_binomial_fit(
    data=cols[0], fit_results=fit_results, x_label='Weekly number of drinks', x_range=(0, 40), bin_width=1)

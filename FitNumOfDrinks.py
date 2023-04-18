import deampy.in_out_functions as io
import deampy.plots.histogram as hist
import deampy.plots.prob_dists as plot_dist
import deampy.random_variates as rvgs
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

print('Fitting a Poisson distribution:', fit_results)

# plot the fitted Poisson distribution

# fit a gamma-Poisson distribution

print('Fitting a gamma-Poisson distribution:', fit_results)

# plot the fitted gamma-Poisson distribution

# fit a beta-binomial distribution

print('Fitting a beta-binomial distribution:', fit_results)

# plot the fitted beta-binomial distribution

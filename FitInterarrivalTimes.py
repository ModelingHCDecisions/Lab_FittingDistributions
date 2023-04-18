import deampy.in_out_functions as io
import deampy.plots.histogram as hist
import deampy.plots.prob_dists as plot_dist
import deampy.random_variates as rvgs
import deampy.statistics as stats

# read interarrival times
cols = io.read_csv_cols(file_name='dataInterarrivalTimes.csv',
                        n_cols=1,
                        if_ignore_first_row=True,
                        if_convert_float=True)

# make a histogram
hist.plot_histogram(data=cols[0],
                    title='Interarrival Times (Minutes)',
                    bin_width=0.5)

# mean and standard deviation
stat = stats.SummaryStat(name='Interarrival times',
                         data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

# fit an exponential distribution

print('Fitting an exponential distribution:', fit_results)

# plot the fitted exponential distribution


# fit a gamma distribution

print('Fitting a gamma distribution:', fit_results)

# plot the fitted gamma distribution

# fit a log-normal distribution

print('Fitting a log-normal distribution:', fit_results)

# plot the fitted log-normal distribution
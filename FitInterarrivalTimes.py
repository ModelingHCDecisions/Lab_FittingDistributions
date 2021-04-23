import SimPy.InOutFunctions as IO
import SimPy.Plots.Histogram as Hist
import SimPy.Plots.ProbDist as Plot
import SimPy.RandomVariateGenerators as RVGs
import SimPy.Statistics as Stat

# read interarrival times
cols = IO.read_csv_cols(file_name='dataInterarrivalTimes.csv',
                        n_cols=1,
                        if_ignore_first_row=True,
                        if_convert_float=True)

# make a histogram
Hist.plot_histogram(data=cols[0],
                    title='Interarrival Times (Minutes)',
                    bin_width=0.5)

# mean and standard deviation
stat = Stat.SummaryStat(name='Interarrival times',
                        data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

# fit an exponential distribution
fit_results = RVGs.Exponential.fit_ml(data=cols[0])
print('Fitting an exponential distribution:', fit_results)

# plot the fitted exponential distribution
Plot.plot_exponential_fit(data=cols[0], fit_results=fit_results, x_label='Interarrival Times', bin_width=0.5)


# fit a gamma distribution
fit_results = RVGs.Gamma.fit_ml(data=cols[0])
print('Fitting a gamma distribution:', fit_results)

# plot the fitted gamma distribution
Plot.plot_gamma_fit(data=cols[0], fit_results=fit_results, x_label='Interarrival Times', bin_width=0.5)

# fit a log-normal distribution
fit_results = RVGs.LogNormal.fit_ml(data=cols[0])
print('Fitting a log-normal distribution:', fit_results)

# plot the fitted log-normal distribution
Plot.plot_lognormal_fit(data=cols[0], fit_results=fit_results, x_label='Interarrival Times', bin_width=0.5)
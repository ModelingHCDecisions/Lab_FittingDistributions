from SimPy import InOutFunctions as InOutSupport
from SimPy import FigureSupport as Fig
from SimPy import StatisticalClasses as Stat
from SimPy import FittingProbDist_ML as FitML

# read interarrival times
cols = InOutSupport.read_csv_cols(file_name='dataInterarrivalTimes.csv',
                                  n_cols=1,
                                  if_ignore_first_row=True,
                                  if_convert_float=True)

# make a histogram
Fig.graph_histogram(data=cols[0],
                    title='Interarrival Times (Minutes)',
                    bin_width=0.5
                    )

# mean and standard deviation
stat = Stat.SummaryStat(name='Interarrival times',
                        data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

# fit an exponential distribution
fit_results = FitML.fit_exp(data=cols[0],
                            x_label='Interarrival Times',
                            bin_width=0.5)
print('Fitting an exponential distribution:', fit_results)

# fit a gamma distribution
fit_results = FitML.fit_gamma(data=cols[0],
                              x_label='Interarrival Times',
                              bin_width=0.5)
print('Fitting a gamma distribution:', fit_results)

# fit a log-normal distribution
fit_results = FitML.fit_lognorm(data=cols[0],
                                x_label='Interarrival Times',
                                bin_width=0.5)
print('Fitting a log-normal distribution:', fit_results)

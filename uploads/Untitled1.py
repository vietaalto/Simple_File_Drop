def histogram_mean(data, hist_cols):
    x = np.array([re.findall(r'\d+', x)[0] for x in hist_cols]).astype(int)
    y = data[hist_cols].values
    # Mean value of a histogram is the weighted average of the bins (bin locations)
    mean = (x * y).sum(axis=1) / y.sum(axis=1)
    return mean

def histogram_std(data, hist_cols):
    x = np.array([re.findall(r'\d+', x)[0] for x in hist_cols]).astype(int)
    y = data[hist_cols].values
    # Variance of a histogram is the weighted average of squared bin distances from the mean
    mean = histogram_mean(data, hist_cols)
    var = (y * (np.tile(x, (len(y), 1)) - mean.reshape(-1, 1))**2).sum(axis=1) / y.sum(axis=1)
    std = np.sqrt(var)
    return std

Usage example:
histogram_mean(data, [f'TIMING_ADV_BIN_{x}' for x in range(1, 31)])
######
nest_list = []
create nest_list:
    res.plit(_LEVEL_)
    nest_list.append(other list)
def histogram(x,y):
    return dataframe( cols = (___mean, std, median ...), index = data.index)

for z in nested list [[PUSCH..],[PUCCH...], ...]
 # z = cols with form PUSCH_level_
 x = # level of bin for cols in z ...
 y = # bin data (data0[z].values) over CELLID, PERIOD_START_TIME
 df = histogram()
 data0.join(df)
 cols['new_kpi'] = col'kpi']drop(z). add(df.col. name)

#change new_kpi in the lag feature & wavelet.

#can only drop PERIOD_START_TIME after creating cv fold

from numpy import *

"""
WRITTEN BY:
Nicklas Hansen
"""

def timeseries(epochs, full, epoch_length, overlap_factor, sample_rate):
	window = int(epoch_length - ( epoch_length / overlap_factor))
	length = int(full[-1].index_stop/sample_rate)
	y, yhat, wake, rem, illegal = zeros(length), zeros(length), zeros(length), zeros(length), zeros(length)
	for i,obj in enumerate(epochs):
		if obj.y is not None:
			y = modify_timeseries(y, obj.y, 1, obj.timecol, window, sample_rate)
		yhat = modify_timeseries(yhat, obj.yhat, 1, obj.timecol, window, sample_rate)
	for i,obj in enumerate(full):
		sleep = transpose(obj.X)[-1]
		wake = modify_timeseries(wake, sleep, -1, obj.timecol, window, sample_rate)
		rem = modify_timeseries(rem, sleep, 1, obj.timecol, window, sample_rate)
		illegal = modify_timeseries(illegal, obj.mask, 1, obj.timecol, window, sample_rate)
	for i in range(len(wake)):
		if illegal[i] == 1 and wake[i] == 1:
			illegal[i] = 0
	return y, yhat, wake, rem, illegal

def modify_timeseries(ts, values, criteria, timecol, window, sample_rate):
	for i,y in enumerate(values[window:]):
		enum = [int(timecol[window+i-3]/sample_rate),int(timecol[window+i]/sample_rate)]
		if enum[0] > enum[1]:
			enum[0] = 0
		if y == criteria:
			for j in range(enum[0],enum[1]):
				ts[j] = 1
	return ts

def region(array):
	regions, start, bin = [], 0, False
	for i,val in enumerate(array):
		if val == 1:
			if not bin:
				start, bin = i, True
		elif bin:
			bin = False
			regions.append([start, i-1])
	if bin:
		regions.append([start, i-1])
	return regions
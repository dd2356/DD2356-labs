import numpy as np
import matplotlib.pyplot as plt

sizes = [1000, 5000, 10000, 50000, 100000][1:2]

arithmetic_names = ["bench_results_%d_arithmetic.txt" % n for n in sizes]
# harmonic_names = ["bench_results_%d_harmonic.txt" % n for n in sizes]

for col, filename in enumerate(arithmetic_names):
	fig, ax = plt.subplots(1, 1)#len(sizes))
	ax = [ax]
	col = 0
	print(col)
	times = np.loadtxt(filename)
	min_val = times.min()
	max_val = times.max()
	mean_val = times.mean()
	median_val = np.median(times)
	perc_95 = np.percentile(times, 95)
	print(times)
	ax[col].hist(times, bins = 100)
	lims = ax[col].get_ylim()
	lims = (0.1, lims[1])
	ax[col].plot([max_val, max_val], [0, 20000], '--', label = "maximum")
	ax[col].plot([min_val, min_val], [0, 20000], '--', label = "minimum")
	ax[col].plot([mean_val, mean_val], [0, 20000], ':', label = "average")
	ax[col].plot([median_val, median_val], [0, 20000], '-', label = "median")
	ax[col].plot([perc_95, perc_95], [0, 20000], '-.', label = "95% quantile")
	ax[col].set_title("Histogram of CPU cycles needed for N = 5000")
	ax[col].set_xlabel("CPU cycles")
	ax[col].set_ylabel("Count")
	ax[col].set_ylim(lims)
	# ax[col].set_yscale("log")
	print(lims)
	plt.legend()
	plt.show()


print(np.mean(times))
print(np.var(times))

sizes = [1000, 5000, 10000, 50000, 100000]

arithmetic_names = ["bench_results_%d_arithmetic.txt" % n for n in sizes]
average_times = []
percs_05 = []
percs_95 = []
percs_99 = []
max_vals = []
min_vals = []

for col, filename in enumerate(arithmetic_names):
	times = np.loadtxt(filename)
	min_val = times.min()
	max_val = times.max()
	mean_val = times.mean()
	median_val = np.median(times)
	perc_05 = np.percentile(times, 5)
	perc_95 = np.percentile(times, 95)
	perc_99 = np.percentile(times, 99)
	average_times.append(median_val)
	percs_05.append(perc_05)
	percs_95.append(perc_95)
	percs_99.append(perc_99)
	max_vals.append(max_val)
	min_vals.append(min_val)

plt.loglog(sizes, average_times, label = "average")
plt.loglog(sizes, percs_05, label = "5% quantile")
plt.loglog(sizes, percs_95, label = "95% quantile")
plt.loglog(sizes, percs_99, label = "99% quantile")
plt.loglog(sizes, max_vals, label = "maximum")
plt.loglog(sizes, min_vals, label = "minimum")
plt.legend()
plt.xlabel("Problem size (N)")
plt.ylabel("Time (CPU cycles)")
plt.title("Execution time for increasing input size")
plt.show()

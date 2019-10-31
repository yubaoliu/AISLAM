""" In the first function, generate the normal distributed samples by summing up 12
 uniform distributed samples, as explained in the lecture
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
import timeit


def sample_normal_distribution(a, b, sample):
    s = 0
    for i in range(12):
        t = np.random.uniform(a, b, sample)
        s += t
    return s/(np.sqrt(sample*(b-a)**2/12))


def sample_normal_twelve(mu, sigma):
    x = 0.5 * np.sum(np.random.uniform(-sigma, sigma, 12))
    return mu+x


def evaluate_sampling_dist(mu, sigma, n_samples, sample_function):
    n_bins = 100
    samples = []
    for i in range(n_samples):
        samples.append(sample_function(mu, sigma))
    print("%30s : mean = %.3f, std_dev = %.3f" % (sample_function.__name__, np.mean(samples), np.std(samples)))
    plt.figure()
    count, bins, ignored = plt.hist(samples, n_bins, density=True)
    plt.plot(bins, stats.norm(mu, sigma).pdf(bins), linewidth=2, color='r')
    plt.xlim([mu - 5*sigma, mu + 5*sigma])
    plt.title(sample_function.__name__)


def evaluage_sampling_time(mu, sigma, n_samples, sample_function):
    tic = timeit.default_timer()
    for i in range(n_samples):
        sample_function(mu, sigma)
    toc = timeit.default_timer()
    time_per_sample = (toc-tic)/n_samples*1e6
    print("%30s : %.3f us" % (sample_function.__name__, time_per_sample))


def sample_normal_rejection(mu, sigma):
    interval = 5*sigma
    max_density = stats.norm(mu, sigma).pdf(mu)

    # Rejection loop
    while True:
        x = np.random.uniform(mu-interval, mu+interval, 1)[0]
        y = np.random.uniform(0, max_density, 1)
        if y<= stats.norm(mu, sigma).pdf(x):
            break
    return x


def sample_normal_boxmuller(mu, sigma):
    u = np.random.uniform(0, 1, 2)

    x = math.cos(2*np.pi*u[0])*math.sqrt(-2*math.log(u[1]))
    return mu + sigma * x


if __name__ == "__main__":
    mu, sigma = 0, 1
    sample_functions =[
        sample_normal_twelve,
        sample_normal_rejection,
        sample_normal_boxmuller
    ]

    for fnc in sample_functions:
        evaluage_sampling_time(mu, sigma, 1000, fnc)

    n_samples = 10000
    print("evaluting sample distances with:")
    print(" mean :", mu)
    print("std_dev :", sigma)
    print("samples :", n_samples)

    for func in sample_functions:
       evaluate_sampling_dist(mu, sigma, n_samples, func)
    plt.show()
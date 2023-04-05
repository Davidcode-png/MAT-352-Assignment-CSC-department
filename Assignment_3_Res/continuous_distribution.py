"""
    This script was written by computer science student 300 level.
    As an assignment submission for MAT353
"""

import numpy as np
import scipy as sp
import seaborn as sb
import matplotlib.pyplot as plt


def visualize_uniform_distribution():
    """This function visualizes a random variable of a uniform distrbution."""
    _, plot_axis = plt.subplots(2, 1)

    # uniformly select 90000 random samples between -1 and 1
    samples = np.random.uniform(-1, 1, 90000)

    # plot histogram of samples distribution
    _, bins, _ = plot_axis[0].hist(samples, bins=30, density=True)

    # draws line plot
    sb.histplot(samples, element='poly', fill=True, ax=plot_axis[1])

    # save visualisation
    plt.savefig(fname=plot_name("Uniform"))
    plt.close()


def visualize_normal_distribution():
    """This function visualizes a random variable of a normal distrbution."""

    _, plot_axis = plt.subplots(2, 1)

    # select 90000 random samples using the nomal distibution given a mean=0 and standard_deviation=0.1
    mean, standard_deviation = 0, 0.1
    samples = np.random.normal(loc=0, scale=0.1, size=90000)

    # plot histogram to show sample distribution
    _, bins, _ = plot_axis[0].hist(samples, 30, density=True)

    # draws line plot
    sb.histplot(samples, element='poly', fill=True, ax=plot_axis[1])

    # save visualisation
    plt.savefig(fname=plot_name("Normal"))
    plt.close()


def visualize_exponential_distibution():
    """This function visualizes a random variable of a exponential distrbution."""
    _, plot_axis = plt.subplots(2, 1)

    # select 90000 random samples using the exponential distribution
    samples = np.random.exponential(1, size=90000)

    # plot histogram to show sample distribution
    _, bins, _ = plot_axis[0].hist(samples, 30, density=True)

    # draws line plot
    sb.histplot(samples, element='poly', fill=True, ax=plot_axis[1])

    plt.savefig(fname=plot_name("Exponential"))
    plt.close()


def visualize_gamma_distribution():
    """This function visualizes a random variable of a gamma distrbution."""
    _, plot_axis = plt.subplots(2, 1)

    # select 90000 random samples using the nomal distibution given a mean=2 and standard_deviation=0.2
    mean, standard_deviation = 2, 0.2
    samples = np.random.gamma(mean, standard_deviation, size=90000)

    # plot histogram to show sample distribution
    _, bins, _ = plot_axis[0].hist(samples, 30, density=True)

    # # draws line to highlight approximate distribution shape
    # scale_y = bins**(mean-1)*(np.exp(-bins/standard_deviation)/(sp.special.gamma(mean)*standard_deviation**mean))
    # plt.plot(bins, scale_y, linewidth=2, color='g')

    # draws line plot
    sb.histplot(samples, element='poly', fill=True, ax=plot_axis[1])

    plt.savefig(fname=plot_name("Gamma"))
    plt.close()


def plot_name(dist_name):
    SAVE_DIR = "Assignment_3_Res/Graphs"

    return f"{SAVE_DIR}/(C)-{dist_name.title()}_distribution_visualization"


if __name__ == '__main__':
    visualize_uniform_distribution()
    visualize_normal_distribution()
    visualize_exponential_distibution()
    visualize_gamma_distribution()


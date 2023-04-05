import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
# sns.set_style("ticks", {'axes.grid' : False})

plt.rcParams['patch.linewidth'] = 0


def plot_bernuolli_graph():
    # Define the probability of success
    p = 0.7

    # Generate an array of values for x
    x = np.array([0, 1])

    # Define the sample sizes
    n_small = 10
    n_large = 1000

    # Generate the data for the small sample size
    data_small = bernoulli.rvs(p, size=n_small)
    hist_small, bins_small = np.histogram(data_small, bins=[-0.5, 0.5, 1.5], density=True)

    # Generate the data for the large sample size
    data_large = bernoulli.rvs(p, size=n_large)
    hist_large, bins_large = np.histogram(data_large, bins=[-0.5, 0.5, 1.5], density=True)

    # Create a grid of subplots
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))

    # Plot the small sample size data on the top subplot
    # axs[0].bar(x, pmf_small, label=f'Theoretical PMF, p = {p}')
    axs[0].bar(x, hist_small, alpha=0.5, label=f'Sample PMF, n = {n_small}')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('P(X=x)')
    axs[0].set_title('Bernoulli Distribution with n = {}'.format(n_small))
    axs[0].legend()

    # Plot the large sample size data on the bottom subplot
    # axs[1].bar(x, pmf_large, label=f'Theoretical PMF, p = {p}')
    axs[1].bar(x, hist_large, alpha=0.5, label=f'Sample PMF, n = {n_large}')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('P(X=x)')
    axs[1].set_title('Bernoulli Distribution with n = {}'.format(n_large))
    axs[1].legend()

    # Show the plot
    plt.tight_layout()
    plt.savefig(fname=plot_name("Bernoulli"))


def plot_binomial_graph():
    # Parameters for the binomial distribution
    n = 10
    p = 0.5

    n_large = 1000
    # Generate random samples for small sample size
    data_small = np.random.binomial(n, p, size=100)

    # Generate random samples for large sample size
    data_large = np.random.binomial(n_large, p, size=1000)

    # Create a figure with two subplots
    fig, axs = plt.subplots(2, 1, figsize=(6, 8))

    # Plot the binomial distribution with small sample size using Seaborn histplot
    sns.histplot(data_small, bins=np.arange(0, n + 2), stat='probability', kde=False, ax=axs[0])
    axs[0].set_title(f'Binomial Distribution (n={n}, p={p}) - Small Sample Size')
    axs[0].set_xlabel('Number of Successes')
    axs[0].set_ylabel('Probability')

    # Plot the binomial distribution with large sample size using Seaborn histplot
    sns.histplot(data_large, bins=np.arange(0, n_large + 2), kde=False, ax=axs[1])
    axs[1].set_title(f'Binomial Distribution (n={n_large}, p={p}) - Large Sample Size')
    axs[1].set_xlabel('Number of Successes')
    axs[1].set_ylabel('Count')

    # Zooming in

    axs[1].set_xlim(400, 600)

    # Show the legend
    axs[1].legend(labels=['Sample PMF'])

    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=0.4)

    # Save the plot
    plt.savefig(fname=plot_name("Binomial"))


def plot_geometric_graph():
    np.random.seed(1)

    # Generate random data for the geometric distribution
    p = 0.3  # probability of success
    sample_size = 1000  # sample size
    data = np.random.geometric(p, sample_size)

    # Create the histogram using seaborn
    sns.histplot(data, bins=np.arange(1, np.max(data) + 2) - 0.5, stat='probability', kde=False)
    plt.xlabel('Number of Trials')
    plt.ylabel('Probability')
    plt.title('Geometric Distribution (p=0.3)')
    # plt.savefig(fname='Geometric_distribution_visualization')
    plt.savefig(fname=plot_name("Geometric"))


def plot_poisson_graph():
    # Testing between the different lambda values
    lambda_small = 3
    lambda_large = 10

    # Generate data for smaller sample size
    data_small = np.random.poisson(lambda_small, size=1000)

    # Generate data for larger sample size
    data_large = np.random.poisson(1, size=1000)

    # Set up the figure with subplots
    fig, axs = plt.subplots(2, 1, figsize=(8, 8))

    # Plot histogram for smaller sample size
    sns.histplot(data_small, kde=False, color='skyblue', bins=range(0, 15), stat='probability', ax=axs[0])
    axs[0].set_title(f'Poisson Distribution (lambda = {lambda_small}) - Smaller Sample Size')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Frequency')

    # Plot histogram for larger sample size
    sns.histplot(data_large, kde=False, color='skyblue', bins=range(0, 15), stat='probability', ax=axs[1])
    axs[1].set_title(f'Poisson Distribution (lambda = {lambda_large}) - Larger Sample Size')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Frequency')

    plt.subplots_adjust(
        hspace=0.33)
    # Save the plot
    plt.savefig(fname=plot_name("Poisson"))


def plot_name(dist_name):
    SAVE_DIR = "Assignment_3_Res/Graphs"

    return f"{SAVE_DIR}/(D)-{dist_name.title()}_distribution_visualization"



if __name__ == '__main__':
    plot_bernuolli_graph()
    plot_binomial_graph()
    plot_geometric_graph()
    plot_poisson_graph()


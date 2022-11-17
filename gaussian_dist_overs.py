import numpy as np
import scipy
from matplotlib import pyplot as plt

from query_utils import filter_by_pitch_x_pitch_y, load_csv_data_mipl, merge_no_balls_and_wides


def get_runs_per_over_innings(data):
    total_runs = []
    for over in range(1, 21):
        over_data = data[data['over'] == str(over)]
        over_runs = sum(over_data.runs)
        total_runs.append(over_runs)

    return total_runs


def plot_gaussian_distribution(mean, std_dev, graph_color):
    x_min = 0.0
    x_max = mean * 3

    x = np.linspace(x_min, x_max, 1000)
    y = scipy.stats.norm.pdf(x, mean, std_dev)

    plt.plot(x, y, color=graph_color)


mipl_csv = load_csv_data_mipl()
mipl_csv = filter_by_pitch_x_pitch_y(mipl_csv)
mipl_csv[['innings', 'over', 'ball']] = mipl_csv['delivery'].str.split('.', 3, expand=True)

matches = mipl_csv.groupby('matchId')

i = 0
runs_per_over = []
for matchId, match in matches:
    first_innings = match[match['innings'] == "1"]
    first_innings = merge_no_balls_and_wides(first_innings)
    runs_per_over.append(get_runs_per_over_innings(first_innings))

    second_innings = match[match['innings'] == "2"]
    merge_no_balls_and_wides(second_innings)
    runs_per_over.append(get_runs_per_over_innings(second_innings))

    print(i)
    i += 1

plt.title('Gaussian Distribution')
plt.ylim(0, 0.2)
plt.xlabel('Runs')
plt.ylabel('Density')

i = 0
legend = []
colours = ['b', 'r', 'g', 'c', 'm', 'y', 'k']
for colour in colours:
    transposed = np.array(runs_per_over).T
    x_data = transposed[i]
    i_over = str(i + 1) + " Over"
    plot_gaussian_distribution(np.mean(x_data), np.std(x_data), colour)
    legend.append(i_over)
    i += 1

plt.legend(legend)
plt.show()

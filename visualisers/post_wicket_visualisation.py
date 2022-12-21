import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from data_processing.query_utils import load_csv_data_mipl, filter_by_pitch_x_pitch_y


def plot_heatmap(data, r):
    x_min = min(data[:, 0])
    x_max = max(data[:, 0])
    y_min = min(data[:, 1])
    y_max = max(data[:, 1])

    X, Y = np.mgrid[x_min:x_max:100j, y_min:y_max:100j]
    positions = np.vstack([X.ravel(), Y.ravel()])
    values = np.vstack([data[:, 0], data[:, 1]])
    kernel = gaussian_kde(values)
    Z = np.reshape(kernel(positions).T, X.shape)

    fig, ax = plt.subplots()
    fig.suptitle("Run " + str(r))
    ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r, extent=[x_min, x_max, y_min, y_max])
    # ax.plot(data[:, 0], data[:, 1], 'k.', markersize=2)

    STUMP_HEIGHT = 0.7112
    STUMP_GAP = 0.08893

    ax.set_ylim(-0.5, 2.5)
    ax.set_xlim(-2, 2)

    # Draw stumps
    x = [0, 0]
    y = [0, STUMP_HEIGHT]
    ax.plot(x, y, color='slategray', linewidth=3, zorder=10)

    x = [STUMP_GAP, STUMP_GAP]
    y = [0, STUMP_HEIGHT]
    ax.plot(x, y, color='slategray', linewidth=3, zorder=10)

    x = [-STUMP_GAP, -STUMP_GAP]
    y = [0, STUMP_HEIGHT]
    ax.plot(x, y, color='slategray', linewidth=3, zorder=10)


def plot_balls_stumps(data, colour):
    x_values = data.stumpsX
    y_values = data.stumpsY

    STUMP_HEIGHT = 0.7112
    STUMP_GAP = 0.08893

    plt.ylim(-0.5, 2.5)
    plt.xlim(-2, 2)

    # Draw stumps
    x = [0, 0]
    y = [0, STUMP_HEIGHT]
    plt.plot(x, y, color='slategray', linewidth=3, zorder=10)

    x = [STUMP_GAP, STUMP_GAP]
    y = [0, STUMP_HEIGHT]
    plt.plot(x, y, color='slategray', linewidth=3, zorder=10)

    x = [-STUMP_GAP, -STUMP_GAP]
    y = [0, STUMP_HEIGHT]
    plt.plot(x, y, color='slategray', linewidth=3, zorder=10)

    plt.scatter(x_values, y_values, s=0.2, color=colour)


mipl_csv = load_csv_data_mipl()
mipl_csv = filter_by_pitch_x_pitch_y(mipl_csv)
mipl_csv[['delivery_innings', 'delivery_over', 'delivery_ball']] = mipl_csv['delivery'].str.split('.', 3, expand=True)
# mipl_csv = mipl_csv[mipl_csv['extras'].isna()]

runs = mipl_csv.batterRuns.unique()

c = 0
colours = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'w']
for run in runs:
    run_data = mipl_csv[mipl_csv['batterRuns'] == run]

    # plt.title("Run " + str(run))
    # plot_balls_stumps(run_data, colours[c])
    # c += 1

    xy = np.array(run_data[['stumpsX', 'stumpsY']])
    plot_heatmap(xy, run)

    plt.show()

# bowled = mipl_csv[mipl_csv['dismissalDetails'].str[0] == "b"]
# plot_balls_stumps(bowled)

# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from query_utils import load_csv_data_mipl, filter_by_pitch_x_pitch_y


def plot_heatmap(data, r, hand):
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
    fig.suptitle(hand + " Run " + str(r))
    ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r, extent=[x_min, x_max, y_min, y_max])
    # ax.plot(data[:, 0], data[:, 1], 'k.', markersize=2)

    WICKET_LENGTH = 22.56
    WICKET_WIDTH = 3.66

    BATTING_CREASE_LENGTH = 1.22

    # Draw a pitch surface
    x = [WICKET_WIDTH / 2,
         -WICKET_WIDTH / 2,
         -WICKET_WIDTH / 2,
         WICKET_WIDTH / 2]
    y = [WICKET_LENGTH - BATTING_CREASE_LENGTH,
         WICKET_LENGTH - BATTING_CREASE_LENGTH,
         -BATTING_CREASE_LENGTH,
         -BATTING_CREASE_LENGTH]

    ax.plot(x, y, color='slategray', linewidth=3, zorder=10)


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

    rh = run_data[run_data.rightHandedBat == True]
    xy = np.array(rh[['pitchX', 'pitchY']])
    plot_heatmap(xy, run, "Right Handed")
    plt.show()

    lh = run_data[run_data.rightHandedBat == False]
    xy = np.array(lh[['pitchX', 'pitchY']])
    plot_heatmap(xy, run, "Left Handed")
    plt.show()

# bowled = mipl_csv[mipl_csv['dismissalDetails'].str[0] == "b"]
# plot_balls_stumps(bowled)

# plt.show()

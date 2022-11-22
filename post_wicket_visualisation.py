import matplotlib.pyplot as plt

from query_utils import load_csv_data_mipl, filter_by_pitch_x_pitch_y


def plot_balls_stumps(data):
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

    plt.scatter(x_values, y_values, s=0.2)


mipl_csv = load_csv_data_mipl()
mipl_csv = filter_by_pitch_x_pitch_y(mipl_csv)
mipl_csv[['delivery_innings', 'delivery_over', 'delivery_ball']] = mipl_csv['delivery'].str.split('.', 3, expand=True)

bowled = mipl_csv[mipl_csv['dismissalDetails'].str[0] == "b"]

plot_balls_stumps(bowled)
plt.show()

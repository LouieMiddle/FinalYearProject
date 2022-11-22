from matplotlib import pyplot as plt

from query_utils import filter_by_pitch_x_pitch_y, cumulative, load_csv_data_mipl, merge_no_balls_and_wides


def plot_innings(data, match_id, innings):
    total_runs = cumulative(data.runs)
    total_balls = range(1, len(data) + 1)

    plt.plot(total_balls, total_runs)
    plt.title("matchId " + str(match_id))
    plt.suptitle("innings " + str(innings))
    plt.show()


def plot_all_innings(data, colour):
    total_runs = cumulative(data.runs)
    total_balls = range(1, len(data) + 1)

    plt.plot(total_balls, total_runs, lw=0.5, color=colour)


def plot_all_innings_over_overs(data, colour):
    total_runs = []
    for over in range(1, 21):
        over_data = data[data['delivery_over'] == str(over)]
        over_runs = sum(over_data.runs)
        total_runs.append(over_runs)

    plt.plot(cumulative(total_runs), lw=0.5, color=colour)


mipl_csv = load_csv_data_mipl()
mipl_csv = filter_by_pitch_x_pitch_y(mipl_csv)
mipl_csv[['delivery_innings', 'delivery_over', 'delivery_ball']] = mipl_csv['delivery'].str.split('.', 3, expand=True)

matches = mipl_csv.groupby('matchId')

i = 0
colours = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'w']
for matchId, match in matches:
    plt.xlabel("balls/overs")
    plt.ylabel("runs")

    c = i % len(colours)
    if c == 0:
        if i != 0:
            plt.show()
        plt.figure(figsize=(10, 10))

    first_innings = match[match['delivery_innings'] == "1"]
    first_innings = merge_no_balls_and_wides(first_innings)
    # plot_innings(first_innings, matchId, 1)
    # plot_all_innings(first_innings, colours[c])
    plot_all_innings_over_overs(first_innings, colours[c])

    second_innings = match[match['delivery_innings'] == "2"]
    merge_no_balls_and_wides(second_innings)
    # plot_innings(second_innings, matchId, 2)
    # plot_all_innings(second_innings, colours[c])
    plot_all_innings_over_overs(second_innings, colours[c])

    print(i)
    i += 1

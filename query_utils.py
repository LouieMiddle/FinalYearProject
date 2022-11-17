import os.path

import pandas as pd


def cumulative(lists):
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length + 1)]
    return cu_list[1:]


def merge_no_balls_and_wides(data):
    return data


def filter_by_pitch_x_pitch_y(data):
    data = data[(data['pitchX'] >= -2) & (data['pitchX'] <= 2)]
    data = data[(data['pitchY'] >= 0) & (data['pitchY'] <= 14)]
    return data


def load_csv_data_mipl():
    csv_path = os.path.join("HawkeyeStats-main", "mensIPLHawkeyeStats.csv")
    return pd.read_csv(csv_path)

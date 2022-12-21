import json
import os.path

import numpy as np
import pandas as pd


def get_json_directory_names():
    path_to_json = '../ipl_2022_data/ball_by_ball'
    return [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


def load_json_data_mipl():
    json_files = get_json_directory_names()

    json_data = []
    for index, js in enumerate(json_files):
        with open(os.path.join('../ipl_2022_data/ball_by_ball', js)) as json_file:
            json_data.append(json.load(json_file))
            json_file.close()

    data = pd.json_normalize(json_data)

    return data


mipl_json = load_json_data_mipl()
print(mipl_json.columns)

bowler_count = mipl_json.match.bowlingTeam.bowler.name.value_counts()
batter_count = mipl_json.match.battingTeam.batsman.name.value_counts()
print(np.mean(bowler_count))
print(np.mean(batter_count))

# batsman_ball_type = mipl_json.pivot_table(columns=['batsman_name', "delivery_type"], aggfunc='size')
# batsman_ball_type.to_csv('Pre-processing-csvs/batsman_ball_type')

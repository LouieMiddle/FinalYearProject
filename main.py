import json
import os.path

import pandas as pd


def load_csv_data_mipl():
    csv_path = os.path.join("HawkeyeStats-main", "mensIPLHawkeyeStats.csv")
    return pd.read_csv(csv_path)


def get_json_directory_names():
    path_to_json = 'ipl_2022_data/data'
    return [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


def load_json_data_mipl():
    mipl_data = pd.DataFrame(columns=['batsman_name'])
    json_files = get_json_directory_names()

    for index, js in enumerate(json_files):
        with open(os.path.join('ipl_2022_data/data', js)) as json_file:
            json_text = json.load(json_file)
            match = json_text['match']['battingTeam']['batsman']['name']
            mipl_data.loc[index] = [match]

    return mipl_data


mipl_csv = load_csv_data_mipl()
# print(mipl_csv.head())
# print(mipl_csv.describe())

mipl_json = load_json_data_mipl()
print(mipl_json.describe())

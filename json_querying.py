import json
import os.path

import pandas as pd


def get_json_directory_names():
    path_to_json = 'ipl_2022_data/data'
    return [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


def load_json_data_mipl():
    mipl_data = pd.DataFrame(columns=['batsman_name', "batsman_id", "bowler_name", "bowler_id", "delivery_type",
                                      "shot_attacked", "shot_played", "shot_type_additional"])
    json_files = get_json_directory_names()

    for index, js in enumerate(json_files):
        with open(os.path.join('ipl_2022_data/data', js)) as json_file:
            json_text = json.load(json_file)
            batsman_name = json_text['match']['battingTeam']['batsman']['name']
            batsman_id = json_text['match']['battingTeam']['batsman']['id']
            bowler_name = json_text['match']['bowlingTeam']['bowler']['name']
            bowler_id = json_text['match']['bowlingTeam']['bowler']['id']
            delivery_type = json_text['match']['delivery']['deliveryType']
            shot_attacked = json_text['match']['delivery']['shotInformation']['shotAttacked']
            shot_played = json_text['match']['delivery']['shotInformation']['shotAttacked']
            shot_type_additional = json_text['match']['delivery']['shotInformation']['shotAttacked']
            mipl_data.loc[index] = [batsman_name, batsman_id, bowler_name, bowler_id, delivery_type,
                                    shot_attacked, shot_played, shot_type_additional]

    return mipl_data


mipl_json = load_json_data_mipl()

batsman_ball_type = mipl_json.pivot_table(columns=['batsman_name', "delivery_type"], aggfunc='size')
batsman_ball_type.to_csv('Pre-processing-csvs/batsman_ball_type')

# Visualiser (heat maps land and wicket passing) (swing and spin rate)
# Visualiser per ball / over for each ground etc.
# Need to separate spin balls and seam balls, so slow seam balls don't get lumped in with spin balls

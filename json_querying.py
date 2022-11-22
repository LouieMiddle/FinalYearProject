import json
import os.path

import pandas as pd

from query_utils import load_csv_data_mipl


def get_json_directory_names():
    path_to_json = 'ipl_2022_data/ball_by_ball'
    return [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


def load_json_data_mipl(columns):
    mipl_data = pd.DataFrame(columns=columns)
    json_files = get_json_directory_names()

    for index, js in enumerate(json_files):
        with open(os.path.join('ipl_2022_data/ball_by_ball', js)) as json_file:
            # json_str = json_file.read()
            # json_file.seek(0)
            json_dict = json.load(json_file)
            # ball_by_ball_schema = marshmallow_dataclass.class_schema(BallByBall)()
            # ball = ball_by_ball_schema.load(json_str)

            matchId = ''
            delivery = json_dict['match']['delivery']['innings'] + '.' + json_dict['match']['delivery']['over'] + '.' + json_dict['match']['delivery']['ball']
            ball = json_dict['match']['delivery']['ball']
            batter = json_dict['match']['battingTeam']['batsman']['name']
            batterId = json_dict['match']['battingTeam']['batsman']['id']
            rightHandedBat = json_dict['match']['battingTeam']['batsman']['isRightHanded']
            nonStriker = json_dict['match']['battingTeam']['batsmanPartner']['name']
            nonStrikerId = json_dict['match']['battingTeam']['batsmanPartner']['id']
            bowler = json_dict['match']['bowlingTeam']['bowler']['name']
            bowlerId = json_dict['match']['bowlingTeam']['bowler']['id']
            rightArmedBowl = json_dict['match']['bowlingTeam']['bowler']['isRightHanded']
            bowlingStyle = json_dict['match']['delivery']['deliveryType']
            ballSpeed = json_dict['match']['delivery']['trajectory']['releaseSpeed']
            dismissalDetails = ''
            runs = json_dict['match']['delivery']['scoringInformation']['score']
            batterRuns = ''
            bowlerRuns = ''
            extras = json_dict['match']['delivery']['scoringInformation']['extrasScore']
            pitchX = ''
            pitchY = ''
            stumpsX = ''
            stumpsY = ''
            fieldX = ''
            fieldY = ''
            delivery_type = json_dict['match']['delivery']['deliveryType']
            shot_attacked = json_dict['match']['delivery']['shotInformation']['shotAttacked']
            shot_played = json_dict['match']['delivery']['shotInformation']['shotAttacked']
            shot_type_additional = json_dict['match']['delivery']['shotInformation']['shotAttacked']
            # mipl_data.loc[index] = [batsman_name, batsman_id, bowler_name, bowler_id, delivery_type,
            #                         shot_attacked, shot_played, shot_type_additional]

            json_file.close()

    return mipl_data


mipl_csv = load_csv_data_mipl()
mipl_json = load_json_data_mipl(mipl_csv.columns)

batsman_ball_type = mipl_json.pivot_table(columns=['batsman_name', "delivery_type"], aggfunc='size')
batsman_ball_type.to_csv('Pre-processing-csvs/batsman_ball_type')

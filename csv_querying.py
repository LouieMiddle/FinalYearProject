import os.path

import pandas as pd


def load_csv_data_mipl():
    csv_path = os.path.join("HawkeyeStats-main", "mensIPLHawkeyeStats.csv")
    return pd.read_csv(csv_path)


def filter_by_pitch_x_pitch_y(data):
    data = data[(data['pitchX'] >= -2) & (data['pitchX'] <= 2)]
    data = data[(data['pitchY'] >= 0) & (data['pitchY'] <= 14)]
    return data


seam = ['FAST_SEAM', 'MEDIUM_SEAM', 'SEAM']

mipl_csv = load_csv_data_mipl()
mipl_csv = filter_by_pitch_x_pitch_y(mipl_csv)

# jos_buttler = mipl_csv[mipl_csv['batter'] == 'Jos Buttler']
# jos_buttler_seam = jos_buttler[jos_buttler['bowlingStyle'].isin(seam)]
# jos_buttler_seam.to_csv('Pre-processing-csvs/jos_buttler_seam_csv')

# faf_du_plessis = mipl_csv[mipl_csv['batter'] == 'Faf du Plessis']
# faf_du_plessis_seam = faf_du_plessis[faf_du_plessis['bowlingStyle'].isin(seam)]
# faf_du_plessis_seam.to_csv('Pre-processing-csvs/faf_du_plessis_seam_csv.csv')

left_arm_balls = mipl_csv[mipl_csv['rightArmedBowl'] == False]
left_arm_balls.to_csv('Pre-processing-csvs/left_arm_bowls_csv.csv')

# right_arm_balls = mipl_csv[mipl_csv['rightArmedBowl'] == True]
# right_arm_balls.to_csv('Pre-processing-csvs/right_arm_bowls_csv.csv')

# ravindra_jadeja = mipl_csv[mipl_csv['bowler'] == 'Ravindra Jadeja']
# ravindra_jadeja.to_csv('Pre-processing-csvs/ravindra_jadeja_csv.csv')

# TODO
#  Past wicket visualisation (low priority)
#  Left arm bowlers not normalised
#  Heatmap not buckets
#  Runs per over
#  No balls in bucket
#  Speed at each pitch

from query_utils import filter_by_pitch_x_pitch_y, load_csv_data_mipl

seam = ['FAST_SEAM', 'MEDIUM_SEAM', 'SEAM']

mipl_csv = load_csv_data_mipl()
mipl_csv = filter_by_pitch_x_pitch_y(mipl_csv)

# jos_buttler = mipl_csv[mipl_csv['batter'] == 'Jos Buttler']
# jos_buttler_seam = jos_buttler[jos_buttler['bowlingStyle'].isin(seam)]
# jos_buttler_seam.to_csv('Pre-processing-csvs/jos_buttler_seam_csv.csv')

# jos_buttler = mipl_csv[mipl_csv['batter'] == 'Jos Buttler']
# jos_buttler.to_csv('Pre-processing-csvs/jos_buttler_csv.csv')

# faf_du_plessis = mipl_csv[mipl_csv['batter'] == 'Faf du Plessis']
# faf_du_plessis_seam = faf_du_plessis[faf_du_plessis['bowlingStyle'].isin(seam)]
# faf_du_plessis_seam.to_csv('Pre-processing-csvs/faf_du_plessis_seam_csv.csv')

# left_arm_balls = mipl_csv[mipl_csv['rightArmedBowl'] == False]
# left_arm_balls.to_csv('Pre-processing-csvs/left_arm_bowls_csv.csv')

# right_arm_balls = mipl_csv[mipl_csv['rightArmedBowl'] == True]
# right_arm_balls.to_csv('Pre-processing-csvs/right_arm_bowls_csv.csv')

# ravindra_jadeja = mipl_csv[mipl_csv['bowler'] == 'Ravindra Jadeja']
# ravindra_jadeja.to_csv('Pre-processing-csvs/ravindra_jadeja_csv.csv')

# lasith_malinga = mipl_csv[mipl_csv['bowler'] == 'Lasith Malinga']
# lasith_malinga.to_csv('Pre-processing-csvs/lasith_malinga_csv.csv')

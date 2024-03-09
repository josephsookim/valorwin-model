import pandas as pd
import pickle

# Load map outcome model
with open('map_outcome_model.pkl', 'rb') as f:
    map_rf = pickle.load(f)

input_data = {
    'team_score': [9],
    'enemy_score': [5],
    'team_loadout_eco': [False],
    'team_loadout_full-buy': [False],
    'team_loadout_semi-buy': [True],
    'team_loadout_semi-eco': [False],
    'enemy_loadout_eco': [False],
    'enemy_loadout_full-buy': [True],
    'enemy_loadout_semi-buy': [False],
    'enemy_loadout_semi-eco': [False],
    'map_name_Ascent': [False],
    'map_name_Bind': [False],
    'map_name_Breeze': [False],
    'map_name_Fracture': [False],
    'map_name_Haven': [False],
    'map_name_Icebox': [False],
    'map_name_Lotus': [False],
    'map_name_Pearl': [False],
    'map_name_Split': [False],
    'map_name_Sunset': [True]
}

# Convert input data to DataFrame and one-hot encode categorical variables
input_df = pd.DataFrame(input_data, index=[0])
input_df = pd.get_dummies(input_df)

# Predict probabilities for map outcome
map_probabilities = map_rf.predict_proba(input_df)

# Probability of Team 1 winning map
print("Probability of Team 1 Winning Map:", map_probabilities[:, 0][0])

# Probability of Team 2 winning map
print("Probability of Team 2 Winning Map:", map_probabilities[:, 1][0])

map_winner = 1 if map_probabilities[:,
                                    0][0] > map_probabilities[:, 1][0] else 2
print("Predicted winner of the map:", map_winner)

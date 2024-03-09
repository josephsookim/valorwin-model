import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

# Assuming your data is stored in a pandas DataFrame called 'data'
data = pd.read_csv('random_forest/data/econ.round_data.csv')

# Data Preprocessing
X = data[['team_loadout', 'enemy_loadout',
          'team_score', 'enemy_score', 'map_name']]
y_round_outcome = data['round_outcome']
y_map_outcome = data['map_outcome']

# Encoding categorical variables
X = pd.get_dummies(X)

# Filtering data to include only classes 1 and 2 for both round and map outcomes
filtered_indices = (y_round_outcome.isin(
    [1, 2])) & (y_map_outcome.isin([1, 2]))
X_filtered = X[filtered_indices]
y_round_outcome_filtered = y_round_outcome[filtered_indices]
y_map_outcome_filtered = y_map_outcome[filtered_indices]

# Splitting data into training and testing sets
X_train_round, X_test_round, y_round_train, y_round_test = train_test_split(
    X_filtered, y_round_outcome_filtered, test_size=0.2, random_state=42)
X_train_map, X_test_map, y_map_train, y_map_test = train_test_split(
    X_filtered, y_map_outcome_filtered, test_size=0.2, random_state=42)

# Training the Random Forest Model for round outcome
round_rf = RandomForestClassifier(n_estimators=100, random_state=42)
round_rf.fit(X_train_round, y_round_train)

# Training the Random Forest Model for map outcome
map_rf = RandomForestClassifier(n_estimators=100, random_state=42)
map_rf.fit(X_train_map, y_map_train)

# Predicting Probabilities for round and map outcomes
round_probabilities = round_rf.predict_proba(X_test_round)
map_probabilities = map_rf.predict_proba(X_test_map)

# Predicting round and map outcomes
round_predictions = round_rf.predict(X_test_round)
map_predictions = map_rf.predict(X_test_map)

# Evaluation for round outcome
print("Round Outcome Classification Report:")
print(classification_report(y_round_test, round_predictions))

# Evaluation for map outcome
print("Map Outcome Classification Report:")
print(classification_report(y_map_test, map_predictions))

# Save round outcome model
with open('round_outcome_model.pkl', 'wb') as f:
    pickle.dump(round_rf, f)

# Save map outcome model
with open('map_outcome_model.pkl', 'wb') as f:
    pickle.dump(map_rf, f)

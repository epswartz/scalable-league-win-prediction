from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from tqdm import tqdm
import pickle

games = pd.read_csv("./data/games.csv")

categoricals = ['firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron', 'firstDragon','t1_champ1id', 't1_champ1_sum1', 't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2', 't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id', 't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1', 't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3', 't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2', 't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id', 't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1', 't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2', 't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4', 't2_ban5']

for c in tqdm(categoricals, "Formatting Data"):
    dummies = pd.get_dummies(games[c], prefix=c)
    games = games.join(dummies)
    games.drop([c], axis=1, inplace=True)

X = games.drop(['winner', 'gameId', 'creationTime'], axis=1).to_numpy()
y = games['winner'].values - 1

clf = LogisticRegression(random_state=0).fit(X, y)

pickle.dump(clf, open("winner_prediction.p", 'wb'))

print("Wrote model to winner_prediction.p")
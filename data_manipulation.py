import pandas as pd

df = pd.read_csv('data.csv')

learner_id = df.iloc[0]["learner_id"]

new_df = df[df["learner_id"] == learner_id]

print(new_df)
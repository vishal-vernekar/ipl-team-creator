import pandas as pd
import db_logic as dblogic

# Iterate over files in directory
file = "test.csv"

data = pd.read_csv(file, names=['key', 'type', 'ball', 'strike_team', 'strike', 'nonstrike', 'bowler', 'runs', 'extras', 'out_type', 'out_who'])

#Insert Team Data
teams = data.loc[(data.key == 'info') & (data.type == 'team')]
gender = data.loc[(data.key == 'info') & (data.type == 'gender')].ball.iloc[0]

for row in teams.itertuples():
    dblogic.insert_team(row.ball, gender)

# dblogic.insert_people()
# dblogic.insert_players()
#
# teams = dblogic.get_teams()
# people = dblogic.get_people()
# players = dblogic.get_players()
# dblogic.insert_game()
# dblogic.insert_balls()

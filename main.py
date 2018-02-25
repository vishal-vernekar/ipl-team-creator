import pandas as pd
import db_logic as dblogic

# TODO: Iterate over files in directory
file = "test.csv"

df = pd.read_csv(file, names=['key', 'type', 'ball', 'strike_team', 'strike', 'nonstrike', 'bowler', 'runs', 'extras', 'out_type', 'out_who'])

teams = df.loc[(df.key == 'info') & (df.type == 'team')]
gender = df.loc[(df.key == 'info') & (df.type == 'gender')].ball.iloc[0]
people = df.loc[(df.key == 'info') & ((df.type == 'umpire') | (df.type == 'tv_umpire') | (df.type == 'match_referee'))]
players = pd.unique(df.loc[df.key == 'ball'].loc[:, 'strike':'bowler'].values.ravel())
venue = df.loc[(df.key == 'info') & (df.type == 'venue')].ball.iloc[0]
city = df.loc[(df.key == 'info') & (df.type == 'city')].ball.iloc[0]

for row in teams.itertuples():
    dblogic.insert_team(row.ball, gender)

for row in people.itertuples():
    dblogic.insert_people(row.ball)

for item in players:
    dblogic.insert_players(item)

dblogic.insert_ground(venue, city)

season = df.loc[(df.key == 'info') & (df.type == 'season')].ball.iloc[0]
date = df.loc[(df.key == 'info') & (df.type == 'date')].ball.iloc[0]
competition = df.loc[(df.key == 'info') & (df.type == 'competition')].ball.iloc[0]

grounds = dblogic.get_grounds()
teams = dblogic.get_teams()
players = dblogic.get_players()
people = dblogic.get_people()

#game_id = dblogic.insert_game(season, date, competition, grounds[])

# dblogic.insert_game()
# dblogic.insert_balls()

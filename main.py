import pandas as pd
import db_logic as dblogic
import logging as log
import os


def process_file(file):

    df = pd.read_csv(file, names=['key', 'type', 'ball', 'strike_team', 'strike', 'nonstrike', 'bowler', 'runs', 'extras', 'out_type', 'out_player'])

    info = df.loc[df.key == "info"]
    balls = df.loc[df.key == "ball"]

    teams = info.loc[info.type == 'team']
    people = info.loc[(info.type == 'umpire') | (info.type == 'tv_umpire') | (info.type == 'match_referee') | (info.type == 'reserve_umpire')]
    gender = info.loc[info.type == 'gender'].ball.iloc[0]

    venue = info.loc[info.type == 'venue'].ball.iloc[0]
    city = info.loc[info.type == 'city'].ball.iloc[0]

    players = pd.unique(df.loc[df.key == 'ball'].loc[:, 'strike':'bowler'].values.ravel())

    for row in teams.itertuples():
        dblogic.insert_team(row.ball, gender)

    for row in people.itertuples():
        dblogic.insert_people(row.ball)

    for item in players:
        dblogic.insert_players(item)

    dblogic.insert_ground(venue, city)

    season = info.loc[info.type == 'season'].ball.iloc[0]
    date = info.loc[info.type == 'date'].ball.iloc[0]
    competition = info.loc[info.type == 'competition'].ball.iloc[0]
    toss_winner = info.loc[info.type == 'toss_winner'].ball.iloc[0]
    toss_decision = info.loc[info.type == 'toss_decision'].ball.iloc[0]
    player_match = info.loc[info.type == 'player_of_match'].ball.iloc[0]
    umpire = info.loc[info.type == 'umpire']
    reserve_umpire = info.loc[info.type == 'reserve_umpire'].ball.iloc[0]
    tv_umpire = info.loc[info.type == 'tv_umpire'].ball.iloc[0]
    match_referee = info.loc[info.type == 'match_referee'].ball.iloc[0]
    winner = info.loc[info.type == 'winner'].ball.iloc[0]
    winner_runs = info.loc[info.type == 'winner_runs'].ball.iloc[0]

    ground_ids = dblogic.get_grounds()
    team_ids = dblogic.get_teams()
    player_ids = dblogic.get_players()
    people_ids = dblogic.get_people()

    game_id = dblogic.insert_game(
        season,
        date,
        competition,
        ground_ids.loc[ground_ids.venue == venue].id.iloc[0],
        team_ids.loc[team_ids.name == teams.ix[1].ball].id.iloc[0],
        team_ids.loc[team_ids.name == teams.ix[1].ball].id.iloc[0],
        team_ids.loc[team_ids.name == toss_winner].id.iloc[0],
        toss_decision,
        player_ids.loc[player_ids.name == player_match].id.iloc[0],
        people_ids.loc[people_ids.name == umpire.iloc[0].ball].id.iloc[0],
        people_ids.loc[people_ids.name == umpire.iloc[1].ball].id.iloc[0],
        people_ids.loc[people_ids.name == reserve_umpire].id.iloc[0],
        people_ids.loc[people_ids.name == tv_umpire].id.iloc[0],
        people_ids.loc[people_ids.name == match_referee].id.iloc[0],
        team_ids.loc[team_ids.name == winner].id.iloc[0],
        winner_runs
    )

    ball_no = 0

    for row in balls.itertuples():
        ball_no += 1
        ball_id = dblogic.insert_ball(
            ball_no,
            row.ball,
            game_id,
            team_ids.loc[team_ids.name == row.strike_team].id.iloc[0],
            player_ids.loc[player_ids.name == row.strike].id.iloc[0],
            player_ids.loc[player_ids.name == row.nonstrike].id.iloc[0],
            player_ids.loc[player_ids.name == row.bowler].id.iloc[0],
            int(row.runs),
            int(row.extras)
        )

        if not pd.isna(row.out_type):
            dblogic.insert_out(
                ball_id,
                player_ids.loc[player_ids.name == row.out_player].id.iloc[0],
                row.out_type
            )

    # enter position data
    balls2 = balls.drop_duplicates(['strike'], keep='first')

    for team in teams.itertuples():
        position_count = 0
        for row in balls2.loc[balls2.strike_team == team.ball].itertuples():
            position_count += 1
            dblogic.insert_lineup(
                player_ids.loc[player_ids.name == row.strike].id.iloc[0],
                game_id,
                position_count
            )


def main():
    log.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=log.INFO)

    for filename in os.listdir("."):
        if filename.endswith(".csv"):
            process_file(filename)


if __name__ == '__main__':
    main()


#print("Season:" + season)
#print("Date:" + date)
#print("Competition:" + competition)
#print(ground_ids.loc[ground_ids.venue == venue].id.iloc[0])
#print(umpire)
#print("Umpire1:" + umpire.iloc[0].ball)
#print(people_ids.loc[people_ids.name == umpire.iloc[1].ball].id.iloc[0])
#print(player_ids.loc[player_ids.name == player_match].id.iloc[0])
#print(people_ids)
#print(reserve_umpire)
#print(people_ids.loc[people_ids.name == reserve_umpire].id.iloc[0])
#print(ground_ids.loc[ground_ids.venue == venue].id.iloc[0])


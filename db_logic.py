import db_conn as db
import pandas as pd
import logging as log


def insert_team(name, gender):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO team(name,gender) VALUES('" + name + "','" + gender + "') ON DUPLICATE KEY UPDATE name = '" + name + "'"
    log.debug(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return


def insert_people(name):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO people(name) VALUES('" + name + "') ON DUPLICATE KEY UPDATE name = '" + name + "'"
    log.debug(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return


def insert_players(name):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO player(name) VALUES('" + name + "') ON DUPLICATE KEY UPDATE name = '" + name + "'"
    log.debug(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return


def insert_ground(venue, city):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO ground(venue, city) VALUES('" + venue + "','" + city + "') ON DUPLICATE KEY UPDATE venue = '" + venue + "'"
    log.debug(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return


def get_people():
    conn = db.get_conn()
    sql = "SELECT id, name from people"
    log.debug(sql)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def get_teams():
    conn = db.get_conn()
    sql = "SELECT id, name from team"
    log.debug(sql)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def get_players():
    conn = db.get_conn()
    sql = "SELECT id, name from player"
    log.debug(sql)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def get_grounds():
    conn = db.get_conn()
    sql = "SELECT id, venue from ground"
    log.debug(sql)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def insert_game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, umpire1,
                umpire2, reserve_umpire, tv_umpire, match_referee, winner, winner_runs):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, umpire1, umpire2, reserve_umpire, tv_umpire, match_referee, winner, winner_runs) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, umpire1, umpire2, reserve_umpire, tv_umpire, match_referee, winner, winner_runs)
    log.debug(sql)
    cursor.execute(sql)
    row_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return row_id


def insert_ball(over, ball, game, strike, nonstrike, bowler, runs, extras):
    sql = "INSERT INTO ball(over, ball, game, strike, nonstrike, bowler, runs, extras) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(over, ball, game, strike, nonstrike, bowler, runs, extras)
    print(sql)
    return 1


def insert_out():
    return


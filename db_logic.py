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


def insert_game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, winner):
    conn = db.get_conn()
    cursor = conn.cursor()
    if winner == '':
        sql = "INSERT INTO game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match)
    else:
        sql = "INSERT INTO game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, winner) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, winner)
    log.info(sql)
    cursor.execute(sql)
    row_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return row_id


def insert_ball(ball, over, game, team, strike, nonstrike, bowler, runs, extras):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO ball(ball, over, game, team, strike, nonstrike, bowler, runs, extras) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ball, over, game, team, strike, nonstrike, bowler, runs, extras)
    log.debug(sql)
    cursor.execute(sql)
    row_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return row_id


def insert_out(ball_id, player_out, method_out):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO wicket(ball_id, player_out, method_out) VALUES('{}','{}','{}')".format(ball_id, player_out, method_out)
    log.debug(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return


def insert_lineup(player_id, game_id, position):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO lineup(player_id, game_id, position) VALUES('{}','{}','{}')".format(player_id, game_id, position)
    log.debug(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return


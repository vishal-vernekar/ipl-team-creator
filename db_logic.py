import db
import pandas as pd
import logging as log


def insert_team(name, gender):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO team(name,gender) VALUES(%s,%s) ON DUPLICATE KEY UPDATE name = %s"
    cursor.execute(sql, (name, gender, name))
    log.debug(sql)
    conn.commit()
    return


# def insert_people(name):
#     conn = db.get_conn()
#     cursor = conn.cursor()
#     sql = "INSERT INTO people(name) VALUES(%s) ON DUPLICATE KEY UPDATE name = %s"
#     cursor.execute(sql, (name,name))
#     log.debug(sql)
#     conn.commit()
#     return


def insert_player(name, gender):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO player(name, gender) VALUES(%s,%s) ON DUPLICATE KEY UPDATE name = %s"
    cursor.execute(sql, (name, gender, name))
    log.debug(sql)
    conn.commit()
    return


def insert_ground(venue, city):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO ground(venue, city) VALUES(%s,%s) ON DUPLICATE KEY UPDATE venue = %s"
    cursor.execute(sql, (venue, city, venue))
    log.debug(sql)
    conn.commit()
    return


# def get_people():
#     conn = db.get_conn()
#     sql = "SELECT id, name from people"
#     log.debug(sql)
#     df = pd.read_sql_query(sql, conn)
#     return df


def get_teams():
    conn = db.get_conn()
    sql = "SELECT id, name from team"
    log.debug(sql)
    df = pd.read_sql_query(sql, conn)
    return df


def get_players():
    conn = db.get_conn()
    sql = "SELECT id, name from player"
    log.debug(sql)
    df = pd.read_sql_query(sql, conn)
    return df


def get_grounds():
    conn = db.get_conn()
    sql = "SELECT id, venue from ground"
    log.debug(sql)
    df = pd.read_sql_query(sql, conn)
    return df


def insert_game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, winner):
    # TODO: Add match_result column
    conn = db.get_conn()
    cursor = conn.cursor()
    if winner == '' and player_match == '':
        sql = "INSERT INTO game(season, date, competition, ground, team1, team2, toss_winner, toss_decision) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (season, date, competition, int(ground), int(team1), int(team2), int(toss_winner), toss_decision))
    elif winner == '':
        sql = "INSERT INTO game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (
        season, date, competition, int(ground), int(team1), int(team2), int(toss_winner), toss_decision,
        int(player_match)))
    else:
        sql = "INSERT INTO game(season, date, competition, ground, team1, team2, toss_winner, toss_decision, player_match, winner) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (season, date, competition, int(ground), int(team1), int(team2), int(toss_winner), toss_decision, int(player_match), int(winner)))
    log.debug(sql)
    row_id = cursor.lastrowid
    conn.commit()
    return row_id


def insert_ball(ball, over, game, team, strike, nonstrike, bowler, runs, extras):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO ball(ball, over, game, team, strike, nonstrike, bowler, runs, extras) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    log.debug(sql)
    cursor.execute(sql, (ball, float(over), int(game), int(team), int(strike), int(nonstrike), int(bowler), int(runs), int(extras)))
    row_id = cursor.lastrowid
    conn.commit()
    return row_id


def insert_out(ball_id, player_out, method_out):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO wicket(ball_id, player_out, method_out) VALUES(%s,%s,%s)"
    log.debug(sql)
    cursor.execute(sql, (ball_id, int(player_out), method_out))
    conn.commit()
    return


def insert_lineup(player_id, game_id, position):
    conn = db.get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO lineup(player_id, game_id, position) VALUES(%s,%s,%s)"
    log.debug(sql)
    cursor.execute(sql, (int(player_id), int(game_id), position))
    conn.commit()
    return


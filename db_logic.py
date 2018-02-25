def insert_team(name, gender):
    print("INSERT INTO team(name,gender) VALUES('" + name + "','" + gender + "') ON DUPLICATE KEY UPDATE name = '" + name + "'")
    return


def insert_people(name):
    print("INSERT INTO team(name) VALUES('" + name + "') ON DUPLICATE KEY UPDATE name = '" + name + "'")
    return


def insert_players(name):
    print("INSERT INTO player(name) VALUES('" + name + "') ON DUPLICATE KEY UPDATE name = '" + name + "'")
    return


def insert_ground(venue, city):
    print("INSERT INTO ground(venue, city) VALUES('" + venue + "','" + city + "') ON DUPLICATE KEY UPDATE name = '" + venue + "'")
    return

def insert_game():
    return


def insert_balls():
    return


def get_people():
    print("SELECT id, name from people")
    return


def get_teams():
    print("SELECT id, name from team")
    return


def get_players():
    print("SELECT id, name from player")
    return


def get_grounds():
    print("SELECT id, name from ground")
    return

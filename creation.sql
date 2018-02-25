CREATE TABLE team (
    id int,
    name varchar(255),
    gender varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE people (
    id int,
    name varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE player (
    id int,
    name varchar(255),
    gender varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE ground (
    id int,
    venue varchar(255),
    city varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE game (
    id int,
    season varchar(255),
    date varchar(255),
    competition varchar(255),
    ground_id int,
    team1 int,
    team2 int,
    toss_winner int,
    toss_decision varchar(255),
    player_match int,
    umpire1 int,
    umpire2 int,
    reserve_umpire int,
    tv_umpire int,
    match_referee int,
    winner int,
    winner_runs int,
    PRIMARY KEY (id),
    FOREIGN KEY (ground_id) REFERENCES ground(id),
    FOREIGN KEY (team1) REFERENCES team(id),
    FOREIGN KEY (team2) REFERENCES team(id),
    FOREIGN KEY (toss_winner) REFERENCES team(id),
    FOREIGN KEY (player_match) REFERENCES player(id),
    FOREIGN KEY (umpire1) REFERENCES people(id),
    FOREIGN KEY (umpire2) REFERENCES people(id),
    FOREIGN KEY (reserve_umpire) REFERENCES people(id),
    FOREIGN KEY (tv_umpire) REFERENCES people(id),
    FOREIGN KEY (match_referee) REFERENCES people(id),
    FOREIGN KEY (winner) REFERENCES team(id)
);

CREATE TABLE ball (
    id int,
    over int,
    ball int,
    game int,
    strike int,
    nonstrike int,
    runs int,
    extras int,
    PRIMARY KEY (id),
    FOREIGN KEY (game) REFERENCES game(id),
    FOREIGN KEY (strike) REFERENCES player(id),
    FOREIGN KEY (nonstrike) REFERENCES player(id),
    FOREIGN KEY (bowler) REFERENCES player(id)
);

CREATE TABLE wicket (
    id int,
    ball_id int,
    player_out int,
    method_out varchar(255),
    PRIMARY KEY (id),
    FOREIGN KEY (ball_id) REFERENCES ball(id),
    FOREIGN KEY (player_out) REFERENCES player(id)
);

CREATE TABLE position (
    id int,
    player_id int,
    game_id int,
    position int,
    PRIMARY KEY (id),
    FOREIGN KEY (player_id) REFERENCES player(id),
    FOREIGN KEY (game_id) REFERENCES game(id)
);
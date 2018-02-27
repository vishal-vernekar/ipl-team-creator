-- Drop if exists player_stats table
DROP TABLE IF EXISTS `player_stats`;


-- Create player_stats table
CREATE TABLE player_stats (
	player_id int NOT NULL UNIQUE,
	scored int,
	times_out int,
	balls_strike int,
	opener int,
	middle int,
	late int,
	total_games_strike int,
	runs_given int,
	wickets_taken int,
	balls_bowled int
);


-- Add all player ids
INSERT INTO player_stats(player_id) SELECT DISTINCT player.id FROM player;


-- Batsmen total runs
UPDATE
	player_stats
SET
    scored = (
		SELECT
            SUM(runs)
        FROM
            ball
        WHERE
            strike = player_stats.player_id
	);


-- Batsmen Total balls faced
UPDATE
	player_stats
SET
    balls_strike = (
		SELECT
            COUNT(*)
        FROM
            ball
        WHERE
            strike = player_stats.player_id
	);


-- Total number of times out batsmen
UPDATE
	player_stats
SET
    times_out = (
		SELECT
            COUNT(*)
        FROM
            wicket
        WHERE
            player_out = player_stats.player_id
	);


-- Batsmen Position Opening
UPDATE
	player_stats
SET
    opener = (
		SELECT
            COUNT(*)
        FROM
            lineup
        WHERE
            lineup.player_id = player_stats.player_id AND
            position IN (1, 2, 3)
	);


-- Batsmen Position Middle Order
UPDATE
	player_stats
SET
    middle = (
		SELECT
            COUNT(*)
        FROM
            lineup
        WHERE
            lineup.player_id = player_stats.player_id AND
            position IN (4, 5, 6)
	);


-- Batsmen Position Late Order
UPDATE
	player_stats
SET
    late = (
		SELECT
            COUNT(*)
        FROM
            lineup
        WHERE
            lineup.player_id = player_stats.player_id AND
            position > 6
	);


-- Total number of games on strike position
UPDATE
	player_stats
SET
    total_games_strike = (
		SELECT
            COUNT(DISTINCT ball.game)
        FROM
            ball
        WHERE
            ball.strike = player_stats.player_id
	);


-- Bowler Balls bowled
UPDATE
	player_stats
SET
    total_balls_bowled = (
		SELECT
            COUNT(*)
        FROM
            ball
        WHERE
            ball.bowler = player_stats.player_id
	);


-- Bowler runs_given
UPDATE
	player_stats
SET
    runs_given = (
		SELECT
            SUM(runs)
        FROM
            ball
        WHERE
            ball.bowler = player_stats.player_id
	);


-- Bowler extras_given
UPDATE
	player_stats
SET
    extras_given = (
		SELECT
            SUM(extras)
        FROM
            ball
        WHERE
            ball.bowler = player_stats.player_id
	);


-- Bowler Total wickets taken
UPDATE
	player_stats
SET
    wickets_taken = (
		SELECT
            COUNT(*)
        FROM
            ball, wicket
        WHERE
            ball.id = wicket.ball_id AND
            ball.bowler = player_stats.player_id
	);
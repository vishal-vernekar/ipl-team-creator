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


-- Score & balls faced
INSERT INTO player_stats(player_id, scored, balls_strike) SELECT player.id, SUM(runs), COUNT(ball.id) FROM ball, player WHERE strike = player.id GROUP BY player.id;


-- Total number of times out batsmen
INSERT INTO player_stats(player_id, times_out) SELECT player.id, COUNT(wicket.id) FROM wicket, player where player_out = player.id GROUP BY player.id;


-- Batsmen Position Opening
INSERT INTO player_stats(player_id, opener) SELECT player.id, COUNT(lineup.id) FROM lineup, player where lineup.player_id = player.id AND position IN (1, 2, 3)
GROUP BY player.id;


-- Batsmen Position Middle Order
INSERT INTO player_stats(player_id, middle) SELECT player.id, COUNT(lineup.id) FROM lineup, player where lineup.player_id = player.id AND position IN (4, 5, 6) GROUP BY player.id;


-- Batsmen Position Late Order
INSERT INTO player_stats(player_id, late) SELECT player.id, COUNT(lineup.id) FROM lineup, player where lineup.player_id = player.id AND position IN (7, 8, 9, 10, 11) GROUP BY player.id;


-- Total number of games on strike position
INSERT INTO player_stats(player_id, total_games_strike) SELECT player.id, COUNT(DISTINCT ball.game) FROM ball, player where ball.strike = player.id GROUP BY player.id;


-- Bowler Balls bowled & runs given
INSERT INTO player_stats(player_id, total_balls_bowled, runs_given, extras_given) SELECT player.id, COUNT(ball.id), SUM(runs), SUM(extras) FROM ball, player where bowler = player.id GROUP BY player.id;


-- Bowler Total wickets taken
INSERT INTO player_stats(player_id, wickets_taken) SELECT player.id, COUNT(ball.id) FROM wicket, ball, player WHERE ball.id = wicket.ball_id AND player.id = bowler GROUP BY player.id;
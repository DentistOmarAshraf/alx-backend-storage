-- Avarage calculation procedure

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int)
BEGIN
    DECLARE the_average float;
    SELECT AVG(c.score) into the_average
    FROM users u JOIN corrections c 
    ON u.id=c.user_id
    WHERE u.id = user_id;
    
    UPDATE users
    set average_score=the_average
    WHERE id = user_id;
end $$
DELIMITER ;

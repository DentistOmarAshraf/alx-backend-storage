-- Compute average weighted score for all

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done int DEFAULT 0;
    DECLARE the_id int;
    DECLARE avg_weighted float;

    DECLARE user_id CURSOR FOR SELECT id from users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_id;
    loop_over_users: LOOP
        FETCH user_id into the_id;
        IF done THEN
            LEAVE loop_over_users;
        END IF;

        SELECT (SUM(c.score * p.weight) / SUM(p.weight))
        INTO avg_weighted
        FROM corrections c JOIN projects p
        ON c.project_id = p.id
        JOIN users u
        ON u.id = c.user_id
        WHERE u.id = the_id;

        UPDATE users
        SET average_score = avg_weighted
        WHERE id = the_id;
    END LOOP;
    CLOSE user_id;
END$$

DELIMITER ;

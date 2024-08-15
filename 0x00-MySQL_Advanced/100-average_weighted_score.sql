-- Compute average WEIGHT score

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id int)
BEGIN
    DECLARE avg_weighted float;

    SELECT (SUM(c.score * p.weight) / SUM(p.weight))
    INTO avg_weighted
    FROM corrections c JOIN projects p
    ON c.project_id = p.id
    JOIN users u
    ON u.id = c.user_id
    WHERE u.id = user_id;

    UPDATE users
    SET average_score = avg_weighted
    WHERE id = user_id;
END$$
DELIMITER ;
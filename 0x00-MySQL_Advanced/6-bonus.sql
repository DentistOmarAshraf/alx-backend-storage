-- Create procedure to insert new correction to student

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id int,
    IN project_name varchar(255),
    IN score int
)
BEGIN
    DECLARE projectID INT;

    SELECT id INTO projectID FROM projects WHERE name=project_name;
    IF projectID IS NULL THEN
        INSERT INTO projects(name) VALUES(project_name);
        SET projectID = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections(user_id, project_id, score)
    VALUES(user_id, projectID, score);
END $$

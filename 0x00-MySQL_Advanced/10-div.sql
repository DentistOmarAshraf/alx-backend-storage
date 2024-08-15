-- Function return result of divide of two number
-- it reutrn 0 if number / 0

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS float
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN (a / b);
END $$

DELIMITER ;
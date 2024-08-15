-- Create view

DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
select name from students
where(
    score < 80
    and
    (last_meeting IS NULL or last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH)));
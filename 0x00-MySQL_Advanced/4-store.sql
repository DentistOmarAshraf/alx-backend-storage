-- Trigger on table to decrease from other table

CREATE TRIGGER buybuy 
AFTER INSERT ON orders 
FOR EACH ROW 
UPDATE items 
SET quantity = quantity - NEW.number
where name = NEW.item_name;
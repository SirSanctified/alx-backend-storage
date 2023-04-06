-- create a trigger that decreases the quantity of an item after adding a new order.

CREATE OR REPLACE TRIGGER update_items_on_new_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	DECLARE ordered_item VARCHAR(255);
	SET ordered_item = NEW.item_name;
	UPDATE items
	SET quantity = quantity - 1
	WHERE name = ordered_item;
END;


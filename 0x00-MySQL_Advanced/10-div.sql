-- creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

DELIMITER //
CREATE FUNCTION SafeDiv(@ INT, @b INT)
RETURNS FLOAT AS
BEGIN
    IF @b = 0
    THEN
        RETURN 0;
    ELSE
        RETURN CAST(@a AS FLOAT) / CAST(@b AS FLOAT);
    END IF;
END//
DELIMITER ;

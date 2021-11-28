select * from ramen;
create table ramencopy as select * from ramen; 
select * from ramencopy;
drop table ramencopy


DO $$
DECLARE
    ramen_id     ramencopy.ramen_id%TYPE;
    ramen_name   ramencopy.ramen_name%TYPE;
	ramen_style  ramencopy.ramen_style%TYPE;
	

BEGIN
    ramen_id := '2599';
    ramen_name := 'Nice Ramen';
	ramen_style := 'Cup';
	
    FOR counter IN 1..10
        LOOP
            INSERT INTO ramencopy(ramen_id, ramen_name, ramen_style)
            VALUES (ramen_id || counter, ramen_name || ' ' || counter, ramen_style + counter);
        END LOOP;
END;
$$
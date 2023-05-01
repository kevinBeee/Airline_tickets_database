select * 
from Flight 
where departure_date > CURRENT_DATE() OR (departure_date = CURRENT_DATE() AND departure_time >= CURRENT_TIME());

select * 
from Flight 
where flight_status='delayed';

select first_name, last_name 
from Customer 
where email in (select email from Purchase);

SELECT * FROM Airplane where airline_name='Jet Blue';
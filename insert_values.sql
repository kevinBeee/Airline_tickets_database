insert into airline values('Jet Blue');
insert into airline values('Delta');

insert into Airport values('JFK', 'John F.Kennedy International Airport', 'New York', 'USA', 'both');
insert into Airport values('PVG', 'Pudong International Airport', 'Shanghai', 'China', 'both');
insert into Airport values('SIN', 'Changi Airport', 'Singapore', 'Singapore', 'international');
insert into Airport values('HPN', 'Westchester County Airport', 'White Plains', 'USA', 'domestic');

insert into Customer values('yz6878@nyu.edu', 'Kz12345', 'Kevin', 'Zhou', '22 Chapel', '22 Chapel Street', '123', 'Brooklyn', 'NY', 11201, 'AB1234567', 'China', '2002-05-09', 'online');
insert into Customer_phone values('yz6878@nyu.edu', 0123456789);
insert into Customer_phone values('yz6878@nyu.edu', 1234123412);
insert into Customer values ('jz4441@nyu.edu', '12345678', 'Junwen', 'Zhong', 'Hoyt&Horn', 'Hoyt St.', '5K', 'Brooklyn', 'NY', 11201, 'ED123456', 'China', '2001-08-08', 'offline');
insert into Customer_phone values('jz4441@nyu.edu', 8888888888);
insert into Customer values('yd2089@nyu.edu', 'Yd12345', 'Yiling', 'Ding', '351 Marin', '351 Marin Blvd', '1234', 'Jersey City', 'NJ', 07302, 'AB7654321', 'China', '2002-05-17', 'online');
insert into Customer_phone values('yd2089@nyu.edu', 1234567890);

insert into Airplane values('N986JB', 200, 'Airbus', '2017-10-01', null, 'Jet Blue');
insert into Airplane values('N187JB', 100, 'Embraer', '2005-11-01', null, 'Jet Blue');
insert into Airplane values('N703TW', 100, 'Boeing', '1996-11-01', null, 'Delta');

insert into Airline_staff values('staff1', 'pwdstaff1', 'James', 'Bond', '1999-12-31', 'Jet Blue');
insert into Staff_phone values('staff1', 1212121212);
insert into Staff_email values('staff1', 'staff1@gmail.com');
insert into Airline_staff values('staff2', 'pwdstaff2', 'Tony', 'Stark', '2000-01-01', 'Jet Blue');
insert into Staff_phone values('staff2', 0101010101);
insert into Staff_email values('staff2', 'staff2@gmail.com');

insert into Flight values(903, 150, '2023-04-03', '21:16', '2023-04-03', '23:25', 'delayed', 99, 'N703TW', 'Delta', 'JFK', 'PVG');
insert into Flight values(1374, 200, '2023-04-03', '13:40', '2023-04-03', '17:27', 'on time', 150, 'N986JB', 'Jet Blue', 'JFK', 'SIN');
insert into Flight values(1374, 200, '2023-05-03', '13:40', '2023-05-03', '17:30', 'on time', 190, 'N986JB', 'Jet Blue', 'JFK', 'SIN');
insert into Flight values(1374, 200, '2023-06-03', '13:40', '2023-06-03', '17:30', 'on time', 100, 'N986JB', 'Jet Blue', 'JFK', 'SIN');
INSERT INTO Flight values(1374, 200, '2023-04-03', '18:40', '2023-04-03', '23:27', 'on time', 150, 'N986JB', 'Jet Blue', 'SIN', 'JFK'); 
#past ticket
insert into Ticket values(1001, 'Kevin', 'Zhou', '2002-05-09', 200, 'debit', 12345, 'Kevin Zhou', '2026-10-01', '2023-04-01', '10:00', 1374, '2023-04-03', '13:40', 'Jet Blue');
insert into Ticket values(1002, 'Hello', 'World', '2002-05-10', 200, 'debit', 12345, 'Kevin Zhou', '2026-10-01', '2023-04-01', '10:00', 1374, '2023-04-03', '13:40', 'Jet Blue');
#future tickets
insert into Ticket values(2001, 'Junwen', 'Zhong', '2001-08-08', 200, 'credit', 23456, 'Junwen Zhong', '2027-11-01', '2023-04-02', '11:00', 1374, '2023-05-03', '13:40', 'Jet Blue');
insert into Ticket values(3001, 'Yiling', 'Ding', '2002-05-17', 200, 'credit', 34567, 'Yiling Ding', '2025-10-01', '2023-04-03', '12:00', 1374, '2023-06-03', '13:40', 'Jet Blue');

insert into Purchase values ('yz6878@nyu.edu', 1001, 9, 'good');
insert into Purchase values ('yz6878@nyu.edu', 1002, null, null);
insert into Purchase values ('jz4441@nyu.edu', 2001, null, null);
insert into Purchase values ('yd2089@nyu.edu', 3001, null, null);

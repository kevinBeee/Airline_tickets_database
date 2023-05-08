insert into airline values('Delta');

insert into Airport values('JFK', 'JFK', 'NYC', 'USA', 'Both');
insert into Airport values('BOS', 'BOS', 'Boston', 'USA', 'Both');
insert into Airport values('PVG', 'PVG', 'Shanghai', 'China', 'Both');
insert into Airport values('BEI', 'BEI', 'Beijing', 'China', 'Both');
insert into Airport values('SFO', 'SFO', 'San Francisco', 'USA', 'Both');
insert into Airport values('LAX', 'LAX', 'Los Angeles', 'USA', 'Both');
insert into Airport values('HKA', 'HKA', 'Hong Kong', 'China', 'Both');
insert into Airport values('SHEN', 'SHEN', 'Shenzhen', 'China', 'Both');

insert into Customer values('testcustomer@nyu.edu', '1234', 'Jon', 'Snow', '1555', 'Jay St', '101', 'Brooklyn', 'New York', 11201, '54321', 'USA', '1999-12-19', 'offline');
insert into Customer_phone values('testcustomer@nyu.edu', 12343214321);
insert into Customer values ('user1@nyu.edu', '1234', 'Alice', 'Bob', '5405', 'Jay Street', '202', 'Brooklyn', 'New York', 11201, '54322', 'USA', '1999-11-19', 'offline');
insert into Customer_phone values('user1@nyu.edu', 12343224322);
insert into Customer values('user2@nyu.edu', '1234', 'Cathy', 'Wood', '1702', 'Jay Street', '123', 'Brooklyn', 'New York', 11201, '54323', 'USA', '1999-10-19', 'offline');
insert into Customer_phone values('user2@nyu.edu', 12343234323);
insert into Customer values('user3@nyu.edu', '1234', 'Trudy', 'Jones', '1890', 'Jay Street', '333', 'Brooklyn', 'New York', 11201, '54324', 'USA', '1999-09-19', 'offline');
insert into Customer_phone values('user2@nyu.edu', 12343244324);

insert into Airplane values('1', 4, 'Boeing', '2013-05-02', null, 'Delta');
insert into Airplane values('2', 4, 'Airbus', '2011-05-02', null, 'Delta');
insert into Airplane values('3', 50, 'Boeing', '2015-05-02', null, 'Delta');

insert into Airline_staff values('admin', 'abcd', 'Roe', 'Jones', '1978-05-25', 'Delta');
insert into Staff_phone values('admin', 11122223333);
insert into Staff_phone values('admin', 44455556666);
insert into Staff_email values('staff1', 'staff@nyu.edu');

insert into Flight values(903, 150, '2023-04-03', '21:16', '2023-04-03', '23:25', 'delayed', 99, 'N703TW', 'Delta', 'JFK', 'PVG');
insert into Flight values(1374, 200, '2023-04-03', '13:40', '2023-04-03', '17:27', 'on time', 150, 'N986JB', 'Jet Blue', 'JFK', 'SIN');
insert into Flight values(1374, 200, '2023-05-03', '13:40', '2023-05-03', '17:30', 'on time', 190, 'N986JB', 'Jet Blue', 'JFK', 'SIN');
insert into Flight values(1374, 200, '2023-06-03', '13:40', '2023-06-03', '17:30', 'on time', 100, 'N986JB', 'Jet Blue', 'JFK', 'SIN');
<<<<<<< Updated upstream
INSERT INTO Flight values(1374, 200, '2023-04-03', '18:40', '2023-04-03', '23:27', 'on time', 150, 'N986JB', 'Jet Blue', 'SIN', 'JFK'); 
=======
INSERT INTO Flight values(1374, 200, '2023-04-03', '18:40', '2023-04-03', '23:27', 'on time',150,'N986JB', 'Jet Blue', 'SIN','JFK'); 
>>>>>>> Stashed changes
#past ticket
insert into Ticket values(1001, 'Kevin', 'Zhou', '2002-05-09', 200, 'debit', 12345, 'Kevin Zhou', '2026-10-01', '2023-04-01', '10:00', 1374, '2023-04-03', '13:40', 'Jet Blue');
insert into Ticket values(1002, 'Hello', 'World', '2002-05-10', 200, 'debit', 12345, 'Kevin Zhou', '2026-10-01', '2023-04-01', '10:00', 1374, '2023-04-03', '13:40', 'Jet Blue');
#future tickets
insert into Ticket values(1003, 'Junwen', 'Zhong', '2001-08-08', 200, 'credit', 23456, 'Junwen Zhong', '2027-11-01', '2023-04-02', '11:00', 1374, '2023-05-03', '13:40', 'Jet Blue');
insert into Ticket values(1004, 'Yiling', 'Ding', '2002-05-17', 200, 'credit', 34567, 'Yiling Ding', '2025-10-01', '2023-04-03', '12:00', 1374, '2023-06-03', '13:40', 'Jet Blue');

insert into Purchase values ('yz6878@nyu.edu', 1001, 9, 'good');
insert into Purchase values ('yz6878@nyu.edu', 1002, null, null);
insert into Purchase values ('jz4441@nyu.edu', 2001, null, null);
insert into Purchase values ('yd2089@nyu.edu', 3001, null, null);

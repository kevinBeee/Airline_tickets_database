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
insert into Staff_email values('admin', 'staff@nyu.edu');

insert into Flight values(102, 300, '2023-02-09', '13:25:25', '2023-02-09', '16:50:25', 'on-time', 0, '3', 'Delta', 'SFO', 'LAX');
insert into Flight values(104, 300, '2023-03-04', '13:25:25', '2023-03-04', '16:50:25', 'on-time', 0, '3', 'Delta', 'PVG', 'BEI');
insert into Flight values(106, 350, '2023-01-04', '13:25:25', '2023-01-04', '16:50:25', 'delayed', 0, '3', 'Delta', 'SFO', 'LAX');
insert into Flight values(206, 400, '2023-07-04', '13:25:25', '2023-07-04', '16:50:25', 'on-time', 0, '2', 'Delta', 'SFO', 'LAX');
insert into Flight values(207, 300, '2023-08-05', '13:25:25', '2023-08-05', '16:50:25', 'on-time', 0, '2', 'Delta', 'LAX', 'SFO');
insert into Flight values(134, 350, '2022-12-11', '13:25:25', '2023-12-11', '16:50:25', 'delayed', 0, '3', 'Delta', 'JFK', 'BOS');
insert into Flight values(296, 3000, '2023-05-30', '13:25:25', '2023-05-30', '16:50:25', 'on-time', 0, '1', 'Delta', 'PVG', 'SFO');
insert into Flight values(715, 500, '2023-02-28', '10:25:25', '2023-02-28', '13:50:25', 'delayed', 0, '1', 'Delta', 'PVG', 'BEI');
insert into Flight values(839, 350, '2023-06-26', '13:25:25', '2023-06-26', '16:50:25', 'on-time', 0, '3', 'Delta', 'SHEN', 'BEI');



INSERT INTO Ticket VALUES (1, "Jon", "Snow", "1999-12-19", 300, "credit", 1111222233334444, "Test Customer 1", "2027-03-01", "2023-02-09", "11:55:55", 102, "2023-02-09", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("testcustomer@nyu.edu", 1, 4, "very comfortable");


INSERT INTO Ticket VALUES (2, "Alice", "Bob", "1999-11-19", 300, "credit", 1111222233335555, "User 1", "2027-03-01", "2023-02-09", "11:55:55", 102, "2023-02-09", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user1@nyu.edu", 2, 5, "relaxing, check-in and onboarding very professional");


INSERT INTO Ticket VALUES (3, "Cathy", "Wood", "1999-10-19", 300, "credit", 1111222233335555, "User 2", "2027-03-01", "2023-02-04", "11:55:55", 102, "2023-02-09", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user2@nyu.edu", 3, 3, "satisfied and will use the same flight again");


INSERT INTO Ticket VALUES (4, "Alice", "Bob", "1999-11-19", 300, "credit", 1111222233335555, "User 1", "2027-03-01", "2023-01-21", "11:55:55", 104, "2023-03-04", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user1@nyu.edu", 4, 5, "comfortable journey and professional");


INSERT INTO Ticket VALUES (5, "Jon", "Snow", "1999-12-19", 300, "credit", 1111222233334444, "Test Customer 1", "2027-03-01", "2023-02-28", "11:55:55", 104, "2023-03-04", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("testcustomer@nyu.edu", 5, 1, "customer care services are not good");

INSERT INTO Ticket VALUES (6, "Jon", "Snow", "1999-12-19", 350, "credit", 1111222233334444, "Test Customer 1", "2027-03-01", "2023-01-04", "11:55:55", 106, "2023-01-04", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("testcustomer@nyu.edu", 6, null, null);

INSERT INTO Ticket VALUES (7, "Trudy", "Jones", "1999-09-19", 350, "credit", 1111222233335555, "User 3", "2027-03-01", "2022-12-03", "11:55:55", 106, "2023-01-04", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user3@nyu.edu", 7, null, null);

INSERT INTO Ticket VALUES (8, "Trudy", "Jones", "1999-09-19", 300, "credit", 1111222233335555, "User 3", "2023-03-01", "2022-06-26", "11:55:55", 839, "2023-06-03", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user3@nyu.edu", 8, null, null);

INSERT INTO Ticket VALUES (9, "Trudy", "Jones", "1999-09-19", 300, "credit", 1111222233335555, "User 3", "2027-03-01", "2022-12-04", "11:55:55", 102, "2023-02-09", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user3@nyu.edu", 9, null, null);

INSERT INTO Ticket VALUES (11, "Trudy", "Jones", "1999-09-19", 300, "credit", 1111222233335555, "User 3", "2027-03-01", "2022-10-23", "11:55:55", 134, "2022-12-11", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user3@nyu.edu", 11, null, null);

INSERT INTO Ticket VALUES (12, "Jon", "Snow", "1999-12-19", 500, "credit", 1111222233334444, "Test customer 1", "2023-03-01", "2022-10-02", "11:55:55", 715, "2023-02-28", "10:25:25", "Delta");
INSERT INTO Purchase VALUES ("testcustomer@nyu.edu", 12, null, null);

INSERT INTO Ticket VALUES (14, "Trudy", "Jones", "1999-09-19", 400, "credit", 1111222233335555, "User 3", "2023-03-01", "2023-04-20", "11:55:55", 206, "2023-07-04", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user3@nyu.edu", 14, null, null);

INSERT INTO Ticket VALUES (15, "Alice", "Bob", "1999-11-19", 400, "credit", 1111222233335555, "User 1", "2023-03-01", "2023-04-21", "11:55:55", 206, "2023-07-04", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user1@nyu.edu", 15, null, null);

INSERT INTO Ticket VALUES (16, "Cathy", "Wood", "1999-10-19", 400, "credit", 1111222233335555, "User 2", "2023-03-01", "2023-02-19", "11:55:55", 206, "2023-07-04", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user2@nyu.edu", 16, null, null);

INSERT INTO Ticket VALUES (17, "Alice", "Bob", "1999-11-19", 300, "credit", 1111222233335555, "User 1", "2023-03-01", "2023-01-11", "11:55:55", 207, "2023-08-05", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user1@nyu.edu", 17, null, null);

INSERT INTO Ticket VALUES (18, "Jon", "Snow", "1999-12-19", 300, "credit", 1111222233334444, "Test Customer 1", "2023-03-01", "2023-02-25", "11:55:55", 207, "2023-08-05", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("testcustomer@nyu.edu", 18, null, null);

INSERT INTO Ticket VALUES (19, "Alice", "Bob", "1999-11-19", 3000, "credit", 1111222233334444, "Test Customer 1", "2023-03-01", "2023-04-22", "11:55:55", 296, "2023-05-30", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("user1@nyu.edu", 19, null, null);

INSERT INTO Ticket VALUES (20, "Jon", "Snow", "1999-12-19", 3000, "credit", 1111222233334444, "Test Customer 1", "2023-03-01", "2022-12-12", "11:55:55", 296, "2023-05-30", "13:25:25", "Delta");
INSERT INTO Purchase VALUES ("testcustomer@nyu.edu", 20, null, null);

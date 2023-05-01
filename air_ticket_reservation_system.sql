create table Airport(
    airport_code char(3),
    name varchar(40),
    city varchar(20),
    country varchar(20),
    type varchar(20),
    primary key (airport_code));

create table Airline(
    airline_name varchar(50),
    primary key (airline_name));

create table Airplane(
    id varchar(20),
    seats numeric(3,0),
    manufacturer varchar(20),
    manufacturing_date date,
    age int AS (YEAR(CURRENT_DATE) - YEAR(manufacturing_date)),
    airline_name varchar(50),
    primary key (id),
    foreign key (airline_name) references Airline(airline_name));
    
create table Customer(
    email varchar(50),
    customer_password varchar(50),
    first_name varchar(20),
    last_name varchar(20),
    building_name varchar(50),
    street_name varchar(50),
    apt_number varchar(20),
    city varchar(20),
    state varchar(20),
    zipcode numeric(10,0),
    passport_number varchar(20),
    passport_country varchar(20),
    date_of_birth date,
    log_in_status varchar(7),
    primary key (email));
    
create table Customer_phone(
    email varchar(50),
    phone_number numeric(20,0),
    primary key (email, phone_number),
    foreign key (email) references Customer(email));

create table Airline_staff(
    username varchar(50),
    staff_password varchar(50),
    first_name varchar(20),
    last_name varchar(20),
    date_of_birth date,
    airline_name varchar(50),
    primary key (username),
    foreign key (airline_name) references Airline(airline_name));
   
create table Staff_phone(
    username varchar(50),
    phone_number numeric(20, 0),
    primary key (username, phone_number),
    foreign key (username) references Airline_staff(username));
    
create table Staff_email(
    username varchar(50),
    email varchar(50),
    primary key (username, email),
    foreign key (username) references Airline_staff(username));

create table Flight(
    flight_number numeric(5,0),
    base_price numeric(8,2),
    departure_date date,
    departure_time time,
    arrival_date date,
    arrival_time time,
    flight_status varchar(20),
    tickets_booked numeric(3,0),
    id varchar(20),
    airline_name varchar(50),
    departure_airport char(3),
    arrival_airport char(3),
    primary key (airline_name, flight_number, departure_date, departure_time),
    foreign key (id) references Airplane(id),
    foreign key (airline_name) references Airline(airline_name),
    foreign key (departure_airport) references Airport(airport_code),
    foreign key (arrival_airport) references Airport(airport_code));

create table Ticket(
    id numeric(20,0),
    first_name varchar(20),
    last_name varchar(20),
    date_of_birth date,
    price numeric(10,2),
    card_type varchar(10),
    card_num numeric(20,0),
    name_on_card varchar(40),
    expire_date date,
    purchase_date date,
    purchase_time time,
    flight_number numeric(5,0),
    departure_date date,
    departure_time time,
    airline_name varchar(50),
    primary key (id),
    foreign key (airline_name, flight_number, departure_date, departure_time) references Flight(airline_name, flight_number, departure_date, departure_time));

create table Purchase(
    email varchar(50),
    id numeric(20,0),
    rate numeric(2,0),
    comments varchar(1000),
    primary key (email, id),
    foreign key (email) references Customer(email),
    foreign key (id) references Ticket(id));

create view public_info as 
    select airline_name, flight_number, departure_date, arrival_date, flight_status
    from Flight;
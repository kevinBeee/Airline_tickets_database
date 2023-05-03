#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
	cursor = conn.cursor()
	query = 'SELECT * FROM public_info'
	cursor.execute(query)
	info = cursor.fetchall()
	cursor.close()
	return render_template('index.html', flights=info)


#flight search
@app.route('/flight_search')
def flight_search():
	if (session):
		return render_template('flight_search.html', loggedin=True)
	else:
		return render_template('flight_search.html', loggedin=False)
@app.route('/search', methods=['GET', 'POST'])
def search():
	search_type = request.form['search_type']
	if (search_type == 'city'):
		source_city = request.form['source']
		destination_city = request.form['destination']
	else:
		source_airport = request.form['source']
		destination_airport = request.form['destination']
	depart_date = request.form['departure_date']
	return_date = request.form.get('return_date', None)

	cursor = conn.cursor()
	if (search_type == 'city'):
		if (return_date):
			query = 'SELECT airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, flight_status FROM Flight where departure_airport in (select airport_code from Airport where city=%s) and arrival_airport in (select airport_code from Airport where city=%s) and departure_date=%s'
			cursor.execute(query, (source_city, destination_city, depart_date))
			depart_flights = cursor.fetchall()
			cursor.execute(query, (destination_city, source_city, return_date))
			return_flights = cursor.fetchall()
		else:
			query = 'SELECT airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, flight_status FROM Flight where departure_airport in (select airport_code from Airport where city=%s) and arrival_airport in (select airport_code from Airport where city=%s) and departure_date=%s'
			cursor.execute(query, (source_city, destination_city, depart_date))
			depart_flights = cursor.fetchall()
	else:
		if (return_date):
			query = 'SELECT airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, flight_status FROM Flight where departure_airport=%s and arrival_airport=%s and departure_date=%s'
			cursor.execute(query, (source_airport, destination_airport, depart_date))
			depart_flights = cursor.fetchall()
			cursor.execute(query, (destination_airport, source_airport, return_date))
			return_flights = cursor.fetchall()
		else:
			query = 'SELECT airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, flight_status FROM Flight where departure_airport=%s and arrival_airport=%s and departure_date=%s'
			cursor.execute(query, (source_airport, destination_airport, depart_date))
			depart_flights = cursor.fetchall()
	cursor.close()
	if (return_date):
		return render_template('search_result.html', departs=depart_flights, returns=return_flights)
	else:
		return render_template('search_result.html', departs=depart_flights)


#customer login
@app.route('/customer_login')
def customer_login():
	return render_template('customer_login.html')
@app.route('/customerLoginAuth', methods=['GET', 'POST'])
def customerLoginAuth():
	#grabs information from the forms
	email = request.form['email']
	customer_password = request.form['customer_password']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Customer WHERE email = %s and customer_password = %s'
	cursor.execute(query, (email, customer_password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['customer'] = email
		return redirect(url_for('customer_home'))
	else:
		#returns an error message to the html page
		error = 'Invalid email or wrong password'
		return render_template('customer_login.html', error=error)


#customer register
@app.route('/customer_register')
def customer_register():
	return render_template('customer_register.html')
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
	#grabs information from the forms
	#email, customer_password, first_name, last_name, building_name, street_name, apt_number, city, state, zipcode, passport_number, passport_country, date_of_birth, log_in_status
	email = request.form['email']
	customer_password = request.form['customer_password']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	phone_number = request.form['phone_number']
	building_name = request.form['building_name']
	street_name = request.form['street_name']
	apt_number = request.form['apt_number']
	city = request.form['city']
	state = request.form['state']
	zipcode = int(request.form['zipcode'])
	passport_number = request.form['passport_number']
	passport_country = request.form['passport_country']
	date_of_birth = request.form['date_of_birth']
	log_in_status = 'online'
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Customer WHERE email = %s'
	cursor.execute(query, (email))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('customer_register.html', error = error)
	else:
		#instruction to add to customer
		ins = "INSERT INTO Customer VALUES("
		for each in [email, customer_password, first_name, last_name]:
			ins = ins + "'" + each + "', "
		for each in [building_name, street_name, apt_number, city, state]:
			if each == '' or each:
				ins = ins + "null, "
			elif isinstance(each, int):
				ins = ins + str(each) + ", "
			else:
				ins = ins + "'" + str(each) + "', "
		ins = ins + str(zipcode) + ", "
		for each in [passport_number, passport_country, date_of_birth]:
			if each == '' or each:
				ins = ins + "null, "
			elif isinstance(each, int):
				ins = ins + str(each) + ", "
			else:
				ins = ins + "'" + str(each) + "', "
		ins = ins + "'" + str(log_in_status) + "')"
		#instruction to add to customer_phone
		phones = str(phone_number).split(',')
		new_ins_lst = []
		for i in range(len(phones)):
			new_ins = "INSERT INTO Customer_phone VALUES('" + email + "', " + phones[i] + ")"
			new_ins_lst.append(new_ins)
		cursor.execute(ins)
		for i in range(len(new_ins_lst)):
			cursor.execute(new_ins_lst[i])
		conn.commit()
		cursor.close()
		session['customer'] = email
		return redirect(url_for('customer_home'))
#customer logout
@app.route('/logout')
def logout():
	session.pop('customer')
	return redirect('/customer_login')


#staff login
@app.route('/staff_login')
def staff_login():
	return render_template('staff_login.html')
@app.route('/staffLoginAuth', methods=['GET', 'POST'])
def staffLoginAuth():
	#grabs information from the forms
	username = request.form['username']
	staff_password = request.form['staff_password']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Airline_staff WHERE username = %s and staff_password = %s'
	cursor.execute(query, (username, staff_password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the staff
		#session is a built in
		session['staff'] = username
		return redirect(url_for('staff_home'))
	else:
		#returns an error message to the html page
		error = 'Invalid email or wrong password'
		return render_template('staff_login.html', error=error)


#staff register
@app.route('/staff_register')
def staff_register():
	return render_template('staff_register.html')
@app.route('/registerAuthStaff', methods=['GET', 'POST'])
def registerAuthStaff():
	auth_codes = ['ABC123', 'DEF456']
	#grabs information from the forms
	# username 	staff_password 	first_name 	last_name 	date_of_birth 	airline_name 	emails	phones
	username = request.form['username']
	staff_password = request.form['staff_password']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	date_of_birth = request.form['date_of_birth']
	airline_name = request.form['airline_name']
	auth_code = request.form['auth_code']
	emails = request.form['emails']
	phones = request.form['phones']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Airline_staff WHERE username = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('staff_register.html', error = error)
	elif (auth_code not in auth_codes):
		error = "Invalid authentication code"
		return render_template('staff_register.html', error = error)
	else:
		#executes query
		ins = "INSERT INTO Airline_staff VALUES("
		for each in [username, staff_password, first_name, last_name, date_of_birth]:
			ins = ins + "'" + each + "', "
		ins = ins + "'" + airline_name + "')"
		print('1 done')
		cursor.execute(ins)
		#instruction to add to staff_phone
		thephones = str(phones).split(',')
		new_ins_lst = []
		for i in range(len(thephones)):
			new_ins = "INSERT INTO Staff_phone VALUES('" + username + "', " + thephones[i] + ")"
			new_ins_lst.append(new_ins)
		for i in range(len(new_ins_lst)):
			cursor.execute(new_ins_lst[i])
		#instruction to add to staff_email
		theemails = str(emails).split(',')
		new_ins_lst = []
		for i in range(len(theemails)):
			new_ins = "INSERT INTO Staff_email VALUES('" + username + "', '" + theemails[i] + "')"
			new_ins_lst.append(new_ins)
		for i in range(len(new_ins_lst)):
			cursor.execute(new_ins_lst[i])
		conn.commit()
		cursor.close()
		session['staff'] = username
		return redirect(url_for('staff_home'))

#staff logout
@app.route('/logout_staff')
def logout_staff():
	session.pop('staff')
	return redirect('/staff_login')





#customer home
@app.route('/customer_home')
def customer_home():
	if ('customer' in session.keys()):
		email = session['customer']
		return render_template('customer_home.html', email=email)
	else:
		return redirect('/')

#view purchased flights
@app.route('/my_flights')
def my_flights():
	if ('customer' not in session.keys()):
		return redirect('/')
	else:
		cursor = conn.cursor()
		query = "SELECT airline_name, flight_number, departure_date, departure_time FROM Customer NATURAL JOIN Purchase NATURAL JOIN Ticket where ((departure_date = NOW() and departure_time > NOW()) or (departure_date > NOW())) and email=%s"
		cursor.execute(query, (session['customer']))
		flights = cursor.fetchall()
		conn.commit()
		cursor.close()
		return render_template('my_flights.html', flights = flights)
@app.route('/update_my_flights', methods=['GET', 'POST'])
def update_my_flights():
	if ('customer' not in session.keys()):
		return redirect('/')
	cursor = conn.cursor()
	option = request.form['dropdown']
	if (option == 'future'):
		query = "SELECT airline_name, flight_number, departure_date, departure_time FROM Customer NATURAL JOIN Purchase NATURAL JOIN Ticket where ((departure_date = NOW() and departure_time > NOW()) or (departure_date > NOW())) and email=%s"
	elif (option == 'past'):
		query = "SELECT airline_name, flight_number, departure_date, departure_time FROM Customer NATURAL JOIN Purchase NATURAL JOIN Ticket where ((departure_date = NOW() and departure_time < NOW()) or (departure_date < NOW())) and email=%s"
	else:
		query = "SELECT airline_name, flight_number, departure_date, departure_time FROM Customer NATURAL JOIN Purchase NATURAL JOIN Ticket where email=%s"
	cursor.execute(query, (session['customer']))
	flights = cursor.fetchall()
	conn.commit()
	cursor.close()
	return render_template('my_flights.html', flights = flights)

#purchasing tickets
@app.route('/ticket_purchase', methods=['GET', 'POST'])
def ticket_purchase():
	if ('customer' not in session.keys()):
		return redirect('/customer_login')
	airline_name = request.form['airline_name']
	flight_number = request.form['flight_number']
	depart_date = request.form['departure_date']
	depart_time = request.form['departure_time']
	return render_template('ticket_purchase.html', airline_name=airline_name, flight_number=flight_number, departure_date=depart_date, departure_time=depart_time)
@app.route('/purchase')


#staff_home
@app.route('/staff_home')
def staff_home():
	if ('staff' in session.keys()):
		username = session['staff']
		return render_template('staff_home.html', username=username)
	else:
		return redirect('/')

#add airplane
@app.route('/add_airplane')
def add_airplane():
	if ('staff' in session.keys()):
		return render_template('add_airplane.html')
	else:
		return redirect('/')
@app.route('/add_airplaneAuth', methods=['GET', 'POST'])
def add_airplaneAuth():
	#data from form
	id = request.form['id']
	seats = request.form['seats']
	manufacturer = request.form['manufacturer']
	manufacturing_date = request.form['manufacturing_date']
	#get airline name
	username = session['staff']
	cursor = conn.cursor()
	query = 'SELECT airline_name FROM Airline_staff WHERE username = %s'
	cursor.execute(query, (username))
	airline_name = cursor.fetchall()[0]['airline_name']
	conn.commit()
	cursor.close()
	#check if airplane already exists
	cursor = conn.cursor()
	query = "SELECT * FROM Airplane WHERE id = %s"
	cursor.execute(query, (id))
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		error = "This airplane already exists"
		return render_template('add_airplane.html', error = error)
	else:
		#add airplane
		ins = "INSERT INTO Airplane VALUES(%s, %s, %s, %s, null, %s)"
		cursor.execute(ins, (id, seats, manufacturer, manufacturing_date, airline_name))
		conn.commit()
		cursor.close()
		return view_airplanes()
@app.route('/view_airplanes')
def view_airplanes():
	if ('staff' in session.keys()):
		username = session['staff']
		print(username)
		cursor = conn.cursor()
		query = 'SELECT airline_name FROM Airline_staff WHERE username = %s'
		cursor.execute(query, (username))		
		airline_name = cursor.fetchall()[0]['airline_name']
		print(airline_name)
		conn.commit()
		cursor.close()
		cursor = conn.cursor()
		query = "SELECT id FROM Airplane WHERE airline_name='" + airline_name + "'"
		cursor.execute(query)
		airplanes = cursor.fetchall()
		print(airplanes)
		conn.commit()
		cursor.close()
		return render_template('view_airplanes.html', airplanes=airplanes)
	else:
		return redirect('/')

#add airport
@app.route('/add_airport')
def add_airport():
	if ('staff' in session.keys()):
		return render_template('add_airport.html')
	else:
		return redirect('/')
@app.route('/add_airportAuth', methods=['GET', 'POST'])
def add_airportAuth():
	#data from form
	airport_code = request.form['airport_code']
	name = request.form['name']
	city = request.form['city']
	country = request.form['country']
	type = request.form['type']
	#check if airport already exists
	cursor = conn.cursor()
	query = "SELECT * FROM Airport WHERE airport_code = %s"
	cursor.execute(query, (airport_code))
	data = cursor.fetchone()
	error = None
	if(data):
		error = "This airport already exists"
		return render_template('add_airport.html', error = error)
	else:
		#add airport
		ins = "INSERT INTO Airport VALUES(%s, %s, %s, %s, %s)"
		cursor.execute(ins, (airport_code, name, city, country, type))
		conn.commit()
		cursor.close()
		return view_airports()
@app.route('/view_airports')
def view_airports():
	if ('staff' in session.keys()):
		cursor = conn.cursor()
		query = "SELECT * FROM Airport"
		cursor.execute(query)
		airports = cursor.fetchall()
		conn.commit()
		cursor.close()
		return render_template('view_airports.html', airports=airports)
	else:
		return redirect('/')

#create new flight
@app.route('/create_new_flights')
def create_new_flights():
	if ('staff' in session.keys()):
		return render_template('create_new_flights.html')
	else:
		return redirect('/')
@app.route('/create_new_flightsAuth', methods=['GET', 'POST'])
def create_new_flightsAuth():
	#data from form
	flight_number = request.form['flight_number']
	base_price = request.form['base_price']
	departure_date = request.form['departure_date']
	departure_time = request.form['departure_time']
	arrival_date = request.form['arrival_date']
	arrival_time = request.form['arrival_time']
	flight_status = 'on time'
	tickets_booked = 0
	id = request.form['id']
	departure_airport = request.form['departure_airport']
	arrival_airport = request.form['arrival_airport']
	#get airline name
	username = session['staff']
	cursor = conn.cursor()
	query = 'SELECT airline_name FROM Airline_staff WHERE username = %s'
	cursor.execute(query, (username))
	airline_name = cursor.fetchall()[0]['airline_name']
	#check if flight already exists
	cursor = conn.cursor()
	query = "SELECT * FROM Flight WHERE flight_number = %s and departure_date = %s and departure_time = %s and airline_name = %s"
	cursor.execute(query, (flight_number, departure_date, departure_time, airline_name))
	data = cursor.fetchone()
	error = None
	if(data):
		error = "This flight already exists"
		return render_template('create_new_flights.html', error = error)
	else:
		#add airport
		ins = "INSERT INTO Flight VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		cursor.execute(ins, (flight_number, base_price, departure_date, departure_time, arrival_date, arrival_time, flight_status, tickets_booked, id, airline_name, departure_airport, arrival_airport))
		conn.commit()
		cursor.close()
		return redirect(url_for('view_flights_staff'))

#change flight status
@app.route('/change_flight_status')
def change_flight_status():
	if ('staff' in session.keys()):
		return render_template('change_flight_status.html')
	else:
		return redirect('/')
@app.route('/change_flight_statusAuth', methods=['GET', 'POST'])
def change_flight_statusAuth():
	#data from form
	flight_number = request.form['flight_number']
	departure_date = request.form['departure_date']
	departure_time = request.form['departure_time']
	flight_status = request.form['flight_status']
	#get airline name
	username = session['staff']
	cursor = conn.cursor()
	query = 'SELECT airline_name FROM Airline_staff WHERE username = %s'
	cursor.execute(query, (username))
	airline_name = cursor.fetchall()[0]['airline_name']
	#change
	ins = "UPDATE Flight SET flight_status=%s WHERE flight_number=%s and departure_date=%s and departure_time=%s and airline_name=%s"
	cursor.execute(ins, (flight_status, flight_number, departure_date, departure_time, airline_name))
	conn.commit()
	cursor.close()
	return render_template('change_flight_status.html', message="Flight status changed successfully")


app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
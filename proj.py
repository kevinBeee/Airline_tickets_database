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
	return render_template('flight_search.html')
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
			query = 'SELECT airline_name, flight_number, departure_date, arrival_date, flight_status FROM Flight where departure_airport in (select airport_code from Airport where city=%s) and arrival_airport in (select airport_code from Airport where city=%s) and departure_date=%s'
			cursor.execute(query, (source_city, destination_city, depart_date))
			depart_flights = cursor.fetchall()
			cursor.execute(query, (destination_city, source_city, return_date))
			return_flights = cursor.fetchall()
		else:
			query = 'SELECT airline_name, flight_number, departure_date, arrival_date, flight_status FROM Flight where departure_airport in (select airport_code from Airport where city=%s) and arrival_airport in (select airport_code from Airport where city=%s) and departure_date=%s'
			cursor.execute(query, (source_city, destination_city, depart_date))
			depart_flights = cursor.fetchall()
	else:
		if (return_date):
			query = 'SELECT airline_name, flight_number, departure_date, arrival_date, flight_status FROM Flight where departure_airport=%s and arrival_airport=%s and departure_date=%s'
			cursor.execute(query, (source_airport, destination_airport, depart_date))
			depart_flights = cursor.fetchall()
			cursor.execute(query, (destination_airport, source_airport, return_date))
			return_flights = cursor.fetchall()
		else:
			query = 'SELECT airline_name, flight_number, departure_date, arrival_date, flight_status FROM Flight where departure_airport=%s and arrival_airport=%s and departure_date=%s'
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
	building_name = request.form['building_name']
	street_name = request.form['street_name']
	apt_number = request.form['apt_number']
	city = request.form['city']
	state = request.form['state']
	zipcode = int(request.form['zipcode'])
	passport_number = request.form['passport_number']
	passport_country = request.form['passport_country']
	date_of_birth = request.form['date_of_birth']
	log_in_status = 'offline'
	tryuse = ''
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
		cursor.execute(ins)
		conn.commit()
		cursor.close()
		return render_template('customer_home.html')


#Define route for staff login
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


#Define route for staff register
@app.route('/staff_register')
def staff_register():
	return render_template('staff_register.html')


#Authenticates the staff login


@app.route('/customer_home')
def customer_home():
    return "hello customer"
    # username = session['username']
    # cursor = conn.cursor();
    # query = 'SELECT ts, blog_post FROM blog WHERE username = %s ORDER BY ts DESC'
    # cursor.execute(query, (username))
    # data1 = cursor.fetchall() 
    # for each in data1:
    #     print(each['blog_post'])
    # cursor.close()
    # return render_template('customer_home.html', username=username, posts=data1)

@app.route('/staff_home')
def staff_home():
    return "hello staff"
    # username = session['username']
    # cursor = conn.cursor();
    # query = 'SELECT ts, blog_post FROM blog WHERE username = %s ORDER BY ts DESC'
    # cursor.execute(query, (username))
    # data1 = cursor.fetchall() 
    # for each in data1:
    #     print(each['blog_post'])
    # cursor.close()
    # return render_template('staff_home.html', username=username, posts=data1)

		
@app.route('/post', methods=['GET', 'POST'])
def post():
	username = session['username']
	cursor = conn.cursor();
	blog = request.form['blog']
	query = 'INSERT INTO blog (blog_post, username) VALUES(%s, %s)'
	cursor.execute(query, (blog, username))
	conn.commit()
	cursor.close()
	return redirect(url_for('customer_home'))

@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')
		
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
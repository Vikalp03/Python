from flask import Flask, render_template, request        #importing of modules using pip command
from flaskext.mysql import MySQL

app = Flask(__name__)



#certain parameters need to be configured to connect this app to the database

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'userdata'

mysql = MySQL()       #instantiation of MySQL module
mysql.init_app(app)    


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':

	        #fetch the user details
		admin_details = request.form
		email = admin_details['Email']
		password = admin_details['Password']
		cur = mysql.get_db().cursor()
		cur.execute("INSERT INTO credentials(username,password) VALUES(%s, %s)",(email, password))
		mysql.connection.commit()

		return 'Success'
	return render_template('index.html')     #render function to render the index.html template

if __name__ == '__main__':
	app.run(debug=True)         #set debug to true to keep yourself free from starting the server again          

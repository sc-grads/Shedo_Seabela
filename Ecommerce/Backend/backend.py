from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app,origins=['http://localhost:4200'])



# define your database connection string
conn_str = 'DRIVER={SQL Server};SERVER=DESKTOP-614IP3I\SQLEXPRESS;DATABASE=Details;Trusted_Connection=yes;'

@app.route('/register', methods=['POST'])
def register():
    # get registration details from request body
    data = request.json
    
    username = data['username']
    password = data['password']

    # connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # insert registration details into database
    query = "INSERT INTO UserInfo( Username, Password_re) VALUES (?, ?)"
    values = ( username, password)
    cursor.execute(query, values)
    conn.commit()

    # close database connection
    cursor.close()
    conn.close()

    # return success message to Angular
    return jsonify({'message': 'Registration successful'})

if __name__ == '__main__':
    app.run(debug=True)

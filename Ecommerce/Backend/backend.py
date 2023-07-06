from flask import Flask, request, jsonify,json
import pyodbc
from collections import namedtuple
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

@app.route('/login', methods=['POST'])
def login():
    # get login details from request body
    data = request.json
    
    username = data['username']
    password = data['password']

    # connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # insert registration details into database
    query = "SELECT * FROM UserInfo WHERE username = ? AND password_re = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.commit()
    if result:
        # based on the truthness of the result we now want to check the role of the user
        query = "SELECT Assignment FROM UserInfo WHERE username = ? AND password_re = ?"
        cursor.execute(query, (username, password))
        role = cursor.fetchone()
        
        if role[0] == "Admin_re":
            # print(role)
            return jsonify({'message': 'Admin'})
        
        # Authentication successful
        return jsonify({'message': 'Login successful'})
    else:
        # Authentication failed
        return jsonify({'message': 'Invalid username or password'})

    # close database connection
    cursor.close()
    conn.close()


@app.route('/items', methods=['GET'])
def get_products():
    try:
        # Connect to the database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Retrieve all products
        query = "SELECT * FROM ProductInfo"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert the query results to a list of dictionaries
        columns = [column[0] for column in cursor.description]
        products = [dict(zip(columns, row)) for row in rows]

        
        # Close the database connection
        cursor.close()
        conn.close()

        # Return the products as JSON response
        return jsonify(products)

    except pyodbc.Error as e:
        # Handle database connection or query errors
        error_message = "An error occurred while retrieving products: {}".format(str(e))
        return jsonify({'error': error_message}), 500
    


@app.route('/addproducts', methods=['POST'])
def Addproduct():
    # get details from request body
    data = request.json
    
    Product = data['Product']
    Description = data['Description']
    Price = data['Price']
    ProductImage = data['ProductImage']

    # connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # insert product details into database
    query = "INSERT INTO ProductInfo( Product, Description_re, Price, ProductImage ) VALUES (?, ?, ?, ?)"
    values = ( Product, Description, Price, ProductImage)
    cursor.execute(query, values)
    conn.commit()

    # close database connection
    cursor.close()
    conn.close()

    # return success message to Angular
    return jsonify({'message': 'Item added successful'})

@app.route('/deleteproducts/<int:ProductID>', methods=['DELETE'])
def DeleteProducts(ProductID):
    # data = request.json
    # Productid = data['ProductID']
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    
    # query = "DELETE FROM ProductInfo WHERE ProductID = "
    # values = ( Productid,)
    cursor.execute(f"DELETE FROM ProductInfo WHERE ProductID ={ProductID} ")
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({'message': 'Product deleted successfully'})

@app.route('/AddToCart', methods=['POST'])
def AddToCart(ProductID):
    
    # conn = pyodbc.connect(conn_str)
    # cursor = conn.cursor()

    
    # query = "DELETE FROM ProductInfo WHERE ProductID = "
    # values = ( Productid,)
    # cursor.execute(f"DELETE FROM ProductInfo WHERE ProductID ={ProductID} ")
    # conn.commit()
    print('Hello am working')
    # cursor.close()
    # conn.close()
    return jsonify({'message': 'Product deleted successfully'})
    
if __name__ == '__main__':
    app.run(debug=True)

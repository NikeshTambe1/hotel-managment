from flask import Flask, render_template, request, jsonify, g
import mysql.connector

app = Flask(__name__)

DATABASE_HOST = "localhost"
DATABASE_USER = "root"
DATABASE_PASSWORD = "nikeshtambe"
DATABASE_NAME = "hotelmanagment"

# Database connection functions
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME
        )
    return g.db

def get_cursor():
    return get_db().cursor()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')  
@app.route("/gallary")  
def gallary():
    return render_template('gallary.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/Room Booking")
def Room_Booking():
    cursor = get_cursor()

    select_query = "SELECT * FROM room1"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    data = []
    for row in rows:
        item = {
            'column1': row[0],
            'column2': row[1],
             'column3': row[2],
              'column4': row[3],
               'column5': row[4],
              'column6': row[5],
              'image': row[6],

            # Add more columns as needed
        }
        
        data.append(item)
        print(item)

    cursor.close()
    return render_template('Room Booking.html', data=data)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/book-now")
def book_now():
    return render_template('book-now.html')

@app.route("/Services")
def service():
    return render_template('Services.html')


@app.route('/thank-you', methods=['POST'])
def thank_you():
    cursor = get_cursor()

    name = request.form.get('name')
    email = request.form.get('email')
    contactnumber= request.form.get('contactnumber')
    checkindate= request.form.get('checkindate')
    outindate = request.form.get('outindate ')

    insert_query = "INSERT INTO contact_us(name, email, contactnumber, checkindate, outindate ) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (name, email, contactnumber, checkindate, outindate ))



    name1=request.form.get('name')
    email1=request.form.get('email')
    mobile1=request.form.get('mobile')
    message=request.form.get('message')

    insert_query="INSERT INTO contact (name,email,mobile_no,message)VALUES(%s,%s,%s,%s)"
    cursor.execute(insert_query,(name1,email1,mobile1,message))


    g.db.commit()
    cursor.close()
    return render_template('thankyou.html')

@app.route("/display-data")
def display_data():
    cursor = get_cursor()

    select_query = "SELECT * FROM contact_us"
    cursor.execute(select_query)

    rows = cursor.fetchall()

    data = []
    for row in rows:
        item = {
            'column1': row[0],
            'column2': row[1],
            # Add more columns as needed
        }
        data.append(item)

    cursor.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

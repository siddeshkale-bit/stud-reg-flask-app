from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Siddhu@1005',
    'database': 'studentdb'
}

# -----------------------------------------------------------
# Home page – Registration Form
# -----------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
        INSERT INTO students (name, email, phone, course, address)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (name, email, phone, course, address)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return "Student Registered Successfully!"

    return render_template('register.html')

# -----------------------------------------------------------
# Students List Page
# -----------------------------------------------------------
@app.route('/students')
def students():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('students.html', students=data)

# -----------------------------------------------------------
# Edit Student Page
# -----------------------------------------------------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']

        update_query = """
        UPDATE students
        SET name=%s, email=%s, phone=%s, course=%s, address=%s
        WHERE id=%s
        """

        cursor.execute(update_query, (name, email, phone, course, address, id))
        conn.commit()

        cursor.close()
        conn.close()
        return "Student Updated Successfully!"

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('edit.html', student=student)

# -----------------------------------------------------------
# Start Flask Server
# -----------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


from sqlite3 import *
import os
from flask import *

db = 'database.db'


def save_lead(request):
    conn = None
    if request.method == 'POST':
        try:
            full_name = str(request.form['full_name'])
            phone_number = str(request.form['phone_number'])
            email = str(request.form['email'])

            with connect("database.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO leads (full_name, phone_number, email) VALUES (?,?,?)",
                               (full_name, phone_number, email))

                conn.commit()
                msg = "Lead successfully created"

        except Exception as e:
            msg = 'Order creation failed: "{}"'.format(e.message)

        finally:
            if conn is not None:
                conn.close()
            return render_template("thank_you.html")

from flask import Flask, render_template,request
import psycopg

app= Flask(__name__)
def get_db_connection():
    return psycopg.connect(
        dbname="chargeconnect",
        user="postgres",
        password="jungkook",
        host="localhost",
        port="5432"
    )

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/driver", methods=["GET","POST"])
def driver():
    if request.method=="POST":
        name=request.form.get("full_name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        vehicle=request.form.get("vehicle_type")
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Vehicle:", vehicle)

        connection= get_db_connection()
        connection.execute(
            """
            INSERT INTO drivers (name, email, phone, vehicle)
            VALUES (%s, %s, %s, %s)
            """,
            (name, email, phone, vehicle)
            )

        connection.commit()
        connection.close()
        print("registration complete")
    return render_template("driver.html")
@app.route("/host")
def host():
    return render_template("host.html")

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, render_template,request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/driver", methods=["GET","POST"])
def driver():
    if request.method=="POST":
        name=request.form.get("full_name")
        print(name)
    return render_template("driver.html")
@app.route("/host")
def host():
    return render_template("host.html")

if __name__=="__main__":
    app.run(debug=True)

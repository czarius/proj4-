from flask import Flask,redirect,url_for,url_for,render_template,request
import solr

app = Flask(__name__)

@app.route("/1",methods=["POST","GET"])
def home():
    if request.method=="POST":
        user = request.form["nm"]
        k=solr.script(user)
        return render_template("login.html")
    else:
        return render_template("index.html")

#@app.route("/login", methods=["POST","GET"])
#def login():
    #search=request.form['search']
#    if request.method=="POST":
#        user = request.form["nm"]
#        return redirect(url_for("user",usr=user))
#    else:
#        return render_template("login.html")
@app.route("/<usr>")
def user(usr):
    return f"<h1{usr}</h1>"

if __name__=='__main__':
    app.run(debug=True)
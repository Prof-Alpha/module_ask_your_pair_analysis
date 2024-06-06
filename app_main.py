from flask import Flask, render_template, flash, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "helloppppssxtuuuggggvv"

@app.route("/")
def home():
    return render_template("home.html", test_content="this is a test content")

@app.route("/analysis_request", methods=['POST'])
def analysis_request():
    f = open("analysis_requests.txt", "a")
    # users_request = get the inpute from the users
    users_request = "test request: BtcUsdt \n"
    users_request = request.form['text1']
    f.write("\n" + users_request)
    f.close()
    flash(users_request)
    return redirect(url_for("home"))

# blog route-ing
@app.route("/blog/<int:id_for_blog>")
def blog():
    pass
    # redirect to @app.route("/blog/<int:id_for_blog>"): how to dynamic urls?
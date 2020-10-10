"""
A Flask application that wraps around AI/ML models.
Qxf2 wrote this to help testers practice testing AI/ML based applications.
To learn more, see the README.md of this application.
"""
from flask import Flask, jsonify, render_template, request
import is_pto.is_pto as pto_classifier
app = Flask(__name__)

@app.route("/")
def index():
    "Home page"
    return render_template("index.html")

@app.route("/about")
def about():
    "About page"
    return render_template("about.html")

@app.route("/is-pto", methods=['GET', 'POST'])
def is_pto():
    "Is the message a PTO?"
    response = render_template("is_pto.html")
    if request.method == 'POST':
        message = request.form.get('message')
        prediction_score = pto_classifier.is_this_a_pto(message)
        prediction_text = "a PTO" if prediction_score==1 else "not a PTO"
        prediction_text = f'"{message}" is {prediction_text} message'
        response = jsonify({"answer": prediction_text})

    return response

#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464, debug= True)

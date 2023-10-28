from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# The API endpoint for email verification
API_URL = "https://emailable.com/test-email-verifier"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]

        if not email:
            return "Please enter an email address."

        payload = {"email": email}
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            try:
                data = response.json()
                return render_template("response.html", data=data)
            except ValueError:
                return "Invalid response from the API."
        else:
            return "An error occurred while verifying the email."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

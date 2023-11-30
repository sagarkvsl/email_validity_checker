from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# The new API endpoint for email verification
API_URL = "https://api.emailable.com/v1/verify"

# Your API key
API_KEY = "live_acec266ebba3820e650e"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]

        if not email:
            return "Please enter an email address."

        # Construct the URL with the email and API key
        url = f"{API_URL}?email={email}&api_key={API_KEY}"

        response = requests.get(url)

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

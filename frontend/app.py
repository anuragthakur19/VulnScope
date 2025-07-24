from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/scan"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        domain = request.form.get("domain")
        try:
            response = requests.post(FASTAPI_URL, json={"domain": domain})
            if response.status_code == 200:
                result = response.json()
            else:
                error = response.json().get("detail", "Scan failed.")
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)

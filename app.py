from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process_variable")
def process_variable():
    variable = request.args.get("variable")
    response = f"You sent: {variable}"
    return response

if __name__ == "__main__":
    app.run()

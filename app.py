from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask inside Docker!"

if __name__ == "__main__":
    # Important: host='0.0.0.0' so it's reachable outside the container
    app.run(host="0.0.0.0", port=5000)

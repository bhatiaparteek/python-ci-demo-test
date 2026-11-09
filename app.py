from flask import Flask

app = Flask(__name__)


def add(a, b):
    return a + b


@app.route("/")
def home():
    return f"App is running! 3 + 32 = {add(3, 32)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

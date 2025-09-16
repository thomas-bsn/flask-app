from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return "Welcome!"

@app.get("/ulala")
def ulala():
    return "Hey babe, how are you?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

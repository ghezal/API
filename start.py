from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    print "printing desktop.jpg"
    return send_from_directory('../','desktop.jpg')

if __name__ == "__main__":
    app.run()

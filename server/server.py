from flask import Flask, render_template

from config import SERVER
from victim import VICTIM

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", victim=VICTIM)

if __name__ == "__main__":
    app.run(host=SERVER["host"], port=SERVER["port"])
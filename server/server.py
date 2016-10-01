from flask import Flask, jsonify

from config import SERVER
from victim import VICTIM

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(VICTIM)
    # return render_template("index.html", victim=VICTIM)

if __name__ == "__main__":
    app.run(port=SERVER["port"])
import sys
from flask import jsonify

from app import application
from victim import VICTIM

@application.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(VICTIM)
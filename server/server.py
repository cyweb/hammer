from flask import Flask, jsonify

from app import application

if __name__ == "__main__":
    application.run(port=3000)
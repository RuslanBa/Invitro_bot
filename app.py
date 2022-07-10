from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()

print('i am ready')

if __name__ == '__main__':
    app.run()
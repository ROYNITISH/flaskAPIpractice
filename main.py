from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def hello():
  return jsonify(message="HelloWorld"),200
@app.route('not_found')
def not_found():
  return jsonify(message="page not found"),404
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
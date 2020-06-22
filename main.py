from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def simpple():
  return jsonify(message="HelloWorld")
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
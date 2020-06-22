from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route('/')
def hello():
  return jsonify(message="HelloWorld")

@app.route('/not_found')
def not_found():
  return jsonify(message="route not found"),404


@app.route('/parameters')
def parameters():
  name = request.args.get('name')
  age = int(request.args.get('age'))
  if age  < 18:
    return jsonify(message="Sorry "+ name + " you are not old enough"),401

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
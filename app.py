from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Herok"

@app.route('/hello/<string:name>')
def Home(name):
	return render_template('index.html', name_html=name)

@app.route('/store/<string:name>')
def Store(name):
	items = [{'name': 'Ice cream', 'price': 50},
			 {'name': 'Cookie', 'price': 35},
			 {'name': 'Chocolate', 'price': 40},
			 {'name': 'Milk', 'price': 32.5}]
	return render_template('temp.html', name=name, items=items)

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False)

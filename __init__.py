from flask import Flask, render_template, request
import pins

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", light="on")

@app.route("/lights", methods=['POST','GET'])
def lights():
	value = request.args['light']
	if value=="on":
		value = "off"
		pins.ledon()
	else:
		value="on"
		pins.ledoff()
	return render_template("index.html", light=value)

if __name__=="__main__":
	pins.init()
	app.run(debug=True, host='0.0.0.0', port=80)

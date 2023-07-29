from flask import Flask, request, jsonify, render_template, Response
import logging
import ee

#try:
#    ee.Initialize()
#except Exception as e:
#    ee.Authenticate()
#    ee.Initialize()

logging.basicConfig(filename='/app/api.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
logging.info("Starting the app...")

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('home.html')

@app.route('/map')
def logging_scars_page():
    return render_template('map.html')

@app.route('/generate', methods = ['POST'])
def generate_mask():
    data = request.get_json()
    return jsonify([data["coord"]])

if __name__ == '__main__':
    app.run(port=5500, host="0.0.0.0", debug=True)

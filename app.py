from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import os
from logistic_regression import do_experiments

app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle experiment parameters and trigger the experiment
@app.route('/run_experiment', methods=['POST'])
def run_experiment():
    start = float(request.json['start'])
    end = float(request.json['end'])
    step_num = int(request.json['step_num'])

    # Run the experiment with the provided parameters
    dataset_filename, parameters_filename = do_experiments(start, end, step_num)

    # Construct URLs to access the generated images
    dataset_img_url = url_for('static', filename=dataset_filename)
    parameters_img_url = url_for('static', filename=parameters_filename)
    print(dataset_img_url)
    print(parameters_img_url)
    return jsonify({
        "dataset_img": dataset_img_url,
        "parameters_img": parameters_img_url
    })

# Route to serve result images
@app.route('/results/<filename>')
def results(filename):
    return send_from_directory('results', filename)

if __name__ == '__main__':
    app.run(debug=True)
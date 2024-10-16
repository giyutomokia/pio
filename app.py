from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return app.send_static_file('index.html')
@app.route('/')
def home():
    return "Welcome to the Rule Engine Application!"

# Other routes and logic here...
@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.json
    rule_string = data.get('rule_string')
    # Process the rule_string to create the AST...
    return jsonify({"message": "Rule created successfully", "rule_string": rule_string})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    data = request.json
    attributes = data.get('attributes')
    # Evaluate the rule using the attributes...
    return jsonify({"result": True})  # Return actual evaluation result
@app.route('/create_rule', methods=['POST'])  # Only accepts POST
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string')
    # Your logic for processing rule_string
    return jsonify({"message": "Rule created successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)

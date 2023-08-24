from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
from flask_cors import CORS
from datetime import datetime, timedelta
from tests.test_azure_openai import *
from tests.test_azure_openai import chatbot_agent

app = Flask(__name__)
CORS(app)
load_dotenv()

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    res = chatbot_agent(request.json['question'])
    response = {
        "message": res,
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

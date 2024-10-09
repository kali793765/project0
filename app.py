########################################################################
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import pandas as pd
from faker import Faker

app = Flask(__name__)

# Initialize Faker
fake = Faker()

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        key = request.json['key']
        data = request.json['data'].encode()
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(data)
        return jsonify({'encrypted_data': encrypted_data.decode()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/anonymize', methods=['POST'])
def anonymize():
    try:
        # Get data from request
        data = request.json['data']
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Anonymize the 'Email' column using Faker
        df['Email'] = df['Email'].apply(lambda x: fake.email())
        
        # Convert DataFrame back to JSON
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '_main_':
    app.run(debug=True)
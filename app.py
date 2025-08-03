from flask import Flask, render_template, request, jsonify, send_file
import os
import json
from ai_assistant import AIAssistant
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global assistant instance
assistant = AIAssistant()

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Process the message with the assistant
        response = assistant.process_request(user_message)
        
        return jsonify({
            'response': response,
            'loaded_datasets': assistant.get_loaded_datasets()
        })
        
    except Exception as e:
        return jsonify({'error': f'Error processing message: {str(e)}'}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Load the data using the assistant
            result = assistant.load_data(filepath)
            
            if 'error' in result:
                return jsonify({'error': result['error']}), 400
            
            return jsonify({
                'message': f'File {filename} uploaded and loaded successfully!',
                'dataset_info': result,
                'loaded_datasets': assistant.get_loaded_datasets()
            })
        
        return jsonify({'error': 'Invalid file type. Please upload CSV or Excel files.'}), 400
        
    except Exception as e:
        return jsonify({'error': f'Error uploading file: {str(e)}'}), 500

@app.route('/analyze/<dataset_name>/<analysis_type>')
def analyze_dataset(dataset_name, analysis_type):
    """Perform analysis on a specific dataset"""
    try:
        result = assistant.analyze_data(dataset_name, analysis_type)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Error analyzing dataset: {str(e)}'}), 500

@app.route('/insights/<dataset_name>')
def get_insights(dataset_name):
    """Get insights for a specific dataset"""
    try:
        insights = assistant.generate_insights(dataset_name)
        return jsonify({'insights': insights})
    except Exception as e:
        return jsonify({'error': f'Error generating insights: {str(e)}'}), 500

@app.route('/query/<dataset_name>')
def query_dataset(dataset_name):
    """Query a specific dataset"""
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify({'error': 'No query provided'}), 400
        
        result = assistant.query_data(dataset_name, query)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Error querying dataset: {str(e)}'}), 500

@app.route('/visualize/<dataset_name>/<viz_type>')
def create_visualization(dataset_name, viz_type):
    """Create visualization for a dataset"""
    try:
        result = assistant.create_visualization(dataset_name, viz_type)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Error creating visualization: {str(e)}'}), 500

@app.route('/datasets')
def get_datasets():
    """Get information about loaded datasets"""
    return jsonify(assistant.get_loaded_datasets())

@app.route('/conversation_history')
def get_conversation_history():
    """Get conversation history"""
    return jsonify(assistant.get_conversation_history())

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'AI Assistant is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
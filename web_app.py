"""
Web application for the construction materials product database.
This application allows users to view products, leave comments, and receive AI-generated responses.
"""
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv
from src.gemini_client import GeminiClient
from src.db.product_db import ProductDB
from src.message_handler import MessageHandler

# Load environment variables
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Initialize components
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

gemini_client = GeminiClient(api_key)
product_db = ProductDB()
message_handler = MessageHandler(gemini_client, product_db)

# Store comments and responses in memory (in a real application, this would be in a database)
comments = {}  # product_id -> list of {comment, response} dictionaries

@app.route('/')
def index():
    """Render the home page with a list of products."""
    products = product_db.get_all_products()
    return render_template('index.html', products=products)

@app.route('/product/<product_id>')
def product_detail(product_id):
    """Render the product detail page."""
    product = product_db.get_product_by_id(product_id)
    if not product:
        return redirect(url_for('index'))
    
    # Get comments for this product
    product_comments = comments.get(product_id, [])
    
    return render_template('product_detail.html', product=product, comments=product_comments)

@app.route('/api/comment', methods=['POST'])
def add_comment():
    """API endpoint for adding a comment and getting a response."""
    data = request.json
    product_id = data.get('product_id')
    comment_text = data.get('comment')
    
    if not product_id or not comment_text:
        return jsonify({'status': 'error', 'message': 'Missing product_id or comment'}), 400
    
    # Process the comment
    message_data = {
        'product_id': product_id,
        'message': comment_text
    }
    
    response_data = message_handler.process_message(message_data)
    
    # Store the comment and response
    if product_id not in comments:
        comments[product_id] = []
    
    comments[product_id].append({
        'comment': comment_text,
        'response': response_data['response']
    })
    
    return jsonify({
        'status': 'success',
        'response': response_data['response']
    })

if __name__ == '__main__':
    # Create the templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create the static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Run the Flask application
    app.run(debug=True)

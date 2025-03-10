#!/usr/bin/env python
# coding: utf-8

# In[1]:

#get_ipython().system('pip install flask')

# In[ ]:

from flask import Flask, request, jsonify
from nlp import search_text  # Ensure 'nlp.py' exists
from recommend import train  # Ensure 'recommend.py' exists
import database  # Ensure 'database.py' exists

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Flask App!"

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')  # Use .get() for safety
    if not query:
        return jsonify({"error": "No query provided"}), 400
    result = search_text(query)
    return jsonify({"result": result})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json.get('data')
    target = request.json.get('target')
    if data is None or target is None:
        return jsonify({"error": "Missing data or target"}), 400
    train(data, target)
    return jsonify({"status": "trained"})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8080)


# In[ ]:





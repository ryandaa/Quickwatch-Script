from flask import Flask, request, jsonify
from transcriptget import get_summary_from_url
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import openai
import os

app = Flask(__name__)
CORS(app)

@app.route('/get_summary', methods=['POST'])

def get_summary():
    data = request.json
    url = data['url']
    summary = get_summary_from_url(url)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
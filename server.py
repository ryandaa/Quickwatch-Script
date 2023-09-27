from flask import Flask, request, jsonify
from transcriptget import get_summary_from_url
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import openai
import os

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": ["https://quickwatchv1-ryanda977-gmailcom.vercel.app", "https://quickwatchv1.vercel.app", "https://quickwatch.info", "https://www.quickwatch.info", "http://localhost:5173", "http://localhost:8000"]}})

@app.route('/', methods=['POST'])

def get_summary():
    data = request.json
    url = data['url']
    summary = get_summary_from_url(url)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)

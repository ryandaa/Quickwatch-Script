from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import openai
import os

OPENAI_KEY = os.environ.get("OPENAI_KEY")

def get_summary_from_url(url):
    # extracts video ID
    parsed_url = urlparse(url)

    if parsed_url.netloc == 'www.youtube.com' and parsed_url.path == '/watch':
        query_params = parse_qs(parsed_url.query)
        video_id = query_params.get('v', [None])[0]
    else:
        return "Invalid URL"

    # gets transcript
    tx = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    outls = []
    
    for i in tx:
        outtxt = i['text']
        outls.append(outtxt)
    transcript = ' '.join(outls)

    # summarizes transcript
    openai.api_key = "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"

    system_message = {
        "role": "system",
        "content": "You are a master at summarizing video transcripts."
    }
    user_message = {
        "role": "user",
        "content": f"Please summarize this transcript and give a digestible summary that anyone can understand. Be elaborate, but yet concise and include key details. Keep it to one paragraph. Also, please do not use the word 'transcript' while in the summary. Here is the transcript.: {transcript}"
    }
    messages = [system_message, user_message]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.4,
        max_tokens=1024
    )
    summary = response['choices'][0]['message']['content'].strip()

    return summary
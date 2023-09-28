# Quickwatch-Script

## Description
Quickwatch-Script is a backend function that is developed with Flask, designed to create the entire experience of the Quickwatch website. The primary function of this script is to fetch YouTube transcripts from a parsed YouTube URL and then summarize the content using the OpenAI API. This provides users with concise and relevant information from lengthy YouTube videos, making it easier to grasp the main points without watching the entire content.

To make it run, users will have to enter: 

**
python server.py**


## Key Functions

### 1. `server.py`
This function serves as the backbone of the script, handling the main server operations and ensuring smooth communication between the website and the OpenAI API.

### 2. `transcriptget.py`
As the name suggests, this function is responsible for extracting transcripts from the provided YouTube URL. It parses the URL, fetches the transcript, and prepares it for further processing by the OpenAI API.

## Usage
To utilize the Quickwatch-Script, follow the instructions provided in the repository. Ensure you have the necessary dependencies installed and the API keys set up.

## Contribution
Contributions to improve the functionality and efficiency of the Quickwatch-Script are always welcome. Please refer to the repository's guidelines for more details.

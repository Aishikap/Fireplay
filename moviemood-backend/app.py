from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from scraper import locate_url, scrape_IMDB

# Add these lines to import your emotion detection function
import sys
sys.path.append('../Emotion-detection/src')  # Adjust path if needed
# from emotions import detect_emotion

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    # Get mood(s) from form
    mood_str = request.form.get('mood', '')
    emotions = [m.strip() for m in mood_str.split(',') if m.strip()]
    url_lst = locate_url(emotions)
    movie_dict = {}
    for url in url_lst:
        if "www.imdb.com" in url:
            if len(emotions) == 1:
                movie_dict.update(scrape_IMDB(url, 12))
            elif len(emotions) == 2:
                movie_dict.update(scrape_IMDB(url, 6))
            elif len(emotions) == 3:
                movie_dict.update(scrape_IMDB(url, 4))
    return render_template('results.html', moods=emotions, movies=movie_dict)

# New endpoint for emotion detection via camera
@app.route('/detect_emotion', methods=['GET'])
def detect_emotion_route():
    emotion = ""
    with open('../Emotion-detection/emotions.txt', 'r') as file:
        lines = file.readlines()
        emotion = lines[-1].strip() if lines else ""
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(port=5001, debug=True, threaded=True)
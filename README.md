# FirePlay – Emotion-Based Movie Recommendation and Watch Party Platform

FirePlay is a prototype application that enhances the streaming experience by combining emotion detection with real-time watch parties. The app detects your mood through your webcam and provides personalized movie recommendations based on it. It also lets you host or join watch parties with friends using synchronized video playback.

---

## Features

### Emotion-Based Movie Recommendation
- Detects user emotions in real-time using a webcam.
- Maps emotions to predefined movie genres.
- Scrapes movie data (titles and summaries) from IMDb using BeautifulSoup.
- Displays personalized recommendations on the frontend.

### Watch Party
- Create or join rooms using room codes.
- Share and queue YouTube video URLs.
- Real-time synchronization of play/pause across users using Redis and WebSockets.
- Collaborative video control for a shared viewing experience.

### Vision for Future
- One-click Watch Party buttons beside movies.
- Seamless integration with OTT platforms like Amazon Prime and Netflix on Fire TV using user subscription tokens.
- Continuous emotion tracking with minimal user interaction for a smoother, more immersive experience.

---

## Tech Stack

- **Frontend**: Next.js (React), TailwindCSS
- **Backend**: FastAPI, Redis, WebSockets
- **Emotion Detection**: OpenCV, Tensorflow, Deep Learning Models (Python)
- **Web Scraping**: BeautifulSoup
- **Real-Time Communication**: Redis Pub/Sub, WebSockets

---

## Demo

[Watch Demo Video](#)  
(https://drive.google.com/file/d/1DdBTUTv80U6ZVwBWE5yuKmrVJ_vSOkvH/view?usp=drive_link)

---

## Dataset for Emotion detection model (CSV file to be kept in Emotion-detection/src folder)

Download and use the FER-2013 CSV dataset file.

---

## Installation

Follow the steps below to get the application running locally:

### 1. Clone the Repository

```bash
git clone https://github.com/adityachoudhury29/FirePlay.git
cd FirePlay

2. Set Up Python Environment

# Create a virtual environment inside the project root
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

3. Start Frontend (in a new terminal)

npm install
npm run dev

4. Start Backend API Server (in a new terminal with the virtual environment activated)

cd moviemood-backend
python app.py

5. Start Emotion Detector (in another terminal with the virtual environment activated)

cd Emotion-detection/src
python emotions.py --mode display

6. Access the Application

Open your browser and visit:
http://localhost:3000

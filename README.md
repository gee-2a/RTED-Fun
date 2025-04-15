
# RTED FUN 🎭 - Real-Time Emotion Detection with Fun Reactions & Games

**RTED FUN** is a fun and interactive real-time emotion detection project built with Flask and OpenCV. It features **two exciting modes**:

1. **Emotion Reaction Mode (`app1.py`)** – Detects user emotions in real time and responds with matching **emojis** and **songs**.
2. **Emotion Mimic Game (`app.py`)** – Challenges the user to mimic randomly selected emotions and checks if their expression matches!

## 📁 Folder Structure
RTED-FUN/
├── app1.py           # Emotion-based reaction mode (emojis + songs)
├── app.py         # Emotion mimic game mode
├── train.py         # CNN model architecture and training
├── templates/
│   ├── index.html   # UI for emotion mimic game
│   └── index1.html  # UI for emoji + song reaction mode
├── static/
│   ├── emojis/      # Emoji images (happy.png, sad.png, etc.)
│   └── songs/       # Emotion-specific songs (happy.mp3, angry.mp3, etc.)
└── README.md        # Project 

 Add Your Emojis and Songs

This project does not include emojis and songs due to copyright and personalization reasons.

Please add your own emoji images and audio files in the following directories:
	•	static/emojis/
Example filenames:
	•	happy.png
	•	sad.png
	•	angry.png
	•	neutral.png
	•	etc.
	•	static/songs/
Example filenames:
	•	happy.mp3
	•	sad.mp3
	•	angry.mp3
	•	etc.



Note: You are free to use your favorite emojis and songs!


📦 Features
	•	CNN-based emotion detection
	•	Real-time webcam feed processing
	•	Emoji and song feedback for 7 emotions
	•	Emotion tracking and chart visualization
	•	Emotion mimic game mode with feedback
	•	Multiple face detection support (in reaction mode)

🛠 Built With
	•	Python
	•	Flask
	•	OpenCV
	•	TensorFlow/Keras
	•	Matplotlib

⸻

🧠 Emotions Supported
	•	Happy 😊
	•	Sad 😢
	•	Angry 😠
	•	Surprise 😮
	•	Fear 😨
	•	Disgust 🤢
	•	Neutral 😐

⸻

💡 Ideas for Extension
	•	Add GIFs instead of emojis
	•	Emotion log history and downloadable reports
	•	Leaderboard for the mimic game
	•	Notification system for extreme emotional shifts
	•	Emotion-triggered light effects or visuals


⸻

Have fun detecting and playing with emotions! 💖

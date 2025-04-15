from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import random
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

app = Flask(__name__)

# Load model
emotion_model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(1024, activation='relu'),
    Dropout(0.5),
    Dense(7, activation='softmax')
])
emotion_model.load_weights('model.weights.h5')

# Mappings
emotion_dict = {
    0: "Angry", 1: "Disgusted", 2: "Fearful",
    3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"
}
emoji_dist = {
    0: "angry.jpeg",
    1: "disgust.png",
    2: "fear.jpeg",
    3: "happy.jpeg",
    4: "neutral.jpeg",
    5: "sad.jpeg",
    6: "surprise.jpeg"
}

# Globals
last_emotion = 4
challenge_emotion = 4
cap = cv2.VideoCapture(0)

def gen_frames():
    global last_emotion
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = emotion_model.predict(cropped_img, verbose=0)
            maxindex = int(np.argmax(prediction))
            last_emotion = maxindex

            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            cv2.putText(frame, emotion_dict[last_emotion], (x + 20, y - 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/emotion')
def get_emotion():
    return jsonify({
        'emotion': emotion_dict[last_emotion],
        'emoji': emoji_dist[last_emotion]
    })

@app.route('/start_challenge')
def start_challenge():
    global challenge_emotion
    challenge_emotion = random.randint(0, 6)
    return jsonify({
        'emotion': emotion_dict[challenge_emotion],
        'emoji': emoji_dist[challenge_emotion]
    })

@app.route('/get_current_emotion')
def get_current_emotion():
    return jsonify({
        'emotion': emotion_dict[last_emotion]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5050)

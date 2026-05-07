import cv2
import numpy as np
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

model_filename = "face_recognition_model.pkl"
model = joblib.load(model_filename)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
threshold = 0.2

@app.route('/predict', methods=['POST'])
def predict():
    print("📥 Received request at /predict")

    if 'image' not in request.files:
        print("🚫 No image found in request")
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        print("🚫 Empty filename received")
        return jsonify({'error': 'Empty filename'}), 400

    try:
        npimg = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)

        if image is None:
            print("❌ Image decoding failed.")
            return jsonify({'error': 'Invalid image'}), 400

        print("✅ Image received and decoded.")

        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY if image.shape[2] == 4 else cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            face_img = gray[y:y+h, x:x+w]
            print("😎 Face detected.")
        else:
            face_img = gray
            print("😐 No face detected, using full image.")

        IMG_SIZE = 100  # Ensure this is consistent with your training data
        face_img_resized = cv2.resize(face_img, (IMG_SIZE, IMG_SIZE))

        # Optional: Normalize pixel values (if model was trained on normalized data)
        face_img_resized = face_img_resized / 255.0  # Adjust this depending on how your model was trained

        face_img_flat = face_img_resized.flatten().reshape(1, -1)

        # Debugging: Print the shape of the flattened image
        print(f"Image shape after flattening: {face_img_flat.shape}")

        # Check probabilities and predictions
        probs = model.predict_proba(face_img_flat)
        print(f"Prediction probabilities: {probs}")

        max_prob = np.max(probs)
        predicted_label = model.predict(face_img_flat)[0]

        print(f"✅ Prediction complete. Label: {predicted_label}, Confidence: {max_prob:.2f}")

        if max_prob >= threshold:
            result = f"Subject {predicted_label}"
        else:
            result = "Unknown"

        return jsonify({
            'result': result,
            'confidence': float(max_prob),
            'label': int(predicted_label)
        })

    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

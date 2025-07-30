import cv2

# Load Haar cascades for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Load image
img = cv2.imread("face1.jpg")
if img is None:
    print("Error: face1.jpg not found in the folder.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

# Predict emotion (happy if smile detected, else neutral)
emotion = "neutral"
for (x, y, w, h) in faces:
    roi_gray = gray[y:y + h, x:x + w]
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
    if len(smiles) > 0:
        emotion = "happy"
    break  # check only the first face detected

# Show result
print("Predicted emotion:", emotion)

# Save output to file
with open("task2_output.txt", "w") as f:
    f.write(f"Predicted emotion: {emotion}")

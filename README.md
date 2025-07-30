# Codeclause-task2
Artificial intelligence 

Facial Emotion Detection Using OpenCV

This project detects human emotions (happy or neutral) from images using Python's OpenCV Haar Cascades.


---

How it works

1. The program loads a face image (e.g., face1.jpg).


2. It detects the face using a Haar cascade classifier.


3. If a smile is detected inside the face region, it predicts happy, otherwise neutral.


4. The detected emotion is displayed on the console and saved to task2_output.txt.




---

Requirements

Python 3 (works on Pydroid3 or PC)

Install the required library:

pip install opencv-python



---

Steps to Run

1. Place your image file (e.g., face1.jpg) in the same folder as the script.


2. Run the script:

python task2_emotion.py


3. The detected emotion will be shown in the console and saved in task2_output.txt.




---

Example Output

Image Content:

> A smiling face photo



Console Output:

Predicted emotion: happy

task2_output.txt:

Predicted emotion: happy

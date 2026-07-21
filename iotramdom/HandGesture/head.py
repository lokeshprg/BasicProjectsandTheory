import cv2
from pyfirmata2 import Arduino, SERVO
import time

board = Arduino('COM7')
servo_pin = 9
time.sleep(2)

board.digital[servo_pin].mode = SERVO

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(80, 80))
    height, width = frame.shape[:2]
    for x, y, w, h in faces:
        center_x = x+w//2
        angle=int((center_x/width*180))
        angle = max(0, min(180, angle))
        board.digital[servo_pin].write(angle)

        cv2.rectangle(frame, (x, y), (x+w, y+h),(255, 0, 0), 2)
        cv2.putText(frame, f"Angle:{angle}", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),2)

    cv2.imshow("Face tracking Servo", frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
board.exit()
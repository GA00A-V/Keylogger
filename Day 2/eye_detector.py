import cv2

cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 15)
    if eyes is not None:
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 2)

    cv2.imshow("Eye Detector", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

import cv2

# teste
frameWidth = 640
frameHeight = 480
# Webcam, Mobile Cam in others
cap = cv2.VideoCapture('rtsp://teste:1892893894ZFZ@192.168.12.228:2808/cam/realmonitor?channel=17&subtype=0')
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


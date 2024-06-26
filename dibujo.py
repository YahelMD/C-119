import cv2
import time
import math


vid = cv2.VideoCapture("ovni.mp4")
tracker = cv2.TrackerCSRT_create()
returned, img = vid.read()
box = cv2.selectROI("tracking", img, False)
tracker.init(img,box)
print (box)
def drawBox(img, box) :
     x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
     cv2.rectangle(img, (x, y), ((x + w), (y + h)), (132, 5, 205), 3)
     cv2.putText(img, "Rastreando...", (60, 302), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 32, 143), 2)
while True:
     ckeck, img = vid.read()
     success, box=tracker.update(img)
     if success:
          drawBox(img, box)
     else:
          cv2.putText(img, "PERDIDO", (60, 302), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (34, 19, 241), 2)
     cv2.imshow("Resultado", img)
     key=cv2.waitKey(25)
     if key == 32:
          cv2.putText(img, "Terminó así bien épico", (60, 302), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (41, 132, 76), 2)
vid.release()
cv2.destroyAllWindows

    

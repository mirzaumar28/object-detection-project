import os 
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"



labels = ['Hello', 'Yes', 'No', 'Thanks', 'I Love You', 'Please'] 

NUM_OF_IMG = 100

cap = cv2.VideoCapture(0)
for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    print(f"Collecting Images for {label}")
    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < NUM_OF_IMG:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        img_name = os.path.join(IMAGE_PATH, label, label + '.' +'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(img_name, frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
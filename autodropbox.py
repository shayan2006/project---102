import cv2

def take_snapshot():
    videocaptureobject = cv2.VideoCapture(0)
    result = True

    while(result):
        try:
            ret,frame = videocaptureobject.read()
            cv2.imwrite("project-102/newpicture1.jpg", frame)
            result= False

        except:
            pass   
    videocaptureobject.release()
    cv2.destroyAllWindows()

take_snapshot()
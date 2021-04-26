import cv2

vidcap =  cv2.VideoCapture("D:\\sura baqarah\\Sura Baqarah ayat 21 by Nouman Ali Khan.mp4")
ret, image = vidcap.read()
count = 0
while True:
    if ret == True:
        cv2.imwrite("D:\\frames\\imgN%d.jpg"%count, image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count**100))
        ret, image = vidcap.read()
        cv2.imshow("res", image)

        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            cv2.destroyAllWindows()

vidcap.release()
cv2.destroyAllWindows()
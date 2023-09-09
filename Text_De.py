import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread("img2.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(800,400))


#cong = r'--oem 3 --psm 6 outputbase digits'
#boxesNu =pytesseract.image_to_boxes(img,config=cong)
#for n in boxesNu.splitlines():
    #n = n.split(" ")
    #print(n)
    #x, y, w, h = int(n[1]), int(n[2]), int(n[3]), int(n[4])
    #cv2.rectangle(img, (x,y), (w, h), (0, 0, 255), 4)
    #cv2.putText(img , n[0],(x,y+60),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

boxes =pytesseract.image_to_data(img)
#print(boxes [0:30])
for b,n in enumerate(boxes.splitlines()):
    if b!=0 :
        n = n.split()
        if len(n) ==  12:
            x, y, w, h = int(n[6]), int(n[7]), int(n[8]), int(n[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0, 0, 255), 4)
            cv2.putText(img , n[11],(x,y+60),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

cv2.imshow("Result" , img)
cv2.waitKey(0)
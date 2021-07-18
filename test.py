import face_recognition    #original
import cv2
import os
known_faces_dir=os.listdir('Images')
knownEncodings=[]
knownNames=[]
a=0
print("Encoding Started")
for name in known_faces_dir:
    for filename in os.listdir(f"Images/{name}"):
         image=face_recognition.load_image_file(f"Images/{name}/{filename}")
         rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
         encodings=face_recognition.face_encodings(rgb)
         for encoding in encodings:
             knownEncodings.append(encoding)
             knownNames.append(name)
         a+=1
         print(a)
print("Encoding over")     
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt2.xml')
video=cv2.VideoCapture(0)
res=[]
print("Streaming Started")
while True:
    ret,frame=video.read()
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    encodings=face_recognition.face_encodings(rgb)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(60,60),flags=cv2.CASCADE_SCALE_IMAGE)
    for encoding in encodings:
      res=face_recognition.compare_faces(knownEncodings,encoding)
    if True in res:
         index=res.index(True)
         name=knownNames[index]
         print("match found")
    else:
         print("match not found")
         name="unknown"    
    key=cv2.waitKey(1)
    
    for(x,y,h,w) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
         cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (255, 0, 0), 2)
    
    if key==ord('q'):
        break
    cv2.imshow("Frame",frame)

cv2.destroyAllWindows()
video.release()

#import os
#knownimage=face_recognition.load_image_file('./Images/DONya KAKA/trump1.jpg')

#known_face_encodings=face_recognition.face_encodings(knownimage)
#unknownimages=face_recognition.load_image_file('./Images/DONya KAKA/trump2.jpg')
#unknown_face_encodings=face_recognition.face_encodings(unknownimages)
#results=face_recognition.compare_faces([known_face_encodings],unknown_face_encodings)
#if results[0]:
    #print('this is trump')  
#else:
    #print("not trump")    

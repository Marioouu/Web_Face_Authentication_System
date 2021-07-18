from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages
from django.contrib.messages import constants
import face_recognition
import base64
import cv2
import io
import os
import numpy as np

import json
from .models import UserProfile
from django.contrib import messages

# Create your views here.
def index(request):
     print(request.user)
     if request.user.is_anonymous:
          return redirect("/loginUser")
     print("success")
     return render(request,'index.html')

def loginUser(request):
     print("req reached login")
     print(request.method)
     
     if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password')
          input_face=request.POST.get('input_face')
          user = authenticate(username=username, password=password)
          print(user)


          if user is not None:
               knownface = np.array(json.loads(user.user_profile.face_data))
               image=face_recognition.load_image_file(io.BytesIO(base64.b64decode(input_face)))
               image_encoding=face_recognition.face_encodings(image)

               match=face_detect(image_encoding,knownface)
               if match:
                    login(request,user)
                    print("MATCED")                         
                    return redirect("/")
               else:
                    print("Face not Matched")                     
                    messages.error(request, 'Faces do not match!', extra_tags='danger')
                    return redirect("/loginUser")
     
          else:
               print("NOT MATCCHED")               
               return render(request,'login.html')
          
          
           
        

     return render(request,'login.html')

def logoutUser(request):
     logout(request)
     #return HttpResponse("Services are: cone 50") 
     return redirect("/loginUser")





def face_detect(reference, to_check):

     print("Comparing With DataBAse")
     #print(reference, to_check)
     matches = face_recognition.compare_faces(np.array(reference),[np.array(to_check)])    
     print("Input face Encoding")
     print(np.array(reference))
     print("Known User Encodings")
     print([np.array(to_check)])
     name = "Unknown"
     if True in matches:
         print("Match Found")
         return True    
     else:
         return False


def signupUser(request):
     print("req reached Signup")
     print(request.method)
     #return HttpResponse("712-712-712")
     if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password')
          input_face=request.POST.get('input_face')

          #input_encodings=get_face_encoding_from_base64(input_face)

          #match=face_detect(input_encodings)
         

          #print(username,password)
          #print(input_face)
          image=face_recognition.load_image_file(io.BytesIO(base64.b64decode(input_face)))
          image_encoding=face_recognition.face_encodings(image)
          encoding=image_encoding[0]
          if(len(image_encoding)!=0):
               encoding = json.dumps(encoding.tolist())
               user = User.objects.create_user(username = username, password = password)
               UserProfile.objects.create(user = user, face_data = encoding)
               messages.success(request, 'Profile created succesfully!')
               print("PROfile Created Succesfully")
               return redirect("/loginUser")
          else:
               messages.error(request, 'ERROR NO face Detected', extra_tags='danger')

          

     return render(request,'signup.html')



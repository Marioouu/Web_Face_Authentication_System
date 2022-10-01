# Face-attendance System

<br/>
<br/>

<p align="center">
  <a href="https://face-attendance935.herokuapp.com/">
    <img src="https://avatars.githubusercontent.com/u/57796181?s=200&v=4" alt="Logo" width="150">
  </a>
</p>

<br/>
<br/>

**Demo** : [Click here](https://face-attendance935.herokuapp.com/)<br/>
**PPT** : [Click here](https://docs.google.com/presentation/d/1ohDVjODKT071X2a1MdO18IM3xQzfvrrgfWj-DLpfOlk/edit?usp=sharing)

<!-- ABOUT THE PROJECT -->
## **About The Project**
This project aims to provide a valuable attendance service for both teachers and students. Reduce manual process errors by provide automated and a reliable attendance system uses face recognition technology.

It involves building an attendance system which utilizes facial recognition to mark the presence of the students. It covers areas such as face detection, alignment, visibility, and web application that provides user interface to use this functionality.




<br/>
<br/>



"# Face_Login_Authentication_System" 

                                             # WHAT IS FACE RECOGNITION?




Face recognition is a technology capable of identifying or verifying a subject through an image, video or any audiovisual element of his face. Generally, this identification is used to access an application, system or service.

It is a method of biometric identification that uses that body measures, in this case face and head, to verify the identity of a person through its facial biometric pattern and data. The technology collects a set of unique biometric data of each person associated with their face and facial expression to identify, verify and/or authenticate a person.



                                              # FACE RECOGNITION SYSTEM
                                                                  
The face recognition procedure simply requires any device that has digital photographic technology to generate and obtain the images and data necessary to create and record the biometric facial pattern of the person that needs to be identified.

Unlike other identification solutions such as passwords, verification by email, selfies or images, or fingerprint identification, Biometric facial recognition uses unique mathematical and dynamic patterns that make this system one of the safest and most effective ones.

The objective of face recognition is, from the incoming image, to find a series of data of the same face in a set of training images in a database. The great difficulty is ensuring that this process is carried out in real-time, something that is not available to all biometric facial recognition software providers.

The facial recognition process can perform two variants depending on when it is performed:

The one in which, for the first time, a facial recognition system addresses a face to register it and associate it with an identity, in such a way that it is recorded in the system. This process is also known as digital onboarding with facial recognition.
The variant in which the user is authenticated, prior to being registered. In this process, the incoming data from the camera is crossed with the existing data in the database. If the face matches an already registered identity, the user is granted access to the system with his credentials.
Schedule an appointment here and access 508 million users thanks to the European standardization of customer onboarding.

                                                                 
                                     # HOW DOES FACE RECOGNITION WORK?
Face recognition systems work by capturing an incoming image from a camera device in a two-dimensional way.

These ones compare the relevant information of the incoming image signal in real-time in photo in a Django database, being much more reliable and secure than the information obtained in a static image. This biometric facial recognition procedure requires an internet connection since the database cannot be located on the capture device as it is hosted on servers.

In this comparison of faces, it analyses mathematically the incoming image without any margin of error and it verifies that the biometric data matches the person who must use the service or is requesting access to an application, system or even building. 

Thanks to the use of artificial intelligence (AI) and machine learning technologies, face recognition(face_recognition.lib) systems can operate with the highest safety and reliability standards. Similarly, thanks to the integration of these algorithms and computing techniques, the process can be carried out in real-time.


## **Screenshots**
<div align="center" ><br/>
Start with Registering the student on portal<br/><hr width=600/>
  <img src="./images/register.png" width=600 ><br/><br/>
After registrartion student can mark the attendence<br/><hr width=600/>
  <img src="./images/login.png" width=600 ><br/><br/>
Generating the attendence sheet<br/><hr width=600/>
  <img src="./images/list.png" width=600><br/>
</div>
<br/>



### **Tech Stack used**

* [Django](https://www.djangoproject.com/)
* [Python](https://www.python.org/)
* [Face-Recognition](https://github.com/ageitgey/face_recognition)
* [HTML & CSS]()
* [JavaScript](https://www.javascript.com/)

<br/>


### **Installation**
Anaconda must be installed on your system if running locally.

1. Clone the repo
   ```sh
   git clone https://github.com/ayushyadav9/face-attendance.git
   ```

2. Create a Python Virtual Environment
   ```sh
   conda create -n yourenvname
   ```
3. Activate the Virtual Environment
   ```sh
   conda activate yourenvname
   ```
4. Install the packages in requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
5. After migrations run the server
   ```sh
   python manage.py runserver
   ```

<br/>

<!-- ROADMAP -->
## Roadmap
1) Adding functionality of registering students with admin face authentication
2) Integrating advanced Deep learning model that only recognizes 3-D faces. Currently the model recognizes 2-D faces also.
3) Generating an excel sheet of attendence list.


<br/>

<!-- CONTRIBUTING -->
### **Contributing**

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
   
<br/>

<!-- ACKNOWLEDGEMENTS -->
### **Acknowledgements**

* [Bootstrap](https://getbootstrap.com)
* [Heroku](https://heroku.com)

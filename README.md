# python-app-with-electron-gui
A better way to make GUIs for your Python apps
Use HTML, JavaScript and CSS to make highly customized, cross platfrom desktop apps which use native Python backends.
https://youtu.be/627VBkAhKTc

<img src="/samples/1.png" width="500" height="900" />

![Alt Text](/samples/2.png)
![Alt Text](/samples/3.png)



Note: This is for educational purposes only, this may not be efficient or bug-free. Code is optimised for Python 2.

## General Dependenices
  * Python
  * NodeJS
  * electron.js
  * python-shell
 
## Specific Dependencies
  * weather module:
    * requests
    * RapidConnect
  
  * face recognition module
    * dlib
    * openCV
    * numpy
    * face_recognition
   
  * object detection module
    * Flask
    * tensorflow
    * keras
    * scipy
    
    ## Usage
    * Make sure you have `electron.js` - download it by typing `npm install electron -g`. This is will install Electron.js and set up your PATH.
    * You can now run `npm start` inside the `gui/` directory.
    * If you want to use the object detection module, make sure the flask server [object_detection.py] is up and running before starting the GUI.
    
    ## Known issues
    * To use the object detection module, the image you want to use must be in the `engine` folder.
   
   
  

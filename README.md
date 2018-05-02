# python-app-with-electron-gui
A better way to make GUIs for your Python apps


Use HTML, JavaScript and CSS to make highly customized, cross platfrom desktop apps which use native Python backends.


https://youtu.be/84_LfKDLXF4

Note: This is for educational purposes only, this may not be efficient or bug-free. Code is optimised for Python 2.

## General Dependenices
  * Python
  * NodeJS
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
    * Inside the `gui` directory, and then run `npm install && npm start`
    * If you're in the `engine` directory, run `./boot.sh`
    
## Known issues
    * To use the object detection module, the image you want to use must be in the `engine` folder. Also, you have to run the app
    from inside the `engine` directory. See usage instructions.
   
   
  

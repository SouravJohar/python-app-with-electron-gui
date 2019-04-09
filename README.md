# python-app-with-electron-gui
A better way to make GUIs for your Python apps
Use HTML, JavaScript and CSS to make highly customized, cross platfrom desktop apps which use native Python backends.

https://youtu.be/627VBkAhKTc

<img src="/samples/1.png" width="50%" />
<img src="/samples/3.png" width="50%" />




Note: This is for educational purposes only, this may not be efficient or bug-free. Also, this is just a demo on how
JS and Python can be used to interact together. This demo is *NOT* meant to show face detection or object detection.

## General Dependenices
  * Python
  * NodeJS
  * electron.js
  * python-shell
 
## Specific Dependencies
  * weather module:
    * requests
    * beautifulsoup4
   
  * object detection module
    * Flask
    * tensorflow
    * keras
    
    ## Usage
    * Clone the repo, and then
	```sh
	$ cd electron-app-with-python-gui
	$ pip install -r requirements.txt
	$ npm install
	$ npm start
	```
    * If you want to use the object detection module, make sure the flask server [object_detection.py] is up and running before starting the GUI.
	```sh
	$ cd engine
	$ python object_detection.py
	```

## Note:

weather_engine.py uses web-scraping to pull data off the internet, from a particular website. If this site happens to be modified
or changed in the future, the code *might* break. However, this can be fixed by analyzing the new layout of the site and adjusting
the python code accordingly.

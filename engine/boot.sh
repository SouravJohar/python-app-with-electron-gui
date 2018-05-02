kill -9 $(lsof -t -i:5000)
echo killed pre
python object_detection.py &
cd ..
cd gui
npm start
kill -9 $(lsof -t -i:5000)
echo killed

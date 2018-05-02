import face_recognition as f
import cv2
import _pickle as c
import os


def display(loc, dpname):
    top, right, bottom, left = loc
    cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 0, 255), 2)
    cv2.rectangle(frame, (left * 4, bottom * 4 - 35),
                  (right * 4, bottom * 4), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, dpname, (left * 4 + 6, bottom * 4 - 6), font, 1.0, (255, 255, 255), 1)


print ("loading face database")
faces = {}
for face in os.listdir("faces/"):
    if not face.startswith("."):
        with open("faces/" + face, 'rb') as fp:
            face_info = c.load(fp)
            faces[face] = {}
            faces[face]["info"] = face_info
            faces[face]["name"] = face

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    sframe = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    sframe = sframe[:, :, ::-1]
    face_locations = f.face_locations(sframe)
    for loc in face_locations:
        dpname = ""
        face_enc = f.face_encodings(sframe, [loc])[0]
        for face in faces:
            match = f.compare_faces([faces[face]["info"]], face_enc, tolerance=0.5)
            if match[0]:
                dpname = faces[face]["name"]
                break
        display(loc, dpname)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

import face_recognition as f
import cv2
import sys
import _pickle as c

'''
command line args: imgfile, name_of_person_in_image
'''

# todo display faces while enc
s, img, name = sys.argv
if img != "cam":
    img_array = f.load_image_file(img)
    face_enc = f.face_encodings(img_array)[0]
    with open("faces/" + name, 'wb') as fp:
        c.dump(face_enc, fp)
    print ("Done")

if img == "cam":
    cam = cv2.VideoCapture(0)
    while True:
        _, img_array = cam.read()
        cv2.imshow("Press 'a' to add your face", img_array)
        k = cv2.waitKey(10)
        if k == ord('a'):
            face_enc = f.face_encodings(img_array)[0]
            with open("faces/" + name, 'wb') as fp:
                c.dump(face_enc, fp)
            break
    print ("Done")
    cam.release()
    cv2.destroyAllWindows()

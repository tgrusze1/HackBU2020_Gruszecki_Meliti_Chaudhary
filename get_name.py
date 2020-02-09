import face_recognition
import cv2

def get_name():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        cap.open()

    ret, frame = cap.read()
    cap.release()

    tdogg_image = face_recognition.load_image_file("tdogg.jpg")
    tdogg_enc = face_recognition.face_encodings(tdogg_image)[0]

    known_face_enc = [
        tdogg_enc
    ]
    known_face = [
        "T-Dogg"
    ]

    rgb_frame = frame[:, :, ::-1]
    face_loc = face_recognition.face_locations(rgb_frame)
    face_enc = face_recognition.face_encodings(rgb_frame, face_loc)

    matches = None
    for (top, right, bottom, left), enc in zip(face_loc, face_enc):
        matches = face_recognition.compare_faces(known_face_enc, enc)

    name = "Unknown"
    if matches != None and True in matches:
        name = known_face[matches.index(True)]

    print(name)
    return name
get_name()

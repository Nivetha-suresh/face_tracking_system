import cv2

genderProto = "models/gender_deploy.prototxt"
genderModel = "models/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

genderList = ['Male', 'Female']

genderNet = cv2.dnn.readNet(genderModel, genderProto)

def detect_gender(frame, face):
    x1, y1, x2, y2 = face

    face_img = frame[max(0, y1):min(y2, frame.shape[0]),
                     max(0, x1):min(x2, frame.shape[1])]

    if face_img.size == 0:
        return "Unknown"

    blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227),
                                 MODEL_MEAN_VALUES, swapRB=False)

    genderNet.setInput(blob)
    prediction = genderNet.forward()

    return genderList[prediction[0].argmax()]
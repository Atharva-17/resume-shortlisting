import cv2

def plotSkills(image , imageOut , skills):
    image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    n_boxes = len(imageOut['text'])
    for i in range(n_boxes):
        if  (imageOut['text'][i].upper()) in skills:
            (x, y, w, h) = (imageOut['left'][i], imageOut['top'][i], imageOut['width'][i], imageOut['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

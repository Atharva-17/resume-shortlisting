import cv2

def plotSkills(image1 , imageOut , skills):
    image1 = cv2.cvtColor(image1 , cv2.COLOR_BGR2RGB)
    image1 = cv2.resize(image1, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    n_boxes = len(imageOut['text'])
    for i in range(n_boxes):
        test_str = imageOut['text'][i]
        #test_str = test_str.translate(str.maketrans('', '', string.punctuation))
        for skill in skills:
          #print(test_str , " " , )
          if test_str.lower().find(skill) != -1:
            #print(test_str)
            (x, y, w, h) = (imageOut['left'][i], imageOut['top'][i], imageOut['width'][i], imageOut['height'][i])
            image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image1

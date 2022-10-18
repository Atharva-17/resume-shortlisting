import cv2

def plotSkills(image1 , imageOut , skills):
    # image1 = cv2.cvtColor(image1 , cv2.COLOR_BGR2RGB)
    # image1 = cv2.resize(image1, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    n_boxes = len(imageOut['text'])
    for i in range(n_boxes):
        test_str = imageOut['text'][i]
        #test_str = test_str.translate(str.maketrans('', '', string.punctuation))
        for skill in skills:
          #print(test_str , " " , )
          if test_str is not None and test_str.lower().find(skill) != -1:
            #print(test_str)
            (x, y, w, h) = (imageOut['left'][i], imageOut['top'][i], imageOut['width'][i], imageOut['height'][i])
            image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image1

def plotName(image1 , imageOut , name):
    
    n_boxes = len(imageOut['text'])
    for i in range(n_boxes):
        test_str = imageOut['text'][i]
        #test_str = test_str.translate(str.maketrans('', '', string.punctuation))
        #print(test_str , " " , )
        if test_str is not None and test_str.lower().find(name) != -1:
          #print(test_str)
          (x, y, w, h) = (imageOut['left'][i], imageOut['top'][i], imageOut['width'][i], imageOut['height'][i])
          image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 255), 2)
    return image1

def plotNumber(image1 , imageOut , number):
    n_boxes = len(imageOut['text'])
    for i in range(n_boxes):
        test_str = imageOut['text'][i]
        #test_str = test_str.translate(str.maketrans('', '', string.punctuation))
        #print(test_str , " " , )
        if test_str is not None and number is not None and test_str.lower().find(number) != -1:
          #print(test_str)
          (x, y, w, h) = (imageOut['left'][i], imageOut['top'][i], imageOut['width'][i], imageOut['height'][i])
          image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 100), 2)
    return image1


def plotEmail(image1 , imageOut , email):
    
    n_boxes = len(imageOut['text'])
    for i in range(n_boxes):
        test_str = imageOut['text'][i]
        #test_str = test_str.translate(str.maketrans('', '', string.punctuation))
        #print(test_str , " " , )
        if email is not None and test_str.lower().find(email) != -1:
          #print(test_str)
          (x, y, w, h) = (imageOut['left'][i], imageOut['top'][i], imageOut['width'][i], imageOut['height'][i])
          image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 100, 255), 2)
    return image1

def plotAll(image1 , imageOut , skills , email , phone):
  image1 = cv2.cvtColor(image1 , cv2.COLOR_BGR2RGB)
  image1 = cv2.resize(image1, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
  image1 = plotEmail(image1 , imageOut , email)
  #image1 = plotName(image1 , imageOut , name)
  image1 = plotNumber(image1 , imageOut , phone)
  image1 = plotSkills(image1 , imageOut , skills)
  return image1


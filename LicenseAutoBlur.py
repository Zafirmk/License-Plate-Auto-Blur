import numpy as np
import matplotlib.pyplot as plt
import cv2

#Load the license cascade
license_cascade = cv2.CascadeClassifier("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/cv2/data/haarcascade_russian_plate_number.xml")

#Function that detects and blurs license plate
def detect_license(img):

    #Store copy of the image in color and B&W to manipulate
    img_copy = img.copy()
    img_BW = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    #Returns coordinates of the located license plate
    license_rect = license_cascade.detectMultiScale(img_BW, scaleFactor=1.3, minNeighbors=5)

    #Isolate ROI, blur and reapply onto original image
    for (x,y,w,h) in license_rect:
        license_ROI = img_copy[y:y+h, x:x+w]
        license_ROI = cv2.blur(license_ROI,(30,30))
        img_copy[y:y+h, x:x+w] = license_ROI
    
    return img_copy


#Loop over all 15 sample images, blur them and display results
for i in range(1,16):
    img = cv2.imread("/Users/zafirkhalid/Desktop/Projects/license"+str(i)+".jpg")

    result_blur = detect_license(img)
    result_blur = cv2.cvtColor(result_blur, cv2.COLOR_BGR2RGB)

    plt.imshow(result_blur, aspect="auto")
    plt.show()
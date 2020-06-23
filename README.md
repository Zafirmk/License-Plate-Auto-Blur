# License-Plate-Auto-Blur

![Working Gif](https://github.com/Zafirmk/License-Plate-Auto-Blur/blob/master/WorkingGIF.gif)  

**Project duration**: <5 hours   
**IDE**: VS Code (Community Edition)  
**Python Version**: Python 3.8


## Description
Takes in input image files that include one or many license plates. All license plates are located in the image and automatically blurred.

## Image Files Used  
* **license(i)**: (Where i is from 1 to 15) sample images taken from dash cam stills.

## How it works
1. License plates are first identified using OpenCV's Russian license plate number cascade.  

2. Once found, the ROI (reigon of interest) is isolated from the image and blurred

3. Blurred reigon is then pasted back onto the original image and displayed 

## Getting Started

1. Clone this repo using the following command  
```
$ git clone https://github.com/Zafirmk/License-Plate-Auto-Blur.git
$ cd License-Plate-Auto-Blur
```
2. Open the project in your preferred IDE  

3. Set the directory of the project to where the repo is saved. Or simply edit the following lines of code to read
```
img = cv2.imread("<YOUR PATH HERE>"+str(i)+".jpg")
```

### Prerequisites
Things you need to install before running:
*  [Python](https://www.python.org/)
*  [OpenCV](https://opencv.org/)
*  [Matplotlib](https://matplotlib.org/)
*  [Numpy](https://numpy.org/)

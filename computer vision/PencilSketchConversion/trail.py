import cv2 as cv 




img_path = r"C:\Users\v.rajkumar\Pictures\yolo\IMG-20241025-WA0005.jpg"

img = cv.imread(img_path)
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img_inverted = cv.bitwise_not(img_gray)
blured_img = cv.GaussianBlur(img_inverted,(21,21),sigmaX=0,sigmaY=0)
img_inverted = cv.bitwise_not(blured_img)
sketch_img = cv.divide(img_gray,img_inverted,scale=256.0)
cv.imshow("img",sketch_img)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import pytesseract 

img = cv.imread("0.jpg")


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]

text = pytesseract.image_to_string(thresh)

print(text)

cv.imshow("img",thresh)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np 
import cv2 as cv 
from PIL import Image 
import matplotlib.pyplot as plt




def colorizer(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
    
    prototxt = r"C:\Users\v.rajkumar\AppData\Local\Programs\Python\Python37\3 MONTH INTERNSHIP\Ai2025\Computer Vision\Image_Colorization\models\colorization_deploy_v2.prototxt"
    model = r"C:\Users\v.rajkumar\AppData\Local\Programs\Python\Python37\3 MONTH INTERNSHIP\Ai2025\Computer Vision\Image_Colorization\models\colorization_release_v2.caffemodel"
    hull_points = r"C:\Users\v.rajkumar\AppData\Local\Programs\Python\Python37\3 MONTH INTERNSHIP\Ai2025\Computer Vision\Image_Colorization\models\pts_in_hull.npy"    
    
    net = cv.dnn.readNetFromCaffe(prototxt=prototxt,caffeModel=model)
    
    class_8  = net.getLayerId("class8_ab")
    conv8   = net.getLayerId("conv8_313_rh")
    
    pts = np.load(hull_points)
    
    pts = pts.transpose().reshape(2,313,1,1)
    
    net.getLayer(class_8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1,313],2.606,dtype="float32")]
    
    scaled =  img.astype("float32") / 255.0
    
    lab = cv.cvtColor(scaled, cv.COLOR_RGB2LAB)
    
    resized = cv.resize(lab,(224,224))
    L = cv.split(resized)[0]
    L -= 50
    
    net.setInput(cv.dnn.blobFromImage(L))
    
    ab = net.forward()[0,:,:,:].transpose((1,2,0))
    ab = cv.resize(ab,(img.shape[1],img.shape[0]))
    
    L = cv.split(lab)[0]
    
    colorized = np.concatenate((L[:,:,np.newaxis],ab),axis=2)
    
    colorized = cv.cvtColor(colorized, cv.COLOR_LAB2RGB)
    colorized = np.clip(colorized, 0, 1)
    
    colorized = (255 * colorized).astype("uint8")
   
    print("predicted")
    return colorized
     
    
    
    
img_path = "1.jpg"

img = cv.imread(img_path)
plt.imshow(img)
plt.show()
c_img = colorizer(img=img)

plt.imshow(c_img)

plt.axis("off")
plt.show()
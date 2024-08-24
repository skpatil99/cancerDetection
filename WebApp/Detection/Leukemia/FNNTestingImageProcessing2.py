import glob
def imageProcessing(path):
    for imgName in glob.glob("/home/sanket/Desktop/WebApp/Detection/media/"+str(path)):
        #Read the Image
        import cv2
        import imageio
        image = cv2.imread(imgName,1)
        image = cv2.resize(image,(500,500))

        #To store of Area initialize the list and to store the number of defected cell initilize linesnum
        AreaSeparation = []

        #Remove Noise
        from skimage import img_as_float
        from skimage.filters import gaussian
        unsharp_strength = 0.8
        blurr_size = 8

        image = img_as_float(image)
        noise = gaussian(image,blurr_size)
        highpass = image - unsharp_strength * noise
        sharp = image + highpass

        imageio.imwrite('/home/sanket/Desktop/WebApp/Detection/Leukemia/templates/sharp.jpg',sharp)
        #Convert the image from RGB to grey color space
        from skimage import color

        grey = color.rgb2grey(sharp)

        #Contrast Strectching of  image
        from skimage.exposure import rescale_intensity
        import numpy as np

        p1,p2 = np.percentile(grey,(2,98))
        contrast = rescale_intensity(grey,in_range=(p1,p2))

        #Histogram Equilization of Image
        from skimage.exposure import equalize_hist

        hist_eq = equalize_hist(contrast)

        #Adaptive Equalization Histogram
        from skimage.exposure import equalize_adapthist

        hist_adapteq = equalize_adapthist(hist_eq, clip_limit=0.03)

        #Addition of hist_eq and contrast
        Add = hist_eq + contrast

        #Substraction of hist_eq and contrast
        Subs = contrast - hist_eq

        #Addition of Add and Subs
        newImage = Add + Subs

        #Otsu Threshold
        import numpy as np

        newImage = newImage.astype(np.uint8)
        threshold = cv2.threshold(newImage,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        threshold = threshold.astype(np.float)

        #Remove small Dot present in image
        from skimage.morphology import closing
        from skimage.morphology import square

        closing = closing(threshold,square(3))

        #Edge Detection Sobel
        from skimage.filters import sobel

        sobel = sobel(closing)

        #Checking for Python3 or Python2 for simplicity
        import imutils

        labels_ws = np.uint8(sobel)
        MIN_THRESH = 100
        if imutils.is_cv2():
            (cnts, _) = cv2.findContours(labels_ws, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        elif imutils.is_cv3():
	        (_, cnts, _) = cv2.findContours(labels_ws, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print("COUNT: " ,len(cnts))


        #Features Extraction
        from skimage.feature import greycomatrix
        from skimage.feature import greycoprops
        from skimage import img_as_ubyte
        from skimage import color
        import math

        PI = 3.14
        cell_count=0

        import csv
        with open('/home/sanket/Desktop/WebApp/Detection/Leukemia/2CheckFeatures.csv','w') as csvfile:
            for c in cnts:
                if cv2.contourArea(c) > MIN_THRESH:
                    M = cv2.moments(c)

                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])

                    area = cv2.contourArea(c)

                    perimeter = cv2.arcLength(c,True)

                    x,y,w,h = cv2.boundingRect(c)
                    aspect_ratio = float(w)/h

                    rect_area = w*h
                    extent=float(area)/rect_area

                    hull = cv2.convexHull(c)
                    hull_area=cv2.contourArea(hull)

                    solidity=float(area)/hull_area

                    equi_diameter = np.sqrt(4*area/np.pi)

                    (x,y),(MA,ma),(angle) = cv2.fitEllipse(c)

                    bounding_box=cv2.boundingRect(c)

                    compactness = (perimeter**2)/area

                    formfactor = 4*PI*area/(perimeter**2)

                    a= MA/2
                    b= ma/2
                    eccentricity = math.sqrt(abs((math.pow(a,2) - math.pow(b,2))/math.pow(a,2)))

                    elongation = MA/ma

                    mean = np.mean(c)

                    std = np.std(c)

                    #Adding the Features into CSV File
                    fieldnames = ['Area','Perimeter','AspectRatio','Extent','Compactness','FormFactor','Angle','Eccentricity','Elongation','Mean','Std','HullArea','Solidity','EquiDiameter']
                    writer1 = csv.DictWriter(csvfile,fieldnames = fieldnames)
                    writer1.writerow({'Area':area,'Perimeter':perimeter,'AspectRatio':aspect_ratio,'Extent':extent,'Compactness':compactness,'FormFactor':formfactor,'Angle':angle,'Eccentricity':eccentricity,'Elongation':elongation,'Mean':mean,'Std':std,'HullArea':hull_area,'Solidity':solidity,'EquiDiameter':equi_diameter})



    cv2.waitKey(0)

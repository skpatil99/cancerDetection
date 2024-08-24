import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
def KNN():
    np.random.seed(7)

    #training Dataset
    dataset = np.loadtxt("/home/sanket/Desktop/WebApp/Detection/Leukemia/2CheckFeatures.csv" ,dtype = float , delimiter =',').astype(np.float32)
    #testing Dataset
    #Testing = np.loadtxt("TestingFeatures.csv" ,dtype = float , delimiter =',').astype(np.float32)

    X = dataset[:,0:14]

    #TX = Testing[:,0:14]
    #TY = Testing[:,14]

    # load the model from disk
    loaded_model = pickle.load(open('/home/sanket/Desktop/WebApp/Detection/Leukemia/KNN_model.sav', 'rb'))

    predicted = loaded_model.predict(X)

    #print prediction
    preds = predicted.tolist()
    c = preds.count(1)



    if (c >(len(preds)*0.94)):
	    return "Cancerous"
    else:
	    return "Non-Cancerous"

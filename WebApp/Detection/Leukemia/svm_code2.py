import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pickle

def SVM():
    data = np.loadtxt('/home/sanket/Desktop/WebApp/Detection/Leukemia/2CheckFeatures.csv', dtype = float, delimiter=',').astype(np.float32)
    d = data.shape
    #input to the model
    if len(d)==1:
	    test_x = data.reshape(1, -1)
    else:
	    test_x = data[:,:]

    print test_x.shape
    # load the model from disk
    loaded_model = pickle.load(open('/home/sanket/Desktop/WebApp/Detection/Leukemia/final_model.sav', 'rb'))
    prediction = loaded_model.predict(test_x)
    #print prediction
    preds = prediction.tolist()
    c = preds.count(1)

    if (c >(len(preds)*0.9)):
	    return "Cancerous"
    else:
	    return "Non-Cancerous"

#Seeding Value
import numpy as np
from keras import backend as K

def FNN():
    np.random.seed(7)

    #Load the Training Dataset
    test_dataset = np.loadtxt("/home/sanket/Desktop/WebApp/Detection/Leukemia/2CheckFeatures.csv", dtype=float, delimiter=',').astype(np.float32)

    #Separate the training data into features and label(train_X->Features,train_Y->label)
    test_X = test_dataset[:,0:14]

    #Create the Neural Network Sequential Model
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import Dropout
    from keras.constraints import maxnorm
    from keras.models import model_from_json

    json_file = open("/home/sanket/Desktop/WebApp/Detection/Leukemia/FNNModel.json","r")
    loaded_file = json_file.read()
    json_file.close()

    #loaded as  a new model
    model = model_from_json(loaded_file)

    #load a weight into new model
    model.load_weights("/home/sanket/Desktop/WebApp/Detection/Leukemia/FNNModel.h5")
    model.compile(loss='binary_crossentropy', optimizer='Adamax', metrics=['accuracy'])

    #Model Output Shape
    model.output_shape

    #Model Summary
    model.summary()

    #Model Config
    model.get_config()

    #List all Weight Tensors
    model.get_weights()

    #Predict the Label according to Feature present in test_X
    Rounded_prediction = model.predict_classes(test_X)

    flat_list=[]
    for sublist in Rounded_prediction:
        for item in sublist:
            flat_list.append(item)

    K.clear_session()
    if( flat_list.count(1)>len(flat_list)*0.92):
        return "Cancerous"
    else:
        return "Non-Cancerous"

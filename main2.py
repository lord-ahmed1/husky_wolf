from tensorflow.keras.models import load_model
import cv2 as cv
import numpy as np
import os
import random
class WolfHuskyClassifier:
    def __init__(self):
        self.model=load_model("wolf_husky_classifier")
    def predict_file(self,filename):
        img=cv.resize(cv.imread(filename),(200,200))
        prediction=self.model.predict(np.array([img]))
        print(prediction.tolist(),"here")
        if prediction[0]>0.5:
            return "wolf"
        else:
            return "husky"

def create_features_labels(data_path):
    husky_train=os.listdir(f'{data_path}/husky')
    wolf_train=os.listdir(f'{data_path}/wolf')
    # Create a random mix of husky and wolf images
    mixed_data = [(img, 0) for img in husky_train] + [(img, 1) for img in wolf_train]
    random.shuffle(mixed_data)

    # Separate features (X) and labels (Y)
    images_names = [item[0] for item in mixed_data]
    Y = np.array([item[1] for item in mixed_data])


    X=np.array([ cv.resize(cv.imread(f"{data_path}/{i.split('_')[0]}/{i}"),(200,200))/255 for i in images_names ])
    return X,Y



load_model=WolfHuskyClassifier()

X_test,Y_test=create_features_labels('data/test internet')

load_model.model.evaluate(X_test,Y_test)
pred=load_model.model.predict(np.array(X_test))
for index in range(len(pred)):
    cv.imshow("img",X_test[index])
    cv.waitKey(0)
    print(pred[index])
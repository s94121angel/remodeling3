#!/usr/bin/python3
# tain.py
# Xavier Vasques 13/04/2021

import platform; 
import sys; 
import numpy; 
import scipy; 
import time;

import os
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import pandas as pd
from joblib import dump
from sklearn import preprocessing

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
#print("Angel is testing the CI/CD")

initial_count=0  

def count_number(): 
    global initial_count
    dir = "./my-model"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
           initial_count += 1
    return initial_count       


def train():
    with open('./my-model/log.txt', 'a') as the_file:
    	the_file.write('1\n')
    # Load directory paths for persisting model

    MODEL_DIR = os.environ["MODEL_DIR"]
    #MODEL_DIR = os.environ["/mnt/minikube"]
    MODEL_FILE_LDA = os.environ["MODEL_FILE_LDA"]
    MODEL_FILE_NN = os.environ["MODEL_FILE_NN"]
    MODEL_PATH_LDA = os.path.join(MODEL_DIR, MODEL_FILE_LDA)
    MODEL_PATH_NN = os.path.join(MODEL_DIR, MODEL_FILE_NN)
      
    # Load, read and normalize training data
    training = "./my-model/train.csv"
    data_train = pd.read_csv(training)
        
    y_train = data_train['# Letter'].values
    X_train = data_train.drop(data_train.loc[:, 'Line':'# Letter'].columns, axis = 1)

    print("Shape of the training data")
    print(X_train.shape)
    print(y_train.shape)
        
    # Data normalization (0,1)
    X_train = preprocessing.normalize(X_train, norm='l2')
    
    # Models training
    
    # Linear Discrimant Analysis (Default parameters)
    clf_lda = LinearDiscriminantAnalysis()
    clf_lda.fit(X_train, y_train)
    
    # Save model
    from joblib import dump
    dump(clf_lda, MODEL_PATH_LDA)
        
    # Neural Networks multi-layer perceptron (MLP) algorithm
    clf_NN = MLPClassifier(solver='adam', activation='relu', alpha=0.0001, hidden_layer_sizes=(500,), random_state=0, max_iter=1000)
    clf_NN.fit(X_train, y_train)
       
    # Secord model
    from joblib import dump, load
    #得到回傳值(資料夾內檔案數量)
    count_of_file=count_number()
    NAME_with_count=str(count_of_file)+"_"+MODEL_FILE_NN
    SAVE_AT_LOCAL_NN =os.path.join(MODEL_DIR,  NAME_with_count)
    time.sleep(50)#######只是單純讓網頁顯示修模中久一點
    dump(clf_NN, SAVE_AT_LOCAL_NN)
    with open('./my-model/log.txt', 'a') as the_file:
    	the_file.write('0\n')
    print("Remodeling Succeed")
        
if __name__ == '__main__':
    train()

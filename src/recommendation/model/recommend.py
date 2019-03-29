import gzip
import pandas as pd
import shelve
import pickle
import sys 
import numpy as np
from sklearn.model_selection import train_test_split
from baseline import DecisionTree
import scipy.sparse
import pdb

def get_data(file):
    path = '../data_processing/'
    cols = ['user','item','rating','timestamp']
    data = pd.read_csv(path + file,names = cols)
    return data

def readffile(path):
	with shelve.open(path, protocol=pickle.HIGHEST_PROTOCOL) as d:
		return d['content']



if __name__=="__main__":
    # filename = 'ratings_Movies_and_TV.csv'
    
    # data = get_data(filename)
    # train,test = train_test_split(data,test_size=0.3)
    # print(data.shape)
    # print(train.shape,test.shape)
    # print(test)
    # finput_iu_rating_matrix_train = "Data/iu_sparse_matrix_train.npz"
    # finput_iuclst_rating_matrix = "Data/iuclst_rating_matrix"
    
    finput_iu_sparse_matrix_train = '../data_processing/Data/iu_sparse_matrix_train.npz'
    finput_iu_sparse_matrix_test = '../data_processing/Data/iu_sparse_matrix_test.npz'
    finput_user_cluster_set = "../data_processing/Data/user_cluster_set"
    finput_iuclst_rating_matrix_train = '../data_processing/Data/iuclst_rating_matrix_train'
    finput_iuclst_rating_matrix_test = '../data_processing/Data/iuclst_rating_matrix_test'
    finput_desired_depth = 5
    
    # read into data for tree construction
    iu_sparse_matrix_train = scipy.sparse.load_npz(finput_iu_sparse_matrix_train)
    iu_sparse_matrix_test = scipy.sparse.load_npz(finput_iu_sparse_matrix_test)
    iuclst_rating_matrix_train = readffile(finput_iuclst_rating_matrix_train)
    iuclst_rating_matrix_test = readffile(finput_iuclst_rating_matrix_test)
    user_cluster_set = readffile(finput_user_cluster_set)

    # build tree
    dt_model = DecisionTree(iu_sparse_matrix_train, iu_sparse_matrix_test, iuclst_rating_matrix_train, iuclst_rating_matrix_test, user_cluster_set, finput_desired_depth)
    dt_model.buildTreeModel()
    print("\ntree construction finished")
    
    # pdb.set_trace()
    # build prediction model
    dt_model.buildPredModel()
    print("prediction model finished")
    # predict
    # dt_model.predict()
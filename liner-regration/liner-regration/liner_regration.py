from tkinter.ttk import LabeledScale
import numpy as np
from utils import prepare_for_training

class LinearRegression:
    def __init__(self,data,labels,polynomial_degree=0,sinusoid_degree=0,normalize_data=True) :
        data_processed,features_mean,features_deviation=prepare_for_training(data,polynomial_degree,sinusoid_degree,normalize_data=True)
        self.data=data_processed
        self.labels=labels
        self.feature_mean=features_mean
        self.feature_deviation=features_deviation
        self.polunomial_degree=polynomial_degree
        self.sinusoid_degree=sinusoid_degree
        self.normalize_data=normalize_data

        num_features=self.data.shape[1]
        self,theta=np.zeros((num_features,1))
    
    def train(self,alpha,num_iterations=1000):
        cost_history=self.gradient_descent(alpha,num_iterations)
        return self.theta,cost_history

    def gradient_descent(self,alpha,num_iterations):
        cost_history=[]
        for _ in range (num_iterations):
            self.gradient_step(alpha)
            cost_history.append(self.cost_funtion(self.data,self.labels))
        return cost_history


    def gradient_step(self,alpha):
        num_examples=self.data.shape[0]
        prediction=LinearRegression.hypothesis(self.data,self.theta)
        delta=prediction-self.labels
        theta=self.theta
        theta=theta-alpha*(1/num_examples)*(np.dot(delta,delta.T)).T
        self.theta=theta



    def cost_funtion(self,alpha,labels):
        num_examples=self.data.shape[0]
        delta=LinearRegression.hypothesis(self.data,self.theta)-labels
        cost=(1/2)*np.dot(delta.T,delta)/num_examples
        return cost[0][0]

    @staticmethod
    def hypothesis(data,theta):
        return np.dot(data,theta)

    def get_cost(self,data,labels):  
        data_processed = prepare_for_training(data,
         self.polynomial_degree,
         self.sinusoid_degree,
         self.normalize_data
         )[0]
        
        return self.cost_function(data_processed,labels)
    

    def predict(self,data):

        data_processed = prepare_for_training(data,
         self.polynomial_degree,
         self.sinusoid_degree,
         self.normalize_data
         )[0]
         
        predictions = LinearRegression.hypothesis(data_processed,self.theta)
        
        return predictions
        
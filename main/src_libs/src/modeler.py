# Data libraries
import pandas as pd
import numpy as np

# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning libraries
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import make_classification

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from xgboost import XGBClassifier


class Model_Maker():
    def __init__(self, dataframe= None):
        self.df = dataframe
        self.label_enc = LabelEncoder()


    def column_encoder(self, column= None, position= None):
        """
                            ---What it does---
        This function

                            ---What it needs---
            - 

                            ---What it return---
        This function
        """
        
        if column != None:
            self.column_encoded = self.label_enc.fit_transform(self.df[column])
        
        elif position != None:
            self.column_encoded = self.label_enc.fit_transform(self.df.iloc[:, position])
        
        return self.column_encoded
    

    def data_splitter(self, train_list= None, test= None, test_size= 0.33, random_state= 42, scale_data= True):
        """
                            ---What it does---
        This function

                            ---What it needs---
            - 

                            ---What it return---
        This function
        """
        
        self.X = self.df[train_list]
        self.y = self.df[test]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size= test_size,
                                                                                random_state= random_state)


        if scale_data == True:
                self.scaler = MinMaxScaler()

                self.X_train = self.scaler.fit_transform(self.X_train)
                self.X_test = self.scaler.transform(self.X_test)


        return self.X_train, self.X_test, self.y_train, self.y_test
    

    def create_linear_or_logistic_model(self, kind= 'linear', fit_intercept=True, 
                            normalize=False, copy_X=True, 
                            n_jobs=None, positive=False, 
                            penalty='l2', dual=False, 
                            tol=0.0001, C=1.0, intercept_scaling=1, 
                            class_weight=None, random_state=None, 
                            solver='lbfgs', max_iter=100, 
                            multi_class='auto', verbose=0, 
                            warm_start=False, 
                            l1_ratio=None):
        """
                            ---What it does---
        This function creates a simple linear/logistic regression model. Prints it and returns it.

                            ---What it needs---
            - The kind of model you wish to create (linear or logistic). Must be string
            - The sklearn standard arguments necessary

                            ---What it return---
        This function returns the created model
        """

        linear_list = ['linear', 'Linear', 'LINEAR']
        logistic_list = ['logistic', 'Logistic', 'LOGISTIC']

        if kind in linear_list:
            created_model = LinearRegression(fit_intercept= fit_intercept, 
                                                normalize=normalize, copy_X=copy_X, 
                                                n_jobs=n_jobs, positive=positive)
            print(self.created_model)

            self.linear_model = self.created_model.fit(self.X_train, self.y_train)
            print(self.linear_model.coef_)

            return self.linear_model
        
        elif kind in logistic_list:
            created_model = LogisticRegression(penalty= penalty, dual= dual, 
                                                    tol= tol, C= C, 
                                                    fit_intercept= fit_intercept, 
                                                    intercept_scaling= intercept_scaling, 
                                                    class_weight= class_weight, random_state= random_state, 
                                                    solver= solver, max_iter= max_iter, 
                                                    multi_class= multi_class, verbose= verbose, 
                                                    warm_start= warm_start, n_jobs= n_jobs, 
                                                    l1_ratio= l1_ratio)
            print(self.created_model) 

            self.logistic_model = self.created_model.fit(self.X_train, self.y_train)
            print(self.linear_model.coef_)

            return self.logistic_mode


    def create_random_forest (self, n_estimators=10, 
                            criterion='gini', max_depth=None, 
                            min_samples_split=2, min_samples_leaf=1, 
                            min_weight_fraction_leaf=0.0, 
                            max_features='auto', max_leaf_nodes=None, 
                            min_impurity_decrease=0.0, 
                            min_impurity_split=None, bootstrap=True, 
                            oob_score=False, n_jobs=1, 
                            random_state=None, verbose=0, 
                            warm_start=False, class_weight=None):
        """
        TODO
                            ---What it does---
        This function creates a random forest classifier model. Prints it and returns it.

                            ---What it needs---
            - The sklearn standard arguments necessary

                            ---What it return---
        This function returns the created model
        """

        created_model = RandomForestClassifier(n_estimators= n_estimators, 
                            criterion= criterion, max_depth= max_depth, 
                            min_samples_split= min_samples_split, 
                            min_samples_leaf= min_samples_leaf, 
                            min_weight_fraction_leaf= min_weight_fraction_leaf, 
                            max_features= max_features, 
                            max_leaf_nodes= max_leaf_nodes, 
                            min_impurity_decrease= min_impurity_decrease, 
                            min_impurity_split= min_impurity_split, 
                            bootstrap= bootstrap, oob_score= oob_score, 
                            n_jobs= n_jobs, random_state= n_jobs, 
                            verbose= verbose, warm_start= warm_start, 
                            class_weight= class_weight)

        self.forest_model = traffic_forest.fit(self.X_train, self.y_train)
        y_pred = forest_model.predict(self.X_test)

        return self.forest_model
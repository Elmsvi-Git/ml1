# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:51:03 2023

@author: ElaheMsvi

For any code related to reading the data
"""

import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

import pandas as pd 
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifact', "train.csv")
    test_data_path:str  = os.path.join('artifact', "test.csv")
    row_data_path:str   = os.path.join('artifact', "data.csv")
    
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or componenet")
        
        try:
            df = pd.read_csv("C:/Users/ElaheMsvi/Desktop/Projects/ML1/notebook/data/stud.csv")
            logging.info("data read and saved as df")
            os.makedirs(os.path.dirname(self.data_ingestion_config.row_data_path), exist_ok= True)
            df.to_csv(self.data_ingestion_config.row_data_path, index =False , header = True)
            
            train_set , test_set = train_test_split(df, test_size = .2 , random_state=42)
            logging.info("Train, test split done.")
            
            train_set.to_csv(self.data_ingestion_config.train_data_path, index = False , header= True)
            test_set.to_csv(self.data_ingestion_config.test_data_path , index = False , header = True)
            logging.info("ingestion of date is done")
            
            return(self.data_ingestion_config.train_data_path,
                   self.data_ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__=="__main__":

    obj = DataIngestion() 
    train_data, test_data = obj.initiate_data_ingestion()       
    
    data_transformation = DataTransformation()
    train_array,test_array,_= data_transformation.initiat_data_transformation(train_data,
                                                                           test_data)
    
    model_obj = ModelTrainer() 
    r2 , models_rep = model_obj.initate_model_trainer(train_array,test_array)
    








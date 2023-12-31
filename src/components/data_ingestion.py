import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass


from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer



#DataIngestionConfig, a dataclass(see decorator) 
# defines values for paths to training, test and raw data.

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")




class DataIngestion:
    # constructor:
    def __init__(self):
        #instance is created with a  DataIngestionConfig object
        self.ingestion_config = DataIngestionConfig()

#performs data ingestion tasks
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            #reads data csv file into pandas dataframe
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            #creates directories, if they don't exist, based on the train_data_path defined in DataIngestionConfig
            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)

            #writes the dataframe to a csv file
            df.to_csv(self.ingestion_config.raw_data_path,
                      index=False, header=True)

            #logs a message about initiating train-test split
            logging.info("Train-test split initiated")
            #splits data into train and test using train_test_split from scikit-learn
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)


            #write the train and test sets to separate csv files
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)

            #logs a message about data ingestion completion
            logging.info("Ingestion of the data is completed")

            #return the paths to train and test datasets
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path


            )


        except Exception as e:
            raise CustomException(e, sys)




if __name__ == "__main__":
    ogj = DataIngestion()
    train_data, test_data = ogj.initiate_data_ingestion()


    data_transformation = DataTransformation()


    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(
        train_data, test_data)


    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))

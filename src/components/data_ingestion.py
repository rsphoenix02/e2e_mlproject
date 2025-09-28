import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path : str = os.path.join("artifacts", "data.csv")
    train_data_path : str = os.path.join("artifacts", "train.csv")
    test_data_path : str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")

        try:
            df = pd.read_csv('notebook\data\stud.csv')

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is complete")

            return (self.data_ingestion_config.train_data_path, self.data_ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=='__main__':
    from src.components.data_tranformation import DataTransformation
    from src.components.model_trainer import ModelTrainer

    ingestion_obj = DataIngestion()
    train_data_path, test_data_path = ingestion_obj.initiate_data_ingestion()

    transformation_obj = DataTransformation()
    train_arr, test_arr, _ = transformation_obj.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer_obj = ModelTrainer()
    print(model_trainer_obj.initiate_model_trainer(train_arr, test_arr))


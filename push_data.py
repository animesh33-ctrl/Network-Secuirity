import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi 
ca = certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecuirity.exception.exception import NetworkSecuirityException
from networksecuirity.logging.logger import logging

class NetWorkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecuirityException(e,sys)
        
    def csv_to_json_converter(self,file_path):
        try :
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecuirityException(e,sys)
        
    def insert_data_into_mongodb(self,records,database,collection):
        try :
            self.database = database
            self.records = records
            self.collection = collection
            # self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            # self.database = self.mongo_client[self.database]
            # self.collection = self.database[self.collection]
            # self.collection.insert_many(self.records)
            with pymongo.MongoClient(MONGO_DB_URL) as mongo_client:
                self.database = mongo_client[database]
                self.collection = self.database[collection]
                self.collection.insert_many(records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecuirityException(e,sys)
        
if __name__ == "__main__":
    FILE_PATH = 'Network_Data\Phishing_Legitimate_full.csv'
    DATABASE = "Animesh31"
    COLLECTION = "NetworkData"
    netobj = NetWorkDataExtract()
    record = netobj.csv_to_json_converter(file_path=FILE_PATH)
    print(record)
    no_of_records = netobj.insert_data_into_mongodb(record,DATABASE,COLLECTION)
    print(no_of_records)
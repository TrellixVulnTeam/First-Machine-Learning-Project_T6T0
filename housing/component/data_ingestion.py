from housing.entity.artifact_entity import *
import os, sys
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import *
import tarfile
from six.moves import urllib


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:

            logging.info(f"{'>>'*20}Data Ingestion log started {'>>'*20}")
            self.data_ingestion_config=data_ingestion_config

        except Exception as e:
            raise HousingException(e, sys) from e


    def download_housing_data(self)-> str:
        try:
            #extract remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            # folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            os.makedirs(tgz_download_dir, exist_ok=True)

            housing_file_name= os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)

            logging.info(f"Downloading file from {download_url} into : {tgz_file_path}")

            urllib.request.urlretrieve(download_url, tgz_file_path)

            logging.info(f" File:[{tgz_file_path}] has been downloaded succesfully")

        except Exception as e:
            raise HousingException(e, sys) from e


    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir= self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir) 

            os.makedirs(raw_data_dir, exist_ok=True) 

            logging.info(f"Extracting tgz file:[tgz_file_path] into: [{raw_data_dir}]")     

            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir)
            logging.info(f"Extraction completed")

        except Exception as e:
            raise HousingException(e, sys) from e

            
                
                








            




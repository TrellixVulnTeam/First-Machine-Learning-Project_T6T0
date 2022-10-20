from housing.logger import logging
from housing.exception import HousingException
from housing.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact 
from housing.entity.config_entity import ModelPusherConfig
import os, sys
import shutil

class ModelPusher:
    def __init__(self, model_pusher_config:ModelPusherConfig,
                 model_evaluation_artifact:ModelEvaluationArtifact):

        try:
            logging.info(f"{'>>' * 30}Model Pusher log started.{'<<' * 30} ")
            self.model_pusher_config= model_pusher_config
            self.model_evaluation_artifact= model_evaluation_artifact


        except Exception as e:
            raise HousingException(e, sys) from e


    def export_model(self)-> ModelPusherArtifact:
        try: 
            evaluated_model_file_path= self.model_evaluation_artifact.evaluated_model_path
            export_dir = self.model_pusher_config.export_dir_path
            model_file_name= os.path.basename(evaluated_model_file_path)    
            export_model_file_path= os.path.join(export_dir, model_file_name)
            logging.info(f"Exporting model file: [{export_model_file_path}]")  
            os.makedirs(export_dir, exist_ok= True)

            



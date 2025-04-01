from src.Predict_Pipe.config.configuration import ConfigurationManager
from src.Predict_Pipe.components.model_trainer import ModelTrainer
from src.Predict_Pipe.logging import logger

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
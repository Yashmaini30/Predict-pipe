from src.Predict_Pipe.config.configuration import ConfigurationManager
from src.Predict_Pipe.components.model_evaluation import ModelEvaluation
from src.Predict_Pipe.logging import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
import sys
import os

# Get the absolute path of "src"
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))

if src_path not in sys.path:
    sys.path.append(src_path)

from src.Predict_Pipe.logging import logger
from src.Predict_Pipe.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.Predict_Pipe.pipeline.data_validation import DataValidationTrainingPipeline
from src.Predict_Pipe.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.Predict_Pipe.pipeline.model_trainer import ModelTrainerTrainingPipeline

logger.info("Logging has started")

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
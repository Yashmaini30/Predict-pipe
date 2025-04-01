from src.Predict_Pipe.config.configuration import ConfigurationManager
from src.Predict_Pipe.components.data_transformation import DataTransformation
from src.Predict_Pipe.logging import logger

from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            status_file = Path("artifacts/data_validation/status.txt")
            if not status_file.exists():
                logger.error(f"Status file not found at {status_file}")
                raise Exception("Data validation status file not found")
            
            with open(status_file, "r") as f:
                content = f.read()
                logger.info(f"Status file content: '{content}'")
                status = content.split(" ")[-1]
                logger.info(f"Extracted status: '{status}'")

            if status.strip() == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                logger.error(f"Data validation status is not True. Got: '{status}'")
                raise Exception("Data validation failed")

        except Exception as e:
            logger.error(f"Error in data transformation: {str(e)}")
            raise e
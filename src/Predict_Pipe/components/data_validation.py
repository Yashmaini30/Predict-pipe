import os
import pandas as pd
from src.Predict_Pipe.logging import logger
from src.Predict_Pipe.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config 

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
          
            all_schema = self.config.all_schema.get('COLUMNS', {})

            missing_cols = []
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    missing_cols.append(col)
                else:
                    expected_type = all_schema[col]
                    actual_type = data[col].dtype
                    if expected_type != actual_type:
                        validation_status = False
                        missing_cols.append(f"{col} (expected: {expected_type}, found: {actual_type})")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            if not validation_status:
                logger.error(f"Validation failed. Columns not in schema or type mismatch: {missing_cols}")

            return validation_status

        except Exception as e:
            raise e

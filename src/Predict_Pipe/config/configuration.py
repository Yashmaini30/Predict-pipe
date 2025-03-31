from pathlib import Path
from src.Predict_Pipe.constants import *
from src.Predict_Pipe.utils.common import read_yaml, create_directories
from src.Predict_Pipe.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    from pathlib import Path
from src.Predict_Pipe.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.Predict_Pipe.utils.common import read_yaml, create_directories
from src.Predict_Pipe.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH
    ):
        config_filepath = config_filepath.resolve()
        params_filepath = params_filepath.resolve()
        schema_filepath = schema_filepath.resolve()

        if not config_filepath.exists():
            raise FileNotFoundError(f"Config file not found: {config_filepath}")
        if not params_filepath.exists():
            raise FileNotFoundError(f"Params file not found: {params_filepath}")
        if not schema_filepath.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_filepath}")

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

from pathlib import Path

import os

CONFIG_FILE_PATH = os.path.abspath(os.path.join(os.getcwd(), "..", "config", "config.yaml"))
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")
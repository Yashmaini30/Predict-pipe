from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]  # Adjusted to go 3 levels up

# Define paths relative to ROOT_DIR
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"
SCHEMA_FILE_PATH = ROOT_DIR / "schema.yaml"


"""
Load and validate the application configuration from YAML files.
"""
from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "search_config.yaml"


def load_config(path: Path= CONFIG_PATH) -> dict:
    """Load the search configuration from a YAML file."""
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
    if config is None:
        raise ValueError("Configuration file is empty.")
    
    if not isinstance(config, dict):
        raise ValueError("Configuration file must contain a dictionary at the top level.")
    
    return config
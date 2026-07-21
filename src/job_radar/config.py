"""
Load and validate the application configuration from YAML files.
"""

import logging
from pathlib import Path
from urllib.parse import urlparse

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
SEARCHES_PATH = CONFIG_DIR / "searches.yaml"
COMPANIES_PATH = CONFIG_DIR / "companies.yaml"
SEARCHES_REQUIRED_FIELDS = ["title", "url"]
COMPANIES_REQUIRED_FIELDS = ["name", "url", "priority", "tags"]

logger = logging.getLogger(__name__)


def load_config(path: Path) -> dict:
    """Load the configuration from a YAML file."""
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        raise ValueError("Configuration file is empty.")

    if not isinstance(config, dict):
        raise ValueError(
            "Configuration file must contain a dictionary at the top level."
        )

    return config


def _validate_url(url: str) -> str:
    """Validate the URL format"""
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")

    url = url.strip()
    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Invalid URL: {url}")
    return url


def _validate_required_fields(item: dict, required_fields: list) -> None:
    """Validate that required fields are present."""
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field '{field}' in item: {item}")


def validate_search_config(config: dict, section: str) -> None:
    """Validate the search configuration file."""
    sections = config.keys() if section == "all" else [section]

    if section != "all" and section not in config:
        raise ValueError(f"Unknown section: {section}")

    for current_section in sections:
        searches = config.get(current_section, [])

        if not searches:
            logger.info(
                "No %s found for %s.",
                "companies" if section == "companies" else "searches",
                current_section,
            )
            continue

        for search in searches:
            _validate_required_fields(search, SEARCHES_REQUIRED_FIELDS)
            _validate_url(search["url"])


def validate_company_config(config: dict) -> None:
    """Validate the company configuration file."""
    companies = config.get("companies")

    if not isinstance(companies, list):
        raise ValueError("'companies' must contain a list.")

    if not companies:
        logger.info("No companies found.")
        return

    for company in companies:
        _validate_required_fields(company, COMPANIES_REQUIRED_FIELDS)
        _validate_url(company["url"])

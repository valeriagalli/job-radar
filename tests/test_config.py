"""
Test module for the configuration.
"""

import pytest

import job_radar.config as config


def test_no_config_file(tmp_path) -> None:
    """Validate FileNotFoundError for missing configuration file."""
    invalid_path = tmp_path / "non_existent_config.yaml"
    with pytest.raises(FileNotFoundError):
        config.load_config(path=invalid_path)


def test_empty_config_file(tmp_path) -> None:
    """Validate ValueError for empty configuration file."""
    empty_config_path = tmp_path / "empty_config.yaml"
    empty_config_path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        config.load_config(path=empty_config_path)


def test_non_dict_config(tmp_path) -> None:
    """Validate ValueError for invalid configuration file."""
    invalid_config_path = tmp_path / "invalid_config.yaml"
    invalid_config_path.write_text("- linkedin\n- jobs_ch\n", encoding="utf-8")
    with pytest.raises(ValueError):
        config.load_config(path=invalid_config_path)


def test_valid_config_file(tmp_path) -> None:
    """Validate that a valid configuration file is loaded correctly."""
    valid_config_path = tmp_path / "valid_config.yaml"
    valid_config_path.write_text(
        """
linkedin:
  - title: Software Engineer Healthcare
    url: https://example.com
jobs_ch:
  - title: Medical Software
    url: https://example.com
""",
        encoding="utf-8",
    )
    search_config = config.load_config(path=valid_config_path)
    assert isinstance(search_config, dict)
    assert "linkedin" in search_config
    assert "jobs_ch" in search_config


def test_invalid_search_section() -> None:
    """Validate ValueError for invalid section."""
    search_config = {
        "linkedin": [
            {
                "title": "Biomedical Engineer",
                "url": "invalid_url",
            }
        ]
    }

    with pytest.raises(ValueError, match="Unknown section"):
        config.validate_search_config(search_config, "invalid_section")


def test_companies_not_a_list() -> None:
    """Validate ValueError for invalid section."""
    companies_config = {
        "companies": [
            {
                "name": "Biomedical Engineer",
                "url": "invalid_url",
            }
        ]
    }

    with pytest.raises(ValueError, match="Unknown section"):
        config.validate_search_config(companies_config, "invalid_section")


def test_non_string_url_raises_value_error() -> None:
    """Validate ValueError for non-string URL."""
    search_config = {
        "linkedin": [
            {
                "title": "Biomedical Engineer",
                "url": 123,
            }
        ]
    }

    with pytest.raises(ValueError, match="must be a string"):
        config.validate_search_config(search_config, "linkedin")


def test_invalid_url_raises_value_error() -> None:
    """Validate ValueError for invalid URL."""
    search_config = {
        "linkedin": [
            {
                "title": "Biomedical Engineer",
                "url": "invalid_url",
            }
        ]
    }

    with pytest.raises(ValueError, match="Invalid URL"):
        config.validate_search_config(search_config, "linkedin")


def test_missing_required_search_field_raises_value_error() -> None:
    """Validate ValueError for missing required field in search configuration."""
    search_config = {
        "linkedin": [
            {
                "url": "https://example.com",
            }
        ]
    }
    with pytest.raises(ValueError, match="Missing required field"):
        config.validate_search_config(search_config, "linkedin")


def test_missing_required_company_field_raises_value_error() -> None:
    """Validate ValueError for missing required field in company configuration."""
    companies_config = {
        "companies": [
            {
                "name": "Company A",
                "url": "https://example.com",
                "priority": "low",
                # missing category
                # missing tags
            }
        ]
    }
    with pytest.raises(ValueError, match="Missing required field"):
        config.validate_company_config(
            companies_config,
        )

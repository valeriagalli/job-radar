"""
Test module for the configuration.
"""

import pytest

from job_radar.config import load_config


def test_no_config_file(tmp_path) -> None:
    """Validate FileNotFoundError for missing configuration file."""
    invalid_path = tmp_path / "non_existent_config.yaml"
    with pytest.raises(FileNotFoundError):
        load_config(path=invalid_path)


def test_empty_config_file(tmp_path) -> None:
    """Validate ValueError for empty configuration file."""
    empty_config_path = tmp_path / "empty_config.yaml"
    empty_config_path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        load_config(path=empty_config_path)


def test_non_dict_config(tmp_path) -> None:
    """Validate ValueError for invalid configuration file."""
    invalid_config_path = tmp_path / "invalid_config.yaml"
    invalid_config_path.write_text("- linkedin\n- jobs_ch\n", encoding="utf-8")
    with pytest.raises(ValueError):
        load_config(path=invalid_config_path)


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
indeed:
  - title: Healthcare IT
    url: https://example.com
""",
        encoding="utf-8",
    )
    config = load_config(path=valid_config_path)
    assert isinstance(config, dict)
    assert "linkedin" in config
    assert "jobs_ch" in config
    assert "indeed" in config

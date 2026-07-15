"""
Test module for the command-line interface.
"""

import pytest

import job_radar.config as config
from job_radar.cli import create_parser, run


def test_valid_choices() -> None:
    """Validate the choices for the command-line argument."""
    parser = create_parser()
    valid_choices = ["linkedin", "jobs_ch", "all", "companies"]
    for choice_str in valid_choices:
        args = parser.parse_args([choice_str])
        assert args.section == choice_str


def test_invalid_choices() -> None:
    """Validate the choices for the command-line argument."""
    parser = create_parser()
    invalid_choices = ["google", "facebook", "twitter"]
    for choice in invalid_choices:
        with pytest.raises(SystemExit):
            parser.parse_args([choice])


def test_run_routes_to_search_workflow(monkeypatch) -> None:
    """Validate that the run function routes to the search workflow for 'linkedin'."""
    search_config = {
        "linkedin": [
            {
                "title": "Biomedical Engineer",
                "url": "https://example.com",
            }
        ]
    }
    loaded_paths = []
    validated_config_data = []
    validated_sections = []
    opened_config_data = []
    opened_sections = []

    def fake_load_config(path):
        loaded_paths.append(path)
        return search_config
    
    monkeypatch.setattr("job_radar.cli.config.load_config", 
                        fake_load_config)
    
    def fake_validate_search_config(config_data, section):
        validated_config_data.append(config_data)
        validated_sections.append(section)
    
    monkeypatch.setattr("job_radar.cli.config.validate_search_config", 
                        fake_validate_search_config)

    def fake_open_links(config_data, section):
        opened_config_data.append(config_data)
        opened_sections.append(section)
    
    monkeypatch.setattr("job_radar.cli.open_links", fake_open_links)

    run("linkedin")

    assert loaded_paths == [config.SEARCHES_PATH]
    assert validated_config_data == [search_config]
    assert validated_sections == ["linkedin"]
    assert opened_config_data == [search_config]
    assert opened_sections == ["linkedin"]
    

def test_run_routes_to_company_workflow(monkeypatch, sample_company_config) -> None:
    """Validate that the run function routes to the company workflow for 'companies'."""
    loaded_paths = []
    validated_calls = []

    def fake_load_config(path):
        loaded_paths.append(path)
        return sample_company_config
    
    monkeypatch.setattr("job_radar.cli.config.load_config", fake_load_config)
    
    def fake_validate_company_config(config_data):
        validated_calls.append(config_data)
    
    monkeypatch.setattr("job_radar.cli.config.validate_company_config", 
                        fake_validate_company_config)

    run("companies")

    assert loaded_paths == [config.COMPANIES_PATH]
    assert validated_calls == [sample_company_config]

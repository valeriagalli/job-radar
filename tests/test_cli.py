"""
Test module for the command-line interface.
"""

import pytest

import job_radar.config as config
from job_radar.cli import create_parser, run


def test_valid_choices() -> None:
    """Validate the choices for the command-line argument."""
    platform_choices = ["linkedin", "jobs_ch"]
    parser = create_parser(platform_choices)
    valid_choices = [*platform_choices, "all"]
    for choice_str in valid_choices:
        args = parser.parse_args([choice_str])
        assert args.section == choice_str


def test_invalid_choices() -> None:
    """Validate the choices for the command-line argument."""
    platform_choices = ["linkedin", "jobs_ch"]
    parser = create_parser(platform_choices)
    invalid_choices = ["google", "facebook", "twitter"]
    for choice in invalid_choices:
        with pytest.raises(SystemExit):
            parser.parse_args([choice])


def test_run_routes_to_search_workflow(monkeypatch) -> None:
    """Validate that the run function routes to the search workflow for 'linkedin'."""
    search_config = {
        "linkedin": [
            {
                "name": "Biomedical Engineer",
                "url": "https://example.com",
            }
        ]
    }

    opened_config_data = []
    opened_sections = []

    def fake_open_links(config_data, section):
        opened_config_data.append(config_data)
        opened_sections.append(section)

    monkeypatch.setattr("job_radar.cli.open_links", fake_open_links)

    run("linkedin", search_config)

    assert opened_config_data == [search_config]
    assert opened_sections == ["linkedin"]

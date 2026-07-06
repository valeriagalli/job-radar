"""
Test module for the browser launcher.
"""

import pytest

from job_radar.launcher import open_links


@pytest.fixture
def sample_config() -> dict[str, list[dict[str, str]]]:
    """Return a sample configuration used by launcher tests."""
    return {
        "linkedin": [
            {
                "title": "Software Engineer Healthcare",
                "url": "https://www.linkedin.com/jobs",
            }
        ],
        "jobs_ch": [
            {
                "title": "Medical Imaging",
                "url": "https://www.jobs.ch/en/vacancies",
            }
        ],
        "indeed": [
            {
                "title": "Scientific Software Engineer",
                "url": "https://ch.indeed.com/jobs",
            }
        ],
    }


@pytest.fixture
def fake_browser(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """Mock broswer opening and collect opened URLs."""
    opened_urls = []

    def fake_open_new_tab(url):
        opened_urls.append(url)

    monkeypatch.setattr("job_radar.launcher.webbrowser.open_new_tab", fake_open_new_tab)

    return opened_urls


def test_open_single_section(sample_config, fake_browser) -> None:
    """Validate correct opening of URLs for a single section."""
    open_links(sample_config, "linkedin")
    assert fake_browser == ["https://www.linkedin.com/jobs"]


def test_open_all_sections(sample_config, fake_browser) -> None:
    """Validate that the open_links function opens all the URLs from all sections."""
    open_links(sample_config, "all")
    assert fake_browser == [
        "https://www.linkedin.com/jobs",
        "https://www.jobs.ch/en/vacancies",
        "https://ch.indeed.com/jobs",
    ]


def test_empty_section(fake_browser) -> None:
    """Validate that empty sections do not open browser tabs."""
    config = {
        "linkedin": [],
        "jobs_ch": [],
        "indeed": [],
        "all": [],
    }

    open_links(config, "indeed")
    assert fake_browser == []
    open_links(config, "all")
    assert fake_browser == []


def test_invalid_section(sample_config) -> None:
    """Validate ValueError for invalid section."""
    with pytest.raises(ValueError, match="Unknown section"):
        open_links(sample_config, "invalid_section")


def test_non_string_url_raises_value_error() -> None:
    """Validate ValueError if there are link URLs not of string type."""
    config = {
        "linkedin": [{"title": "Software Engineer Healthcare", "url": 123}],
    }
    with pytest.raises(ValueError, match="must be a string"):
        open_links(config, "linkedin")


def test_invalid_url_format_raises_value_error() -> None:
    """Validate ValueError if there are invalid links in the config file."""
    config = {
        "linkedin": [{"title": "Software Engineer Healthcare", "url": "invalid_url"}],
    }
    with pytest.raises(ValueError, match="Invalid URL"):
        open_links(config, "linkedin")

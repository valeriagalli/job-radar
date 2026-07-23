"""
Common pytest fixtures for testing the job_radar package.
"""

import pytest


@pytest.fixture
def sample_search_config() -> dict[str, list[dict[str, str]]]:
    """Return a sample configuration used by launcher tests."""
    return {
        "linkedin": [
            {
                "name": "Software Engineer Healthcare",
                "url": "https://www.linkedin.com/jobs",
            }
        ],
        "jobs_ch": [
            {
                "name": "Medical Imaging",
                "url": "https://www.jobs.ch/en/vacancies",
            }
        ],
    }


@pytest.fixture
def sample_company_config() -> dict:
    """Return a valid sample company configuration."""
    return {
        "companies": [
            {
                "name": "Company A",
                "url": "https://example.com",
                "category": "monitor",
                "priority": "high",
                "tags": ["software"],
            }
        ]
    }


@pytest.fixture
def fake_browser(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """Mock broswer opening and collect opened URLs."""
    opened_urls = []

    def fake_open_new_tab(url):
        opened_urls.append(url)

    monkeypatch.setattr("job_radar.launcher.webbrowser.open_new_tab", fake_open_new_tab)

    return opened_urls

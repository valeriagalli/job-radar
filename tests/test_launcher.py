"""
Test module for the browser launcher.
"""

from job_radar.launcher import open_links


def test_open_single_section(sample_search_config, fake_browser) -> None:
    """Validate correct opening of URLs for a single section."""
    open_links(sample_search_config, "linkedin")
    assert fake_browser == ["https://www.linkedin.com/jobs"]


def test_open_all_sections(sample_search_config, fake_browser) -> None:
    """Validate that the open_links function opens all the URLs from all sections."""
    open_links(sample_search_config, "all")
    assert fake_browser == [
        "https://www.linkedin.com/jobs",
        "https://www.jobs.ch/en/vacancies",
    ]


def test_empty_section(fake_browser) -> None:
    """Validate that empty sections do not open browser tabs."""
    config = {
        "linkedin": [],
        "jobs_ch": [],
        "all": [],
    }

    open_links(config, "jobs_ch")
    assert fake_browser == []
    open_links(config, "all")
    assert fake_browser == []

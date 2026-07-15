"""
Command-line interface for Job Radar.
"""

import argparse

import job_radar.config as config
from job_radar.launcher import open_links
from job_radar.logging_config import configure_logging


def create_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="job-radar",
        description="Open predefined job searches in your default web browser.",
    )

    parser.add_argument(
        "section",
        choices=["linkedin", "jobs_ch", "all", "companies"],
        help="Search platform to open",
    )

    return parser


def run(section: str) -> None:
    """Run the workflow selected by the user"""
    if section == "companies":
        companies_config = config.load_config(config.COMPANIES_PATH)
        config.validate_company_config(companies_config)
    else:
        searches_config = config.load_config(config.SEARCHES_PATH)
        config.validate_search_config(searches_config, section)
        open_links(searches_config, section)


def main() -> None:
    """Parse command-line arguments and launch the selected searches."""
    configure_logging()

    parser = create_parser()
    args = parser.parse_args()

    run(args.section)


if __name__ == "__main__":
    main()

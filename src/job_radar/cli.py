"""
Command-line interface for Job Radar.
"""

import argparse
import sys

import job_radar.config as config
from job_radar.launcher import open_links
from job_radar.logging_config import configure_logging


def create_parser(platform_choices) -> argparse.ArgumentParser:
    """Create and return the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="job-radar",
        description="Open predefined job searches in your default web browser.",
    )

    parser.add_argument(
        "section",
        choices=[*platform_choices, "all"],
        help="Search platform to open (from searches.yaml), or 'all'",
    )

    return parser


def run(section: str, searches_config: dict) -> None:
    """Run the workflow selected by the user"""
    open_links(searches_config, section)


def main() -> None:
    """Parse command-line arguments and launch the selected searches."""
    configure_logging()

    try:
        searches_config = config.load_config(config.SEARCHES_PATH)
        platform_choices = list(searches_config.keys())
    except FileNotFoundError:
        sys.exit(
            "config/searches.yaml not found. Copy config/searches.example.yaml "
            "to config/searches.yaml and add your own searches."
        )

    parser = create_parser(platform_choices)
    args = parser.parse_args()

    run(args.section, searches_config)


if __name__ == "__main__":
    main()

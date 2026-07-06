"""
Command-line interface for Job Radar.
"""
import argparse

from job_radar.config import load_config
from job_radar.launcher import open_links


def create_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        description="Open predefined job searches in your default web browser."
    )

    parser.add_argument(
        "section",
        choices=["linkedin", "jobs_ch", "indeed", "all"],
        help="Search platform to open",
    )
    
    return parser


def main() -> None:
    """Parse command-line arguments and launch the selected searches."""
    parser = create_parser()
    args = parser.parse_args()

    config = load_config()

    open_links(config, args.section)


if __name__ == "__main__":
    main()
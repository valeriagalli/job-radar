"""
Test module for the command-line interface.
"""
import pytest
 
from job_radar.cli import create_parser


def test_valid_choices() -> None:
    """Validate the choices for the command-line argument."""
    parser = create_parser()
    valid_choices = ["linkedin", "jobs_ch", "indeed", "all"]
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
    
    
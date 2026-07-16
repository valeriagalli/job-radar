"""
Open configured job search URLs in the default web browser.
"""

import logging
import webbrowser

logger = logging.getLogger(__name__)


def open_links(search_config: dict, section: str) -> None:
    """Open the configured searches for the selected section."""
    sections = search_config if section == "all" else [section]

    for current_section in sections:
        logger.info("Opening %s searches:", current_section)

        for search in search_config[current_section]:
            logger.info("- %s", search["title"])
            webbrowser.open_new_tab(search["url"])

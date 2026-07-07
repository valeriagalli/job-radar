"""
Open configured job search URLs in the default web browser.
"""

import webbrowser
import logging
from urllib.parse import urlparse


logger= logging.getLogger(__name__)


def open_links(config: dict, section: str) -> None:
    sections = config.keys() if section == "all" else [section]

    if section != "all" and section not in config:
        raise ValueError(f"Unknown section: {section}")

    for current_section in sections:
        links = config.get(current_section, [])

        if not links:
            logger.info("No searches found for %s.", current_section)
            continue

        logger.info("Opening %s searches:", current_section)
        for item in links:
            title = item.get("title", "Unnamed search")
            url = item.get("url")

            if not isinstance(url, str):
                raise ValueError(f"URL for '{title}' must be a string.")

            url = url.strip()
            parsed = urlparse(url)

            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                raise ValueError(f"Invalid URL for '{title}': {url}")

            logger.info("- %s", title)
            webbrowser.open_new_tab(url)

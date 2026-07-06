"""
Open configured job search URLs in the default web browser.
"""
import webbrowser
from urllib.parse import urlparse


def open_links(config: dict, section: str) -> None:
    sections = config.keys() if section == "all" else [section]

    if section != "all" and section not in config:
        print(section)
        raise ValueError(f"Unknown section: {section}")

    for current_section in sections:
        links = config.get(current_section, [])

        if not links:
            print(f"No searches found for '{current_section}'.")
            continue
        
        print(f"\nOpening {current_section} searches:")
        for item in links:
            title = item.get("title", "Unnamed search")
            url = item.get("url")

            if not isinstance(url, str):
                raise ValueError(f"URL for '{title}' must be a string.")
            
            url = url.strip()
            parsed = urlparse(url)

            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                raise ValueError(f"Invalid URL for '{title}': {url}")
            
            print(f"- {title}")
            webbrowser.open_new_tab(url)
        
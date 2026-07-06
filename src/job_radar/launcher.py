"""
Open configured job search URLs in the default web browser.
"""
import webbrowser


def open_links(config: dict, section: str) -> None:
    sections = config.keys() if section == "all" else [section]

    for current_section in sections:
        links = config.get(current_section, [])

        if not links:
            print(f"No searches found for '{current_section}'.")
            continue
        
        print(f"\nOpening {current_section} searches:")
        for item in links:
            title = item.get("title", "Unnamed search")
            url = item.get("url")

            if url is None:
                print(f"Skipping '{title}': missing URL.")
                continue

            print(f"- {title}")
            webbrowser.open_new_tab(url)
        
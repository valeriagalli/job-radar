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

        for item in links:
            name = item.get("name", "Unnamed search")
            url = item.get("url")

            if url is None:
                print(f"Skipping '{name}': missing URL.")
                continue

            print(f"- {name}")
            webbrowser.open_new_tab(url)
        print(f"\nOpening {current_section}:")
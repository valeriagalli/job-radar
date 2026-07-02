from pathlib import Path
import argparse
import webbrowser
import yaml

CONFIG_PATH = Path("searches.yaml")


def load_config(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def open_links(config: dict, section: str) -> None:
    sections = config.keys() if section == "all" else [section]

    for current_section in sections:
        links = config.get(current_section, [])

        print(f"\nOpening {current_section}:")

        for item in links:
            print(f"- {item['name']}")
            webbrowser.open_new_tab(item["url"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "section",
        choices=["linkedin", "jobs_ch", "indeed", "all"],
        help="Which section to open",
    )
    args = parser.parse_args()

    config = load_config(CONFIG_PATH)
    open_links(config, args.section)


if __name__ == "__main__":
    main()
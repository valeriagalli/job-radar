# Job Radar

A Python CLI application that streamlines the search for software engineering and AI roles in healthcare by automating searches across multiple job platforms.

## Motivation

This application streamlines job searches by launching predefined search queries across multiple job platforms.
Searching for software engineering positions often requires repeating the same searches every day on different platforms (e.g. LinkedIn, jobs.ch, Indeed.ch, etc). 
Job Radar automates this repetitive workflow while serving as a practical software engineering project to explore modern Python development, testing, CI/CD, and containerization.


## Installation (Windows)

### PowerShell

Clone the repository

```bash
git clone https://github.com/<your_username>/job-radar.git
cd job-radar
```

Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project

```powershell
pip install -e ".[dev]"
```

## Usage

Open a single job search platform:

```bash
job-radar linkedin
job-radar jobs_ch
job-radar indeed
```

Or open all configured searches:

```bash
job-radar all
```


## Features (v0.1)

- Supports multiple job platforms (LinkedIn, jobs.ch, Indeed).
- Opens searches in the default web browser.
- Platform-specific execution from the command line.


## Project structure
```text
job-radar/
├── src/
│   └── job_radar/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       └── launcher.py
├── tests/
│   ├── test_cli.py
│   ├── test_config.py
│   └── test_launcher.py
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── search_config.yaml
```

## Roadmap

### v0.1
- [x] Project skeleton
- [x] YAML configuration
- [x] Modular architecture
- [x] Browser launcher
- [x] Command-line interface

### v0.2
- [X] Unit tests
- [X] Ruff formatting
- [X] Logging

### v0.3
- [ ] Console Script
- [ ] Docker support
- [ ] GitHub Actions

### v1.0
- [ ] Career page monitoring
- [ ] Job scoring


## Status

Under active development.
Current milestone: v0.2 


# Job Radar

A Python CLI application that streamlines the search for software engineering and AI roles in healthcare by automating searches across multiple job platforms.

## Motivation

A CLI that opens predefined, saved job searches with a single command, instead of
manually reconstructing the same filtered search each time. Platform-agnostic by
design: search platforms are just top-level keys in `searches.yaml`, adding a new
one (e.g. swissdev.ch) requires no code changes. Built primarily as a practical
project for exploring modern Python packaging, testing, and CI/CD, using my own
job search as the working example. Configured out of the box with LinkedIn and
jobs.ch; Indeed.ch was tried initially but dropped, results for my specific search
terms were weaker there, though that's likely a reflection of my queries rather
than a general limitation of the platform.

## Installation (Windows)

### PowerShell

Clone the repository:

```bash
git clone https://github.com/<your_username>/job-radar.git
cd job-radar
```

Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project:

```powershell
pip install -e ".[dev]"
```

Set up your configuration (personal config is gitignored, copy from the examples):

```powershell
Copy-Item config\companies.example.yaml config\companies.yaml
Copy-Item config\searches.example.yaml config\searches.yaml
```

Then edit `config/companies.yaml` and `config/searches.yaml` with your own target companies and saved searches.


## Project structure
```text
job-radar/
├── .github/
│   └── workflows/
│       └── quality-checks.yml
├── config/
│   ├── companies.example.yaml
│   ├── job_profile.yaml
│   └── searches.example.yaml
├── src/
│   └── job_radar/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── launcher.py
│       └── logging_config.py
├── tests/
│   ├── conftest.py
│   ├── test_cli.py
│   ├── test_config.py
│   └── test_launcher.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

Note: `config/companies.yaml` and `config/searches.yaml` hold personal search targets and
are gitignored. Copy the `.example.yaml` files to get started (see Installation).


## Roadmap

### v0.1
- [x] Project skeleton
- [x] YAML configuration
- [x] Modular architecture
- [x] Browser launcher
- [x] Command-line interface

### v0.2
- [x] Unit tests
- [x] Ruff formatting
- [x] Logging

### v0.3
- [x] Console Script
- [x] GitHub Actions

### v0.4
- [x] Improve search relevance
- [x] Investigate company-specific career-page search (see Design notes below) — parked

### v0.5
- [ ] Company-specific search via Adzuna + client-side filtering
- [ ] Docker support


## Status

Search-URL launcher (LinkedIn, jobs.ch) is feature-complete for personal use.
Actively building company-specific search via Adzuna.
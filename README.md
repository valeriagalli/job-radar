# Job Radar

A Python CLI application that streamlines the search for software engineering and AI roles in healthcare by automating searches across multiple job platforms.

## Motivation

This application streamlines job searches by launching predefined search queries across multiple job platforms.
Searching for software engineering positions often requires repeating the same searches every day on different platforms (e.g. LinkedIn, jobs.ch, Indeed.ch, etc). 
Job Radar automates this repetitive workflow while serving as a practical software engineering project to explore modern Python development, testing, CI/CD, and containerization.


## Features (v0.1)

- Supports multiple job platforms (LinkedIn, jobs.ch, Indeed).
- Opens searches in the default web browser.
- Platform-specific execution from the command line.


## Project structure
```text
job-radar/
│   .gitignore
│   LICENSE
│   project.toml
│   README.md
│
├───src
│       __init__.py.py
│
└───tests
```

## Roadmap

### v0.1

- [X] Project skeleton
- [ ] YAML configuration
- [ ] Browser launcher
- [ ] CLI


## Status

Under active development.
Current milestone: v0.1 (MVP)

The current goal is to build a simple browser launcher driven by a YAML configuration file.
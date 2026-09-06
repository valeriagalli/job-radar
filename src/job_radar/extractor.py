"""
ETL pipeline to fetch jobs from company career pages.
"""

import re
from pathlib import Path

import requests

from job_radar.config import load_config

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
JOB_PROFILE_PATH = CONFIG_DIR / "job_profile.yaml"
job_profile_config = load_config(JOB_PROFILE_PATH)
tags = job_profile_config["tags"]

REMOVE_STRINGS = [
    "(m/f/d)",
    "(f/m/d)",
    "(m/w/d)",
    "(w/m/d)",
    "(m/f/x)",
    "(all genders)",
]


def fetch_jobs(response: requests.Response) -> list[dict]:
    """Fetch jobs from career webpage."""
    jobs = response.json()

    if not isinstance(jobs, list):
        raise (TypeError, "Extracted job list must be a list")

    return jobs


def filter_job_location(jobs: list[dict]) -> list[dict]:
    """Filter jobs by location."""
    local_jobs = []

    for job in jobs:
        location = job.get("country").get("label")

        if location == "Switzerland":
            if isinstance(job["location"], dict):
                location = job["location"]["label"]
            else:
                location = "Unspecified"

            local_jobs.append(job)

    print(f"Found {len(local_jobs)} jobs for the desired location")

    return local_jobs


def filter_job_relevance(jobs: list[dict]) -> list[dict]:
    """Filter jobs by relevance based on predefined tags."""
    relevant_jobs = []
    print(tags)
    for job in jobs:
        title = normalize_job_title(job.get("title"))
        print(title)
        if any(tag in title for tag in tags):
            relevant_jobs.append(job)

    print(f"Found {len(relevant_jobs)} relevant jobs")
    return relevant_jobs


def normalize_job_title(title: str) -> str:
    """Normalize job title before filtering."""
    title = title.lower()

    title = re.sub(
        r"\(\d+\s*%(?:\s*-\s*\d+\s*%)?\)",
        "",
        title,
    )

    for remove in REMOVE_STRINGS:
        title = title.replace(remove, "")

    return " ".join(title.split())


if __name__ == "__main__":
    urls = {
        "jnj": "https://jj.wd5.myworkdayjobs.com/wday/cxs/jj/JJ/jobs",
        "roche": "https://roche.wd3.myworkdayjobs.com/wday/cxs/roche/roche-ext/jobs",
    }

    for name, url in urls.items():
        response = requests.post(url, json={}, timeout=10)

        print(f"\n{name}")
        print(response.status_code)
        print(response.headers.get("content-type"))
        print(response.text[:500])

    # payload = {
    #     "appliedFacets": {},
    #     "limit": 20,
    #     "offset": 0,
    #     "searchText": ""
    # }

    # response = requests.post(
    #     url,
    #     json=payload,
    #     timeout=10,
    # )

    response.raise_for_status()

    jobs = fetch_jobs(response)

    print(jobs)

    local_jobs = filter_job_location(jobs)

    relevant_jobs = filter_job_relevance(local_jobs)

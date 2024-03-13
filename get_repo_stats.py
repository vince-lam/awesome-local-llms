import datetime
import json
import os
import pandas as pd
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, List, Union


def fetch_repo_info(repo: str) -> Dict[str, Union[str, int]]:
    """
    Fetches information about a GitHub repository.

    Args:
        repo (str): The repository name in the format "owner/repo".

    Returns:
        Dict[str, Union[str, int]]: A dictionary containing various information about the repository,
        including the repository name, stars count, forks count, contributors count, open issues count,
        watchers count, releases count, last commit date, license information, repository description,
        and the languages used in the repository.

    Raises:
        requests.exceptions.HTTPError: If an HTTP error occurs during the API request.
        Exception: If any other error occurs during the API request.
    """
    base_url = f"https://api.github.com/repos/{repo}"
    try:
        repo_response = requests.get(base_url, headers=headers)
        repo_data = repo_response.json()

        # Fetch contributors count
        contributors_count = 0
        page = 1
        while True:
            contributors_url = f"{base_url}/contributors?page={page}&per_page=100"
            contributors_response = requests.get(contributors_url, headers=headers)
            contributors = contributors_response.json()
            if not contributors:
                break
            contributors_count += len(contributors)
            page += 1

        # Fetch languages
        languages_url = f"{base_url}/languages"
        languages_response = requests.get(languages_url, headers=headers)
        languages = languages_response.json().keys()

        # Fetch releases count
        releases_count = 0
        page = 1
        while True:
            releases_url = f"{base_url}/releases?page={page}&per_page=100"
            releases_response = requests.get(releases_url, headers=headers)
            releases = releases_response.json()
            if not releases:
                break
            releases_count += len(releases)
            page += 1

        last_commit = repo_data["pushed_at"]
        # Parse the datetime string into a datetime object
        last_commit_datetime = datetime.strptime(last_commit, "%Y-%m-%dT%H:%M:%SZ")
        # Calculate the time since the last commit
        time_since_last_commit = datetime.now() - last_commit_datetime

        # Convert the time since the last commit to days, hours, and minutes
        days, remainder = divmod(time_since_last_commit.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, _ = divmod(remainder, 60)

        # License information check
        if "license" in repo_data and repo_data["license"]:
            license_info = repo_data["license"]["name"]
        else:
            license_info = "No license"

        stats: Dict[str, Union[str, int]] = {
            "Owner": repo.split("/")[0],
            "Repository Name": repo.split("/")[1],
            "About": repo_data["description"],
            "Stars": repo_data["stargazers_count"],
            "Forks": repo_data["forks_count"],
            "Issues": repo_data["open_issues_count"],
            "Contributors": contributors_count,
            "Releases": releases_count,
            "Watchers": repo_data["subscribers_count"],
            "Time Since Last Commit": f"{int(days)} days, {int(hours)} hrs, {int(minutes)} mins",
            "License": license_info,
            "Languages": ", ".join(languages),
            "URL": f"https://github.com/{repo}",
        }
        print(stats)
        return stats

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    finally:
        time.sleep(1)


if __name__ == "__main__":
    start_time = time.time()
    load_dotenv()
    api_token = os.getenv("API_TOKEN")
    headers = {"Authorization": f"token {api_token}"}

    # Load the list of repositories from the repos.json file
    with open("repos.json", "r") as f:
        repos: List[str] = json.load(f)

    repo_info_list: List[Dict[str, Union[str, int]]] = []
    for repo in repos:
        info = fetch_repo_info(repo)
        if info:  # Ensure info is not None
            repo_info_list.append(info)

    # Create a DataFrame and export to CSV
    df = pd.DataFrame(repo_info_list)
    df = df.drop_duplicates()
    df = df.sort_values(by="Stars", ascending=False)
    dir_name = "outputs/"

    # create path if it doesnt exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    current_datetime = datetime.now().strftime("%Y-%m-%d_%H%M")
    csv_filename = f"{dir_name}{current_datetime}_repo_stats.csv"
    df.to_csv(csv_filename, index=False)

    end_time = time.time()
    duration = end_time - start_time
    minutes, seconds = divmod(duration, 60)

    print(f"Data exported: {csv_filename}")
    print(f"Duration: {int(minutes)} minutes and {int(seconds)} seconds")

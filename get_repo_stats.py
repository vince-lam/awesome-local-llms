import datetime
import json
import os
import pandas as pd
import re
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from tabulate import tabulate
from typing import Dict, List, Union


def fetch_repo_info(repo: str, headers: Dict[str, str]) -> Dict[str, Union[str, int]]:
    """
    Fetches information about a GitHub repository.

    Args:
        repo (str): The repository name in the format "owner/repo".
        headers (Dict[str, str]): The headers for the API request.

    Returns:
        Dict[str, Union[str, int]]: A dictionary containing various information about the repository.

    Raises:
        requests.exceptions.HTTPError: If an HTTP error occurs during the API request.
        Exception: If any other error occurs during the API request.
    """
    base_url = f"https://api.github.com/repos/{repo}"
    try:
        repo_response = requests.get(base_url, headers=headers)
        repo_response.raise_for_status()  # Raise an exception for bad status codes
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
            "About": repo_data.get("description", "No description available"),
            "Stars": repo_data.get("stargazers_count", 0),
            "Forks": repo_data.get("forks_count", 0),
            "Issues": repo_data.get("open_issues_count", 0),
            "Contributors": contributors_count,
            "Releases": releases_count,
            "Watchers": repo_data.get("subscribers_count", 0),
            "Time Since Last Commit": f"{int(days)} days, {int(hours)} hrs, {int(minutes)} mins",
            "License": license_info,
            "Languages": ", ".join(languages),
            "URL": f"https://github.com/{repo}",
        }
        print(stats)
        return stats

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for repo {repo}: {http_err}")
    except KeyError as key_err:
        print(f"Key error occurred for repo {repo}: {key_err}")
    except Exception as err:
        print(f"An error occurred for repo {repo}: {err}")

    return None  # Return None if there was an error


def fetch_all_repo_info(repos: List[str], headers: Dict[str, str]) -> pd.DataFrame:
    repo_info_list: List[Dict[str, Union[str, int]]] = []
    for repo in repos:
        info = fetch_repo_info(repo, headers)
        if info is not None:  # Only append if info is not None
            repo_info_list.append(info)

    # Create a DataFrame and remove duplicates
    if repo_info_list:  # Only create DataFrame if list is not empty
        df = pd.DataFrame(repo_info_list)
        df = df.drop_duplicates()
        df = df.sort_values(by="Stars", ascending=False)
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].apply(lambda x: "{:,}".format(x))
        return df
    else:
        print("No valid repository data found.")
        return pd.DataFrame()  # Return an empty DataFrame if no data


def output_to_csv(df: pd.DataFrame, dir_name: str, current_datetime: str) -> None:
    csv_filename = f"{dir_name}{current_datetime}_repo_stats.csv"
    df.to_csv(csv_filename, index=False)


def create_markdown_file(
    df: pd.DataFrame, dir_name: str, current_datetime: str
) -> None:
    # Filter out repos with less than 100 stars
    df["stars_int"] = df["Stars"].str.replace(",", "").astype(int)
    df = df[df["stars_int"] > 100]
    # Filter out repos that have not been updated in the last 60 days
    df["Days Since Commit"] = (
        df["Time Since Last Commit"].str.extract("(\d+)").astype(int)
    )
    df = df[df["Days Since Commit"] <= 60]

    df["Repo"] = df.apply(
        lambda row: f'[{row["Repository Name"]}](https://github.com/{row["Owner"]}/{row["Repository Name"]})',
        axis=1,
    )
    df = df.reset_index()
    df["#"] = df.index + 1
    col_order = [
        "#",
        "Repo",
        "About",
        "Stars",
        "Forks",
        "Issues",
        "Contributors",
        "Releases",
        "License",
        "Time Since Last Commit",
    ]
    df = df[col_order]
    markdown_table = tabulate(df, headers="keys", tablefmt="github", showindex=False)
    condensed_markdown_table = re.sub(r" {3,}", "  ", markdown_table)
    condensed_markdown_table = re.sub(r"-{4,}", "----------", condensed_markdown_table)
    markdown_filename = f"{dir_name}{current_datetime}_repo_stats.md"

    with open(markdown_filename, "w") as f:
        f.write(condensed_markdown_table)


def main():
    start_time = time.time()
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H%M")
    load_dotenv()
    api_token = os.getenv("API_TOKEN")
    headers = {"Authorization": f"token {api_token}"}

    dir_name = "outputs/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Load the list of repositories from repos.json
    with open("repos.json", "r") as f:
        repos: List[str] = json.load(f)

    df = fetch_all_repo_info(repos, headers)
    output_to_csv(df, dir_name, current_datetime)
    create_markdown_file(df, dir_name, current_datetime)

    end_time = time.time()
    duration = end_time - start_time
    minutes, seconds = divmod(duration, 60)

    print(f"Duration: {int(minutes)} minutes and {int(seconds)} seconds")


if __name__ == "__main__":
    main()

import datetime
import os
import pandas as pd
import requests
import time
from datetime import datetime
from dotenv import load_dotenv

# List of GitHub repositories in the format 'owner/repo'
repos = [
    "ggerganov/llama.cpp",
    "ollama/ollama",
    "open-webui/open-webui",
    "ollama-webui/ollama-webui",
    "LostRuins/koboldcpp",
    "janhq/jan",
    "nat/openplayground",
    "Mozilla-Ocho/llamafile",
    "nomic-ai/gpt4all",
    "oobabooga/text-generation-webui",
    "psugihara/FreeChat",
    "cztomsik/ava",
    "withcatai/catai",
    "Mobile-Artificial-Intelligence/maid",
    "mudler/LocalAI",
    "ptsochantaris/emeltal",
    "pythops/tenere",
    "semperai/amica",
    "guinmoon/LLMFarm",
    "h2oai/h2ogpt",
    "imartinez/privateGPT",
    "huggingface/chat-ui",
    "ParisNeo/lollms-webui",
    "SillyTavern/SillyTavern",
    "NimbleBoxAI/ChainFury",
    "lobehub/lobe-chat",
    "turboderp/exui",
    "PromtEngineer/localGPT",
    "shinomakoi/AI-Messenger",
    "Mintplex-Labs/anything-llm",
    "iohub/collama",
]


def fetch_repo_info(repo):
    base_url = f"https://api.github.com/repos/{repo}"
    try:
        repo_response = requests.get(base_url, headers=headers)
        repo_data = repo_response.json()

        # Fetch contributors count (simplified)
        contributors_url = f"{base_url}/contributors?per_page=100"
        contributors_response = requests.get(contributors_url, headers=headers)
        contributors_count = len(contributors_response.json())

        # Fetch languages
        languages_url = f"{base_url}/languages"
        languages_response = requests.get(languages_url, headers=headers)
        languages = languages_response.json().keys()

        # Fetch releases count
        releases_url = f"{base_url}/releases"
        releases_response = requests.get(releases_url, headers=headers)
        releases_count = len(releases_response.json())

        last_commit = repo_data["pushed_at"]
        # Parse the datetime string into a datetime object
        last_commit_datetime = datetime.strptime(last_commit, "%Y-%m-%dT%H:%M:%SZ")
        # Format the datetime object into a more readable string
        last_commit_readable = last_commit_datetime.strftime("%B %d, %Y, %H:%M:%S")

        # License information check
        if "license" in repo_data and repo_data["license"]:
            license_info = repo_data["license"]["name"]
        else:
            license_info = "No license"

        stats = {
            "Repository Name": repo_data["name"],
            "Stars": repo_data["stargazers_count"],
            "Forks": repo_data["forks_count"],
            "Contributors": contributors_count,
            "Issues": repo_data["open_issues_count"],
            "Watchers": repo_data["subscribers_count"],
            "Releases": releases_count,
            "Last Commit": last_commit_readable,
            "License": license_info,
            "About": repo_data["description"],
            "Languages": ", ".join(languages),
        }
        print(stats)
        return stats

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Specific HTTP related error
    except Exception as err:
        print(f"An error occurred: {err}")  # Any other error
    finally:
        time.sleep(1)  # Delay between requests to avoid rate limiting


if __name__ == "__main__":
    start_time = time.time()
    load_dotenv()
    api_token = os.getenv("API_TOKEN")
    headers = {"Authorization": f"token {api_token}"}

    repo_info_list = []
    for repo in repos:
        info = fetch_repo_info(repo)
        if info:  # Ensure info is not None
            repo_info_list.append(info)

    # Create a DataFrame and export to CSV
    df = pd.DataFrame(repo_info_list)
    df = df.sort_values(by="Stars", ascending=False)
    dir_name = "outputs/"

    # create path if it doesnt exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    csv_filename = f"{dir_name}{current_datetime}_repo_stats.csv"
    df.to_csv(csv_filename, index=False)

    end_time = time.time()
    duration = end_time - start_time
    minutes, seconds = divmod(duration, 60)

    print(f"Data exported: {csv_filename}")
    print(f"Duration: {int(minutes)} minutes and {int(seconds)} seconds")

import os
import requests
from dotenv import load_dotenv

# Load your token from .env
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

# Update these to match your repo
OWNER = "YoussefShaaban07"
REPO = "pr-bot-test"

# Headers required by GitHub's API for authentication
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_open_pull_requests():
    """Fetch all open PRs for the repo."""
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_pr_diff(pr_number):
    """Fetch the raw diff for a specific PR number."""
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}"
    diff_headers = headers.copy()
    diff_headers["Accept"] = "application/vnd.github.v3.diff"
    response = requests.get(url, headers=diff_headers)
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    prs = get_open_pull_requests()
    print(f"Found {len(prs)} open PR(s):\n")

    for pr in prs:
        print(f"PR #{pr['number']}: {pr['title']}")

    if prs:
        first_pr_number = prs[0]["number"]
        print(f"\n--- Diff for PR #{first_pr_number} ---\n")
        diff = get_pr_diff(first_pr_number)
        print(diff)
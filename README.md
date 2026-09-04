# PR Review Bot

Hi, welcome to my Pull Request review bot. This bot receives pull requests using a polling technique, where it asks the GitHub API every so often if there's a new event. If there is a pull request that happened, the bot takes it and uses a predetermined AI (currently Gemini, though it could be swapped for Claude or ChatGPT) to evaluate the code. If there are problems with the code, the bot writes that feedback back to whoever submitted the PR, as a comment directly on GitHub.

I built this as a way to learn the GitHub API, LLM prompt design, and how to build something that actually runs on its own instead of just answering one-off questions.

## How it works

The bot checks the repo for open pull requests every few minutes. For each one, it pulls the diff (just the code that changed), sends it to Gemini with a prompt asking it to review the code and return its findings as structured JSON, then posts that as a comment on the PR. It also keeps track of which commits it's already reviewed, so it doesn't spam the same PR with duplicate comments every time it checks.

## Stack

- Python
- GitHub REST API (fetching PRs/diffs, posting comments)
- Google Gemini API (gemini-3.7-flash)
- python-dotenv for handling API keys

## A few decisions worth explaining

Polling instead of webhooks. Webhooks would be more efficient (GitHub pushes updates to you instantly instead of you checking on a timer), but they need a publicly reachable server to receive them. Polling was simpler to get working for a first version, and it's a reasonable trade-off when you're prioritizing finishing a working project over building infrastructure. Webhooks would be the natural next step if I revisited this.

Structured JSON output instead of plain text. I originally had Gemini just return a written paragraph, but switched to asking for JSON (a summary plus a list of issues with severity ratings) so the bot could actually do something with the response, like format it consistently or, in theory, filter out low-priority stuff.

## Does it actually work?

Yes. I tested it against a PR with a few intentionally planted problems: a SQL injection vulnerability, a hardcoded password, a divide-by-zero bug, and an unused import. The bot caught all four and correctly rated the security issues as higher severity than the style issue.

## Running it yourself

pip install requests python-dotenv google-genai

Add a .env file:

GITHUB_TOKEN=your_github_token
GEMINI_API_KEY=your_gemini_key

Update OWNER and REPO in bot.py to point at whatever repo you want it watching, then:

python bot.py

## What I'd add next

- Webhooks instead of polling, for real-time reviews
- Support for watching multiple repos at once
- Breaking up large diffs by file instead of reviewing everything in one shot
- Skipping auto-generated files like lockfiles

Built as a personal project while studying AI engineering.

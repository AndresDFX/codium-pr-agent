from pr_agent import cli
from pr_agent.config_loader import get_settings
import os

def main():
    provider = "github"  # GitHub provider
    user_token = os.getenv("GITHUB_USER_TOKEN")  # GitHub user token
    openai_key = os.getenv("OPENAI_KEY")  # OpenAI key
    pr_url = os.getenv("PR_URL")  # PR URL, provided by GitHub Actions
    command = os.getenv("COMMAND")  # Command to run (e.g., '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)

    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)

if __name__ == '__main__':
    main()

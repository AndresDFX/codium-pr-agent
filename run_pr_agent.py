from pr_agent import cli
from pr_agent.config_loader import get_settings

def main():
    # Fill in the following values
    provider = "github"  # GitHub provider
    user_token = "YOUR_GITHUB_USER_TOKEN"  # GitHub user token
    openai_key = "YOUR_OPENAI_KEY"  # OpenAI key
    pr_url = "YOUR_PR_URL"  # PR URL, e.g., 'https://github.com/yourusername/yourrepo/pull/1'
    command = "/review"  # Command to run (e.g., '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)

    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)

if __name__ == '__main__':
    main()

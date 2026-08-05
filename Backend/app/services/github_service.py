from git import Repo
from pathlib import Path

REPOSITORIES_DIR = Path("repositories")


def validate_github_url(repo_url: str):

    if not repo_url.startswith("https://github.com/"):
        raise ValueError("Invalid GitHub repository URL.")

    parts = repo_url.rstrip("/").split("/")

    if len(parts) < 5:
        raise ValueError("Repository owner or repository name is missing.")


def clone_repository(repo_url: str):

    validate_github_url(repo_url)

    REPOSITORIES_DIR.mkdir(exist_ok=True)

    repo_name = repo_url.rstrip("/").split("/")[-1]

    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    repo_path = REPOSITORIES_DIR / repo_name

    # ✅ Repository already exists
    if repo_path.exists():
        print(f"Repository '{repo_name}' already exists. Using existing copy.")
        return repo_path

    try:
        print(f"Cloning repository '{repo_name}'...")

        Repo.clone_from(
            repo_url,
            repo_path
        )

        print("Repository cloned successfully.")

    except Exception as e:
        raise ValueError(
            f"Failed to clone repository: {str(e)}"
        )

    return repo_path
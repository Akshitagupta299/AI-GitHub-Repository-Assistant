import os

IGNORED_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    "venv",
    ".venv"
}

# Programming/source file types
ALLOWED_EXTENSIONS = {
    ".py",
    ".java",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".md",
    ".json",
    ".yaml",
    ".yml"
}

#Special configuration files
IMPORTANT_FILES = {
    "requirements.txt",
    "Dockerfile",
    ".env.example",
    "Makefile"
}

def get_repository_files(repository_path: str):

    repository_files = []

    # Visits every folder
    for root, dirs, files in os.walk(repository_path):

        dirs[:] = [
            directory
            for directory in dirs
            if directory not in IGNORED_DIRS
        ]

        # Visits every file inside that folder
        for file in files:

            full_path = os.path.join(root, file)

            _, extension = os.path.splitext(full_path)

            if extension in ALLOWED_EXTENSIONS:
                repository_files.append(full_path)

    return repository_files
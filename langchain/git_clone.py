from pathlib import Path
import subprocess

def clone_repo(url: str) -> Path:
    repo_name = url.rstrip("/").split("/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    save_dir = Path("langchain/repositories") / repo_name

    if not save_dir.exists():
        subprocess.run(
            ["git", "clone", url, str(save_dir)],
            check=True
        )

    return save_dir
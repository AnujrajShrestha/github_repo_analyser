from git_clone import clone_repo
from db import run_db

user_input= input("Enter repository name: ")
clone_repo(user_input)
run_db(user_input)
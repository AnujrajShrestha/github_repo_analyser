from db import run_db
from git_clone import clone_repo

def run_url():
   repo_url= input("Enter repositority url: ")
   clone_repo(repo_url)
   retriever=run_db(repo_url)
   return {
       'url':repo_url,
       'retriever': retriever
   }
   
   
import os
import subprocess
import requests
import time
from datetime import datetime

ngrok_path = r'd:\ngrok'
command = 'ngrok http 5021'
subprocess.Popen(command, cwd=ngrok_path, shell=True)

time.sleep(5)

url = 'http://127.0.0.1:4040/api/tunnels'
response = requests.get(url)

if response.status_code == 200:
    public_link = response.json()['tunnels'][0]['public_url']

    with open("link.txt", "w+") as link_file:
        link_file.write("public_link")
    
else:
    raise Exception(f"Failed to retrieve tunnels. Status code: {response.status_code}")

git_repo_path = os.getcwd()  # Set to the current folder
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
commit_message = f'Link Update [{timestamp}]'

subprocess.run(['git', 'add', '.'], cwd=git_repo_path, shell=True)
subprocess.run(['git', 'commit', '-m', commit_message], cwd=git_repo_path, shell=True)

# Step 6: Run 'git push origin master'
subprocess.run(['git', 'push', 'origin', 'master'], cwd=git_repo_path, shell=True)
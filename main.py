import requests

response = requests.get("https://gitlab.com/api/v4/users/techworld-with-nana/projects")
my_projects = response.json()

for project in my_projects:
    print(f"project-name: {project['name']}\n project-url: {project['web_url']}\n")

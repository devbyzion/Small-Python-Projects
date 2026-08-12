import requests

def get_github_user():

    name = input("Enter Github username:\n ")
    url = f"https://api.github.com/users/{name}"
    try: 
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        user = response.json()
        return user
    
    except requests.exceptions.RequestException as e:
        print(f"Failed: {e}")
        
user = get_github_user()
    
print("Username",user["login"], "\nPublic Repositories", user["public_repos"], "\nFollowers:", user["followers"])
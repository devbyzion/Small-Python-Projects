import requests 

url = "https://api.github.com/users/devbyzion"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    user = response.json()
    
    print("Username:", user["login"], "\nPublic repositories:",
        user["public_repos"], "\nFollowers:", user["followers"] )

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
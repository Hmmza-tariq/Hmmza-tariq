import requests
from bs4 import BeautifulSoup

# Function to fetch latest apps from App Store developer page
def fetch_latest_apps():
    url = "https://play.google.com/store/apps/dev?id=8768216911832834755"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract app names from the developer page
    app_names = [app.text.strip() for app in soup.find_all('a', class_='app-link')]
    return app_names

# Function to update README.md with latest apps list
def update_readme_with_apps(apps):
    with open('README.md', 'w') as readme_file:
        readme_file.write('# Latest Apps\n\n')
        for app in apps:
            readme_file.write(f'- {app}\n')

# Main function
def main():
    latest_apps = fetch_latest_apps()
    update_readme_with_apps(latest_apps)
    print("README.md updated with latest apps.")

if __name__ == "__main__":
    main()

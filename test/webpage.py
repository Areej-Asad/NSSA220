# review ex2
# fetches webpage "https://www.rit.edu/" & stores its html code in
# file called page.html

import requests

url = "https://www.rit.edu/"

response = requests.get(url)

if response.status_code == 200:
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("HTML content saved to page.html")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")



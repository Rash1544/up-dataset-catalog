import requests

print("Program Started")

url = "https://data.gov.in/api/3/action/package_search?q=uttar+pradesh&rows=5"

response = requests.get(url, timeout=20)

print("Status Code:", response.status_code)

print(response.text[:500])

print("Program Finished")
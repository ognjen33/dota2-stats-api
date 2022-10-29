from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def get_heroes():
    auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiJodHRwczovL3N0ZWFtY29tbXVuaXR5LmNvbS9vcGVuaWQvaWQvNzY1NjExOTgwNDcwMDk3NjgiLCJ1bmlxdWVfbmFtZSI6Imhvb250ZXIiLCJTdWJqZWN0IjoiYzBjZGVkNWYtZTE0ZS00ZDU4LWEzOTEtMTFhNDEwODJkZGIzIiwiU3RlYW1JZCI6Ijg2NzQ0MDQwIiwibmJmIjoxNjY2OTgyNTM2LCJleHAiOjE2OTg1MTg1MzYsImlhdCI6MTY2Njk4MjUzNiwiaXNzIjoiaHR0cHM6Ly9hcGkuc3RyYXR6LmNvbSJ9._S-lLnETMYsJHzIaYpDcuLRZpADA1ZyUy_Nr3b3Xkb8'
    headers = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get("https://api.stratz.com/api/v1/Hero", headers=headers)
    return response.json()
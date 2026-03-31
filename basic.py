import requests

url = "https://raw.githubusercontent.com/naijilnj/foss-greenspace/master/test_api.py"
code = requests.get(url).text

with open("script.py", "w", encoding="utf-8") as f:
    f.write(code)


print(code)
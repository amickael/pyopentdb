import requests

req = requests.get("https://opentdb.com/api_category.php")
data = req.json()["trivia_categories"]
for cat in data:
    ident = cat["id"]
    name = cat["name"]
    enum = name.upper().replace(" ", "_").replace(":", "_").replace("&", "_").strip()
    enum = enum.replace("___", "_").replace("__", "_")
    print(f'{enum} = CategoryItem({ident}, "{name}")')

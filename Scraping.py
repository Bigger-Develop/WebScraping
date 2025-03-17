import requests as re
while True:
    response = re.get(input('URL: '))
    Code = response.text

    with open('Main.txt', "w", encoding="utf-8") as file:
        file.write(Code)
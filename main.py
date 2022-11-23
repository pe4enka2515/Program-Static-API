import requests

x, y = input("Первые координаты: "), input("Вторые коордианты: ")
while True:
    try:
        image = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={y},{x}&spn=0.01,0.01&l=sat")
        with open("map.png", "wb") as file:
            file.write(image.content)
        print("Изображение сохранено" + "\n")
        print()
    except Exception:
        print("Некорректные координаты!")
    finally:
        x, y = input("Первые координаты: "), input("Вторые коордианты: ")
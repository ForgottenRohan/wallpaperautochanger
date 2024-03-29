import os
import random
import ctypes

path = 'C:\\Users\\theDima\\Pictures\\4K Wallpapers by Howdy & Cat of Bar'


def random_wallpaper(path: str) -> str:
    amount = os.listdir(path=path)
    image = random.choice(amount)
    full_path = path + '\\' + image
    return full_path


if __name__ == '__main__':
    full_path = random_wallpaper(path=path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 3)

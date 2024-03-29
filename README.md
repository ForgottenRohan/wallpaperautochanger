# AutoChanger Random Wallpaper from Directory

Выбирает случайное изображение из папки и использует как обои рабочего стола.

# Инструкция

## 1. Выбираем папку.

### _Например_

```
 C:/autochanger
```

## 2. Вводим путь до папки с обоями в main.py.

### _Например_

```python
path = "C:/ОчКрутыеОбои/"
```
Я использую [крутой пак обоев от Хауди Хо](https://drive.google.com/file/d/1-4Ii9UQHCc_uikwNbnLdpMlOXkAbNPP3/view?usp=sharing)

## 3. _Если на Windows_, нажимаем Win + R и вводим.

```
shell:startup
```
## 4. В открытой папке создаем файл *anything.bat*, открываем и вводим.
```bat
@ECHO OFF
python3 C:/путь_до_файла/main.py
```
@ECHO OFF - если не хотите чтобы открывалась консоль перед выполнением скрипта.
## 5. Готово, празднуем!
Теперь, когда вы запустите систему, автоматически случайно установится изображение как обои рабочего стола.

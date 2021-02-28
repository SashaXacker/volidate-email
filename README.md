# Volidate Email
Проверка почт на их существование
## _Проверка почт на их существование_


Это приложение поможет вам при создании почты
Вы можете придумать имя почты, а програма проверит его на разных доменах
Домены которые проверяет программа изначально

- gmail.com
- yandex.ru
- outlook.cm
- mail.ru

## Установка программы
У вас должен быть установлен [Python 3.x](https://python.org/)
Скачайте папку проекта и зайдите в нее.
Далее откройте в ней терминал и выполните следующую команду:
Если у вас Linux/MacOs:
```sh
pip3 install -r requirements.txt
```
Если у вас Windows:
```sh
pip install -r requirements.txt
```


## Работа с приложением
Запустите файл `main.py` следующей командой:
Если у вас Linux/MacOs:
```sh
python3 main.py
```
Если у вас Windows:
```sh
python main.py
```
Далее программа попросит вас ввести имя и сама подставит домены для поиска почт.

## Расширение доменов для поиска
В списке `emailist` добавтье строчку 
```sh
f'{name}@example.com'
```
P.S
Прошу не трогать тестовую почту. В ней нет ничего нужного, она ни к чему не привязана и нужна только для работоспособности этой программы.
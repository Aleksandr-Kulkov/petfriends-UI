# petfriends-UI

UI-тестирование веб-приложения PetFriends (https://petfriends.skillfactory.ru/) с использованием Selenium.

Browser - Chrome 129.0.6668.71 (скачан соответствующий chromedriver).

Файл wait.py - файл с тестами.

Перед запуском тестов необходимо в файле wait.py в переменной pytest.driver вместо <path_to_driver> указать путь до проекта.

При тестировании применены следующие библиотеки:
- pytest - версия 6.2.5
- pytest-selenium - версия 4.0.0
- selenium - версия 4.9.0

В тестах использовано явное и неявное ожидания элементов.

Команда для запуска тестов в терминале PyCharm (вместо <path_to_driver> необходимо указать путь до проекта):
python -m pytest -v --driver Chrome --driver-path <path_to_driver>/chromedriver-win64/chromedriver
.exe petfriends-selenium/wait.py

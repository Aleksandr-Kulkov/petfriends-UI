# petfriends-UI

UI-тестирование веб-приложения PetFriends (https://petfriends.skillfactory.ru/) с использованием Selenium.

Browser - Chrome 129.0.6668.71 (скачан соответствующий chromedriver).

При тестировании применены следующие библиотеки:
- pytest - версия 6.2.5
- pytest-selenium - версия 4.0.0
- selenium - версия 4.9.0

Файл wait.py - файл с тестами.

Перед запуском тестов необходимо:
- скачать архив с файлом chromedriver в соответствии с версией браузера Chrome по ссылке https://developer.chrome.com/docs/chromedriver/downloads?hl=ru, разархивировать архив, переместить папку с файлом chromedriver в папку проекта;
- в файле wait.py в переменной pytest.driver вместо <path_to_driver> указать путь до проекта.

Команда для запуска тестов в терминале PyCharm (вместо <path_to_driver> необходимо указать путь до проекта):

python -m pytest -v --driver Chrome --driver-path <path_to_driver>/chromedriver-win64/chromedriver
.exe petfriends-selenium/wait.py

В тестах использовано явное и неявное ожидания элементов.

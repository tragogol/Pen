**Подготовка:**


Для запуска необходим Python3.6:

`apt-get -y update`\
`apt-get install -y python3.6`\
`apt-get install -y python3.6-pip`

Установка библиотек:

`pip3 install -r requirements`

Для установки пути к тесту: python -m test.test_pen

**Запуск:**

Для запуска всех тестов в директории test: `pytest -v`\
Для запуска теста с определённым тегом(mark) [init, writefunc, others]: `pytest -v -m mark_name `\
Для запуска определенного теста: `pytest -v test/test_pen.py::test_name`




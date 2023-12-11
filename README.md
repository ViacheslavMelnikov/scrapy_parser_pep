# Проект асинхронный парсер PEP

Созданный проект позволяет проводить асинхронный парсинг страницы https://peps.python.org/
с извлечением статусов PEP указанных в соответствующей карточке PEP.
Программа подсчитывает количество PEP по каждому статусу и выводит результат в двух csv-файлах,
файлы сохраняются в папке results.

В первых файл выводится список всех PEP. Файл содержит три столбца: 
- номер
- название
- статус

Маска файла pep_ДатаВремя.csv, например — pep_2029-01-31T23-55-00.csv

Второй файл содержит информацию со сводкой по статусам.
В файле два стобца «Статус» и «Количество». Последняя строка содержит результирующую информацию.


# Как запустить проект:

## Клонировать репозиторий и перейти в него в командной строке:

git clone ...

## Cоздать и активировать виртуальное окружение:

python3 -m venv venv

source venv/bin/activate

## Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

## Запустить проект:

scrapy crawl pep

## Примеры получаемых запросов в файле отражающим список PEP:
number,name,status
1,PEP Purpose and Guidelines,Active
5,Guidelines for Language Evolution,Superseded
9,Sample Plaintext PEP Template,Withdrawn
6,Bug Fix Releases,Superseded
7,Style Guide for C Code,Active

## Примеры получаемых запросов в файле со сводкой по статусам PEP:
Статус,Количество
Active,32
Superseded,23
Withdrawn,57
Final,281
Rejected,124
Draft,30
Accepted,47
Deferred,36
Provisional,2
April Fool!,1
Total,633
# Использованы асинхронные технологии фреймворка Scrapy с записью в режиме получения данных (item) и запись аккумулированных данных в файлы csv.

# Автор проекта
Мельников Вячеслав Александрович
e-mail: melnikov.plusm@yandex.ru
nik rqprograz

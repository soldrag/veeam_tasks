# Veeam_tasks

    Запуск всех заданий через main.py
    Зависимости в requirements.txt
    Необходим Python 3.8+, так как во втором задании используется моржовый оператор
    В проекте написано несколько юниттестов. Они лежат в папке tests. Запустить можно из корня проекта
    python3 -m unittest discover -v -s tests -p "*_test.py"

## Task_1
    Реализовать программу, осуществляющую копирование файлов в соответствии с конфигурационным файлом.  
    Конфигурационный файл должен иметь формат xml. Для каждого файла в конфигурационном файле должно  
    быть указано его имя, исходный путь и путь, по которому файл требуется скопировать.

### Пример
#### Конфигурационный файл:
    <config>
      <file
            source_path="C:\Windows\system32"
            destination_path="C:\Program files"
            file_name="kernel32.dll"
            />
      <file
            source_path="/var/log"
            destination_path="/etc"
            file_name="server.log"
            />
    </config>
## Реализация
    Для запуска есть флаги
    "-i" - Игнорировать ошибки и продолжать копирование
    "-с" - При отсутствии папки назначения, создавать ее
    "-f" - перезаписывать файлы не спрашивая, иначе будет появляться диалог с запросом.
    main.py -i -c -f config.xml

## Task_2
    Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие  
    им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите  
    программу, читающую данный файл и проверяющую целостность файлов.
    Если в троке недостаточно аргументов (меньше 3), то она пропускается.

### Пример
#### Файл сумм:
    file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906
    file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
    file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
    file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709
### Пример вызова:  
    <your program> <path to the input file> <path to the directory containing the files to check>
### Формат вывода:
    file_01.bin OK
    file_02.bin FAIL
    file_03.bin NOT FOUND
    file_04.txt OK
## Реализация
    Добавил проверку что метод хеширования поддерживается, а так же что сам хеш валидный, чтобы попусту  
    не гонять хеш функции по файлам. 
    И тут всплывает одна особенность. Если файла для хеширования нету, но метод хеширования или сам хеш при  
    этом невалидные, будет сообщение именно FAIL, а не NOT FOUND

## Task_3
    Напишите прототип тестовой системы, состоящей из двух тест-кейсов. В данной задаче использование  
    стороннего модуля для автоматизации тестирования не приветствуется.  
    Тестовая система представляет собой иерархию классов, описывающую тест-кейсы.  
### У каждого тест-кейса есть:
    - Номер (tc_id) и название (name)
    - Методы для подготовки (prep), выполнения (run) и завершения (clean_up) тестов. 
    - Метод execute, который задаёт общий порядок выполнения тест-кейса и обрабатывает исключительные  
    ситуации. 
    Все этапы выполнения тест-кейса, а также исключительные ситуации должны быть задокументированы в лог-файле  
    или в стандартном выводе.

### Тест-кейс 1: Список файлов
    [prep] Если текущее системное время, заданное как целое количество секунд от начала эпохи Unix,  
    не кратно двум, то необходимо прервать выполнение тест-кейса.
    [run] Вывести список файлов из домашней директории текущего пользователя.
    [clean_up] Действий не требуется.
### Тест-кейс 2: Случайный файл
    [prep] Если объем оперативной памяти машины, на которой исполняется тест, меньше одного гигабайта,  
    то необходимо прервать выполнение тест-кейса.
    [run] Создать файл test размером 1024 КБ со случайным содержимым.
    [clean_up] Удалить файл test.
## Реализация
    Реализовал прототип так, что тесткейсы описываются в отдельном файле. Запуск файла с тесткейсами  
    делается через main.py, модуль с тесткейсами передается первым аргументом "main.py test_cases".
    Инициализация и запуск всех кейсов должен быть прописан в функции "run_tests"
    Чтобы не повторять код, часть логирования реализована декоратором класса. Для сообщений в логах  
    служат докстринги из абстрактного класса.
    
